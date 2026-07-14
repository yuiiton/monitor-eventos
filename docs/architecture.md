# Arquitetura

O **Monitor Eventos** foi desenvolvido seguindo uma arquitetura modular, separando cada responsabilidade em um componente específico da aplicação. Essa organização facilita a manutenção, a adição de novas fontes de eventos e a evolução do projeto.

## Estrutura do projeto

```text
monitor-eventos/
├── core/
│   ├── configs.py
│   ├── database.py
│   ├── models.py
│   └── repository.py
│
├── data/
│   └── monitor.db
│
├── docs
│   ├── architecture.md
│   ├── executation.md
│   └── images
│       ├── email.png
│       └── terminal.png
│
├── notifications/
│   └── email.py
│
├── sources/
│   ├── ifs.py
│
├── .env.example
├── main.py
└── requirements.txt
```

---

# Fluxo da aplicação

A execução da aplicação segue o fluxo abaixo:

```text
            main.py
                │
                ▼
        Criação do banco
                │
                ▼
     Coleta de eventos (sources)
                │
                ▼
    Verificação no banco (repository)
                │
      ┌─────────┴─────────┐
      │                   │
      ▼                   ▼
Já existe?            Evento novo
      │                   │
Não salva no banco   Salva no banco
      │                   │
      └─────────┬─────────┘
                ▼
    Lista de novos eventos
                │
                ▼
     Envio de notificação
```

---

# Componentes

## `main.py`

Responsável por orquestrar todo o fluxo da aplicação.

Durante a execução ele:

- cria o banco de dados caso ainda não exista;
- obtém eventos das fontes cadastradas;
- verifica quais eventos ainda não foram processados;
- salva os novos eventos;
- envia uma única notificação contendo todos os eventos inéditos encontrados.

---

## `sources/`

Contém os módulos responsáveis pela coleta de eventos.

Cada fonte possui seu próprio scraper.

Exemplo:

- `ifs.py`
- `ufs.py` (planejado)

Todos os scrapers devem retornar uma lista de objetos `Event`, permitindo que o restante da aplicação seja independente da origem dos dados.

---

## `core/models.py`

Define o modelo de domínio da aplicação utilizando **SQLModel**.

O modelo `Event` representa um evento coletado por qualquer fonte.

Principais atributos:

- origem (`source`);
- identificador externo (`external_id`);
- título;
- descrição;
- período de inscrição;
- link.

Esse mesmo modelo é utilizado tanto pelo scraper quanto pelo banco de dados.

---

## `core/database.py`

Responsável pela configuração do banco SQLite.

Fornece:

- criação automática das tabelas;
- criação de sessões de acesso ao banco.

---

## `core/repository.py`

Centraliza todas as operações de persistência.

Atualmente possui responsabilidades como:

- salvar eventos;
- verificar se um evento já foi armazenado anteriormente.

Essa separação evita que regras de acesso ao banco fiquem espalhadas pela aplicação.

---

## `notifications/`

Contém os serviços de notificação.

Atualmente existe apenas:

- envio de e-mail via SMTP.

O objetivo dessa separação é permitir a adição de novos canais futuramente, como:

- Telegram;
- Discord;
- WhatsApp;
- Push notifications.

Sem alterar o restante da aplicação.

---

## `data/`

Armazena o banco SQLite utilizado pelo projeto.

O banco mantém o histórico de eventos já encontrados para impedir que notificações duplicadas sejam enviadas.

---

# Banco de dados

O projeto utiliza SQLite devido à simplicidade de configuração.

A identificação de um evento é feita pela combinação de:

- fonte (`source`);
- identificador externo (`external_id`).

Dessa forma diferentes instituições podem possuir identificadores iguais sem gerar conflitos.

Exemplo:

```text
IFS + 748
UFS + 748
```

São considerados eventos distintos.

---

# Extensibilidade

A arquitetura foi projetada para facilitar a adição de novas fontes.

Para integrar um novo portal basta:

1. criar um novo módulo em `sources/`;
2. implementar a coleta dos eventos;
3. retornar uma lista de objetos `Event`;
4. chamar o novo scraper no fluxo principal.

Como todas as fontes utilizam o mesmo modelo de domínio, nenhuma alteração é necessária nas camadas de persistência ou notificação.

---

# Tecnologias utilizadas

- Python 3
- Requests
- BeautifulSoup4
- SQLModel
- SQLite
- SMTP (e-mail)
- python-dotenv
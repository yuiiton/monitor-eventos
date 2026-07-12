# Monitor Eventos

Monitor Eventos é uma ferramenta em Python que acompanha portais de eventos de instituições de ensino, identifica novos eventos publicados e envia notificações automaticamente.

O objetivo do projeto é evitar a necessidade de acessar manualmente diferentes portais todos os dias em busca de oportunidades como palestras, minicursos, oficinas, semanas acadêmicas, visitas técnicas e outros eventos.

## Funcionalidades

* Monitoramento automático de portais de eventos.
* Detecção de novos eventos.
* Persistência dos eventos em banco SQLite.
* Notificações por e-mail.
* Arquitetura preparada para adicionar novas fontes de eventos.

## Fontes suportadas

| Instituição                           | Status               |
| ------------------------------------- | -------------------- |
| Instituto Federal de Sergipe (IFS)    | ✅ Em desenvolvimento |
| Universidade Federal de Sergipe (UFS) | 🚧 Planejado         |

## Estrutura do projeto

```text
monitor-eventos/
├── core/              # Banco de dados e modelos
├── data/              # Banco SQLite
├── notifications/     # Serviços de notificação
├── sources/           # Scrapers das instituições
├── main.py
└── requirements.txt
```

## Tecnologias

* Python
* Requests
* BeautifulSoup4
* SQLModel
* SQLite

## Roadmap

* [ ] Estrutura inicial do projeto
* [ ] Primeiro scraper do IFS
* [ ] Persistência em SQLite
* [ ] Detecção de novos eventos
* [ ] Notificações por e-mail
* [ ] Suporte ao portal da UFS

## Motivação

Este projeto nasceu da necessidade de acompanhar oportunidades acadêmicas em diferentes instituições sem precisar consultar cada portal manualmente todos os dias.

Além de resolver esse problema, o projeto serve como um estudo sobre scraping, persistência de dados, automação e arquitetura de software em Python.

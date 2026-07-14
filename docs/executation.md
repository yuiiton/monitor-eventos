# Executando o Monitor Eventos

Este documento descreve como configurar e executar o **Monitor Eventos** localmente.

## Pré-requisitos

Antes de começar, certifique-se de possuir:

- Python 3.13 ou superior
- Git
- Uma conta Google para envio das notificações por e-mail

---

## 1. Clonar o repositório

```bash
git clone https://github.com/yuiiton/monitor-eventos.git
cd monitor-eventos
```

---

## 2. Criar um ambiente virtual

### Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Configurar as variáveis de ambiente

Copie o arquivo de exemplo:

```bash
cp .env.example .env
```

ou, no Windows:

```powershell
copy .env.example .env
```

Depois edite o arquivo `.env`.

Exemplo:

```env
EMAIL_USER=seuemail@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
EMAIL_TARGET=destinatario@gmail.com
```

### Campos

#### EMAIL_USER

Conta do Gmail que será utilizada para enviar as notificações.

Exemplo:

```env
EMAIL_USER=meuprojeto@gmail.com
```

#### EMAIL_PASSWORD

Senha de aplicativo gerada pelo Google.

> **Importante:** não utilize sua senha normal da conta Google.

Para gerar uma senha de aplicativo:

1. Ative a autenticação em duas etapas na sua conta Google.
2. Acesse a página de Senhas de App da sua conta Google.
3. Gere uma nova senha para o projeto.
4. Copie a senha gerada para o campo `EMAIL_PASSWORD`.

#### EMAIL_TARGET

Endereço que receberá as notificações.

Pode ser o mesmo e-mail utilizado para enviar ou qualquer outro endereço válido.

---

## 5. Executar o projeto

Execute:

```bash
python main.py
```

Na primeira execução:

- o banco SQLite será criado automaticamente;
- todos os eventos encontrados serão armazenados;
- caso existam eventos inéditos, uma notificação será enviada por e-mail.

Nas próximas execuções, apenas eventos novos serão enviados.

---

# Execução automática

O Monitor Eventos também pode ser executado periodicamente de forma automática.

A forma de configuração depende do sistema operacional utilizado.

Algumas opções são:

- **Linux:** `cron` ou `systemd timers`;
- **Windows:** Agendador de Tarefas (Task Scheduler);
- **macOS:** `launchd`.

Uma configuração comum é executar o programa algumas vezes por dia, por exemplo:

- a cada 6 horas;
- duas vezes ao dia;
- uma vez por dia.

Dessa forma, o monitor verifica automaticamente se novos eventos foram publicados e envia notificações apenas quando encontrar novidades.

---

# Estrutura de armazenamento

Os eventos já processados são armazenados em um banco SQLite localizado em:

```
data/monitor.db
```

Esse banco permite que o projeto identifique quais eventos já foram enviados anteriormente, evitando notificações duplicadas.

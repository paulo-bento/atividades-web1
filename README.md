# 🌐 GlobalDocs – Acompanhamento Multilíngue de Pedidos

## 📚 Descrição
Sistema Django que permite o cadastro e acompanhamento de pedidos internacionais, com foco em recursos avançados: envio de e-mail, signals, middleware, testes, i18n, fixtures, serviço, uso de variáveis de ambiente e preparo para deploy.

## 🧩 Funcionalidades
- Cadastro de pedidos com envio de documentos.
- Confirmação por e-mail usando `EmailMessage`.
- Signal para notificação automática após criação.
- Middleware que loga o tempo de execução da requisição.
- Camada de serviço (`services/`) para lógica de negócio.
- Camada de repositórios (`repositories/`) para separar responsabilidades.
- Tradução automática para inglês e português (i18n).
- Testes automatizados com Django Test Framework.
- Seeders/Fixtures com status de pedidos.
- Deploy com Gunicorn e WhiteNoise.
- Uso de `.env` para configurações sensíveis.

## 🚀 Instruções de Execução

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata app/fixtures/status.json
python manage.py createsuperuser
python manage.py runserver
```

## 🧪 Executar testes

```bash
python manage.py test
```

## 📦 Deploy

- Configure `gunicorn`, `collectstatic` e `WhiteNoise` no `settings.py`
- Utilize variáveis do `.env` com `python-decouple`

---

## 🤝 **Dúvidas?**

Caso tenha dúvidas, entre em contato pelo **Discord** ou pelo e-mail do professor. Bons estudos e divirta-se! 🐍

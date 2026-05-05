# Django Avançado I - Atividade Prática 🚀

## 📌 **Sobre a Atividade**

Esta atividade faz parte da disciplina de **Desenvolvimento Web I** no curso de **Análise e Desenvolvimento de Sistemas da UNIFIP**, ministrada pelo professor **José Matheus**.

Este repositório contém uma aplicação Django **pré-escrita**, mas **incompleta**. O objetivo será **completar e aprimorar** a aplicação adicionando funcionalidades como:

✅ **Soft Delete**  
✅ **Auditoria (`BaseModel`)**  
✅ **Consultas avançadas (`annotate`, `filter`, `gt`, `lt`, etc.)**  
✅ **Configuração segura com `.env`**  
✅ **Configuração de banco de dados (PostgreSQL e MySQL)**  
✅ **Manipulação de arquivos de mídia e estáticos**  
✅ **Criação do modelo `Order` para consultas avançadas**

---

## 🎯 Objetivo da Atividade

Cada aluno deverá **completar a aplicação** implementando os seguintes recursos:

- [ ] **Configuração Segura**: Adicionar suporte a `.env` para armazenar credenciais do banco de dados.
- [ ] **Herança de Modelos**: Criar um **modelo base (`BaseModel`)** contendo auditoria (`created_at`, `updated_at`).
- [ ] **Soft Delete**: Implementar um sistema de exclusão lógica (`is_deleted`).
- [ ] **Configuração de Banco de Dados**: Adicionar suporte para **PostgreSQL ou MySQL**.
- [ ] **Configuração de Mídia e Arquivos Estáticos**.
- [ ] **Criação do Modelo `Order`**: Implementar o modelo de pedidos e suas consultas avançadas.
- [ ] **Exibir os Resultados**: Criar um template Django para visualizar os dados.

---

## 🔧 Configuração do Ambiente

```sh
git clone https://github.com/matheuslima25/django-revisao.git
cd django-revisao
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

## 🤝 **Dúvidas?**

Caso tenha dúvidas, entre em contato pelo **Discord** ou pelo e-mail do professor. Boa prática e divirta-se! 🚀

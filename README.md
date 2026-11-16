# 🐾 Plataforma Web de Gestão e Adoção Responsável — ONG Patas & Esperança

> **Projeto de Software — Experiência Prática III**  
> Aluno: **Yury** | Usuário GitHub: [@yuryfigueiredo](https://github.com/yuryfigueiredo)  
> Alinhamento com a Agenda 2030: **ODS 15 — Vida Terrestre (Meta 15.5)** e **ODS 11 — Cidades e Comunidades Sustentáveis**

---

## 📌 Sobre o Projeto
Este repositório contém a implementação do Minimum Viable Product (MVP) desenvolvido para atender às necessidades operacionais e de saúde pública da **ONG Patas & Esperança (Associação de Proteção e Resgate Animal)**.

O sistema substitui o controle manual e descentralizado em papéis e chats de redes sociais por uma aplicação web responsiva que centraliza:
1. **Catálogo Público de Animais:** Vitrine web com filtros rápidos (espécie, porte) e badges de vacinação.
2. **Formulário de Triagem de Adoção:** Coleta estruturada de critérios de posse responsável (moradia, telas de proteção).
3. **Painel Administrativo da ONG:** Gestão autenticada de prontuários profiláticos de vacinas, castração e lares temporários.

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem Principal:** Python 3.12
- **Framework Web / API:** FastAPI + Uvicorn
- **ORM e Banco de Dados:** SQLAlchemy 2.0 com SQLite local e suporte a PostgreSQL 16
- **Validação de Dados:** Pydantic v2
- **Segurança & Criptografia:** Passlib (BCrypt com salt) e PyJWT
- **Testes Automatizados:** Pytest e Pytest-Coverage
- **Integração Contínua (CI):** GitHub Actions
- **Front-end:** HTML5 Semântico, Bootstrap 5.3 e Vanilla JS (Mobile-First)

---

## 🚀 Como Executar o Projeto Localmente

```bash
# 1. Clonar o repositório
git clone https://github.com/yuryfigueiredo/ong-patas-esperanca.git
cd ong-patas-esperanca

# 2. Criar e ativar o ambiente virtual
python -m venv venv
# No Windows:
.\venv\Scripts\activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Executar os testes automatizados com cobertura
pytest --cov=app --cov-report=term-missing

# 5. Iniciar o servidor de desenvolvimento
uvicorn app.main:app --reload --port 8000
```
Acesse a aplicação em `http://localhost:8000` e a documentação interativa Swagger em `http://localhost:8000/docs`.

---

## 🧪 Estrutura de Testes Automatizados
O projeto conta com cobertura de testes unitários e de integração abrangendo:
- Criação e consulta de animais (`test_animals.py`)
- Submissão e validação de candidaturas de triagem (`test_candidaturas.py`)
- Hashing de senhas e autenticação segura com JWT (`test_auth.py`)

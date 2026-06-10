# 🧮 Calculadoras Malucas

## 📄 Descrição

Este projeto é uma API RESTful de calculadoras matemáticas desenvolvida com Flask. Cada calculadora expõe uma rota própria e aplica uma lógica de cálculo diferente sobre os dados recebidos via requisição POST. Este projeto foi criado com fins educacionais para praticar conceitos de APIs REST, injeção de dependência, tratamento de erros e testes unitários. As 3 primeiras calculadoras foi desenvolvido em aula, já a 4 foi o desafio passado e desenvolvido

---

## ⚙️ Funcionalidades

- 🔢 **Calculadora 1:** Recebe um número e aplica uma fórmula matemática composta.
- 📊 **Calculadora 2:** Recebe uma lista de números, aplica transformação e retorna o inverso do desvio padrão.
- 📐 **Calculadora 3:** Recebe uma lista de números e verifica a relação entre variância e multiplicação.
- ➗ **Calculadora 4:** Recebe uma lista de números e calcula a **média aritmética**.

---

## 💻 Tecnologias Utilizadas

- Python 3.11
- Flask 3.0.1
- NumPy

### Ferramentas

- Pytest (testes unitários)
- pip (gerenciador de pacotes)

---

## 🚀 Instalando e Rodando o Projeto

Clonar o repositório:

```bash
git clone git@github.com:seu-usuario/calculadoras-malucas.git
```

Acesse o diretório do projeto:

```bash
cd calculadoras-malucas
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows:** `venv\Scripts\activate`
- **Linux/Mac:** `source venv/bin/activate`

Instale as dependências:

```bash
pip install -r requeriments.txt
```

Execute a aplicação:

```bash
python run.py
```

O servidor estará disponível em: `http://localhost:3000`

---

## 🧪 Rodando os Testes

```bash
pytest src/calculators/
```

---

## 📜 Licença

Este projeto não está sob nenhuma licença específica.

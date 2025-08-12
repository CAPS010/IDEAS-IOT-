# Contributing to IDEAS-IOT

Thank you for considering contributing to **IDEAS-IOT**!  
This project is built to be collaborative, so whether you’re fixing bugs, adding features, or improving documentation, your help is welcome.

---

## 📌 How to Contribute

### 1️⃣ Fork & Clone the Repository
First, fork the repository on GitHub and clone it locally:
```bash
git clone https://github.com/<your-username>/IDEAS-IOT-.git
cd IDEAS-IOT-
2️⃣ Create a Branch
Use a descriptive branch name for your changes:

bash
Copy
Edit
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/short-description
3️⃣ Make Your Changes
Keep your code readable and well-commented.

Follow the PEP 8 Python style guide.

Update or add tests for new features.

If you modify environment variables, update .env.example.

4️⃣ Test Your Changes
Before committing, ensure everything runs smoothly:

bash
Copy
Edit
pytest          # If tests are present
flask run       # To check the app works locally
5️⃣ Commit Your Changes
Write clear, concise commit messages:

bash
Copy
Edit
git add .
git commit -m "Add: description of your change"
6️⃣ Push & Open a Pull Request
Push your branch to your fork:

bash
Copy
Edit
git push origin feature/your-feature-name
Then, open a Pull Request on GitHub:

Explain what you changed

Describe why it’s needed

Reference related issues if any

🛠 Development Guidelines
Code Style
Python: Follow PEP 8

Commit messages: Use Add:, Fix:, Update:, Refactor:, Docs: prefixes when possible.

Keep functions small and focused on a single task.

Security
Never commit secrets or credentials.

Use .env for sensitive data.

Do not expose API keys in code or logs.

Documentation
Update the README.md if you add features or change setup instructions.

Add docstrings to new functions and classes.

💡 Suggestions & Issues
If you have ideas for new features or find a bug:

Open an issue on GitHub

Use the provided template

Include as much detail as possible (screenshots, logs, steps to reproduce)

📜 License
By contributing, you agree that your work will be licensed under the MIT License of this project.
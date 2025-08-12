# Contributing to IDEAS-IOT

Thank you for your interest in contributing to **IDEAS-IOT**\! 🎉 We're excited to have your help. This project is built to be a collaborative effort, and we welcome all contributions, whether you're fixing bugs, adding new features, or improving documentation.

-----

## 📌 How to Contribute

Here’s how you can get started with your contribution.

### 1️⃣ Fork & Clone the Repository

First, create a copy (a "fork") of the repository on GitHub and then download it to your local machine.

```bash
git clone https://github.com/<your-username>/IDEAS-IOT.git
cd IDEAS-IOT
```

### 2️⃣ Create a New Branch

Create a separate branch for your changes. Use a descriptive name that reflects your work.

```bash
# For a new feature
git checkout -b feature/your-awesome-feature

# For a bug fix
git checkout -b bugfix/a-short-description
```

### 3️⃣ Make Your Changes

Now, you can start coding\! As you work, please keep the following in mind:

  * Write **clean, readable, and well-commented** code.
  * Follow the **PEP 8** style guide for Python.
  * Update or add **tests** for any new features.
  * If you add or change environment variables, update the `.env.example` file.

### 4️⃣ Test Your Changes

Before you submit your work, make sure everything is working correctly.

```bash
# Run tests if they are available
pytest

# Run the app locally to check for issues
flask run
```

### 5️⃣ Commit Your Changes

Write a clear, concise commit message that explains what you've done. Using a prefix helps keep the history clean.

```bash
git add .
git commit -m "Fix: Corrected a bug in the data processing module"
```

### 6️⃣ Push & Open a Pull Request

Push your branch to your forked repository on GitHub.

```bash
git push origin feature/your-awesome-feature
```

Finally, go to the original IDEAS-IOT repository on GitHub and open a **Pull Request**. In your PR description, please:

  * Explain the **changes** you made.
  * Describe **why** these changes are needed.
  * Reference any related **issues** (e.g., "Closes \#42").

-----

## 🛠️ Development Guidelines

### Code Style

  * **Python**: Follow the **PEP 8** style guide.
  * **Commit Messages**: Use prefixes like `Add:`, `Fix:`, `Update:`, `Refactor:`, or `Docs:`.
  * **Simplicity**: Keep functions small and focused on a single task.

### Security

  * **Never commit secrets** or credentials (API keys, passwords, etc.).
  * Use a `.env` file for all sensitive data.
  * Ensure that API keys or other secrets are not exposed in logs or printed to the console.

### Documentation

  * If you add a new feature or change the setup, please update the `README.md`.
  * Add clear docstrings to all new functions, classes, and modules.

-----

## 💡 Suggestions & Issues

Have an idea for a new feature or found a bug? 🐛

1.  Go to the **"Issues"** tab on our GitHub repository.
2.  Open a new issue using one of the provided templates.
3.  Include as much detail as possible, such as logs, screenshots, and steps to reproduce the problem.

-----

## 📜 License

By contributing to this project, you agree that your work will be licensed under the project's **MIT License**.
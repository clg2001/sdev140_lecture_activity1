# Python Project Template for Beginners

Welcome! This is a simple Python project template designed to help you get started with Python programming.

## What's in This Project?

This project contains a basic Python program that prints "Hello World" to the screen. It's the perfect starting point for learning Python!

## Setup and Installation

### Using GitHub Codespaces (Recommended for Beginners)

GitHub Codespaces provides a cloud-based development environment - no local setup required!

1. **Clone this template to your account**:
   - Click the **Use this template** button on the repository page
   - Select **Create a new repository**
   - Name your new repository and click **Create repository from template**

2. **Open in Codespaces**:
   - Go to your new repository
   - Click the green **Code** button
   - Select the **Codespaces** tab
   - Click **Create codespace on main**
   - VS Code will open in your browser with Python ready to use

### Using a Local Dev Container

**Prerequisites:**
- [Docker](https://docs.docker.com/get-docker/) installed and running on your machine
- [VS Code](https://code.visualstudio.com/) installed
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

If you prefer to code on your local machine, you can use Docker and VS Code's dev container support:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd python-project-template
   ```

2. **Open in VS Code**:
   - Open the folder in VS Code
   - If you have Dev Containers extension installed, click the blue button in the bottom-left corner
   - Select **Reopen in Container**
   - VS Code will build and open the dev container with Python pre-configured

3. **What's included**:
   - Python 3 and pip3
   - Git
   - All common development tools
   - Full VS Code experience

### Clone for Local Development (Without Dev Container)

**Prerequisites:**
- [Python 3.8 or higher](https://www.python.org/downloads/) installed on your machine
- [Git](https://git-scm.com/) installed
- A text editor or IDE (like VS Code, PyCharm, or similar)

**Steps:**

If you prefer to work without containers:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd python-project-template
python3 main.py
```

You should see `Hello World` printed to your terminal!

## Getting Started

### Step 1: Open the Project

You already have this project open in VS Code. The main file is `main.py`.

### Step 2: Run the Program

To run your Python program, follow these steps:

1. **Using VS Code**: 
   - Open the `main.py` file
   - Click the **Run** button (▶️) in the top right corner of the editor
   - Watch the output appear at the bottom of the screen

2. **Using the Terminal**:
   - Open the terminal (View → Terminal, or press Ctrl+`)
   - Type the command: `python3 main.py`
   - Press Enter to run the program

### Step 3: See the Output

You should see the message:
```
Hello World
```

## How to Customize

Ready to make changes? Try these experiments:

1. **Change the message**: 
   - Open `main.py`
   - Replace `"Hello World"` with your own message
   - Example: `print("My name is Sarah")`

2. **Print multiple lines**:
   - Add more `print()` statements
   - Example:
     ```python
     print("Hello World")
     print("I'm learning Python!")
     print("This is fun!")
     ```

3. **Do some math**:
   - Try these commands inside `print()`:
     ```python
     print(5 + 3)
     print(10 - 2)
     print(4 * 5)
     ```

## Common Commands for Beginners

Here are some useful Python basics to try:

| Command | What it does | Example |
|---------|-------------|---------|
| `print()` | Display text or values | `print("Hello")` |
| `+` | Add numbers | `print(2 + 3)` |
| `-` | Subtract numbers | `print(10 - 4)` |
| `*` | Multiply numbers | `print(3 * 7)` |
| `/` | Divide numbers | `print(20 / 4)` |

## Next Steps

Once you're comfortable with the basics, try:

- Creating **variables** to store information
- Using **input()** to get text from the user
- Writing **if statements** to make decisions
- Using **loops** to repeat actions
- Creating **functions** to organize your code

## Tips for Success

✅ **Run your code often** - Test changes as you make them  
✅ **Start small** - Write one line, test it, then add more  
✅ **Read error messages** - They tell you what went wrong  
✅ **Experiment** - Try new things and see what happens  
✅ **Ask questions** - Reach out to your instructor if you get stuck  

## Need Help?

- Check the [Python Official Documentation](https://docs.python.org/3/)
- Visit [Python.org](https://www.python.org/) for more resources
- Ask your instructor or a classmate
- Use the VS Code integrated help features

## Project Structure

```
python-project-template/
├── main.py          # Your main Python program
├── README.md        # This file - documentation
└── (add more files as your project grows)
```

Happy coding! 🐍

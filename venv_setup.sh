#!/bin/bash
# Name of the virtual environment directory
VENV_DIR="learning_venv"

if [ -d "$VENV_DIR" ]; then
    echo "✅ Virtual environment already exists at ./$VENV_DIR"
else
    echo "📦 Creating virtual environment in ./$VENV_DIR"
    python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment
echo "🚀 Activating virtual environment"
source "$VENV_DIR/bin/activate"

# Optional: Install requirements if present

if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies from requirements.txt"
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "⚠️  No requirements.txt file found. Skipping package installation."
fi

# Confirm Python and pip path
echo "🐍 Python: $(which python)"
echo "📦 Pip: $(which pip)"


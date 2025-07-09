#!/bin/bash

echo "🔒 Saving current LUMATRIX snapshot to Git..."

# Step 1: Show status
echo "🔍 Checking git status..."
git status

# Step 2: Add everything
echo "✅ Staging all changes..."
git add .

# Step 3: Commit with milestone message
echo "✅ Committing..."
git commit -m "✅ Added brand_admin.py — admin tool for self-training brand map"

# Step 4: Show your new log
echo "📜 Recent commits:"
git log --oneline --graph --decorate --all

echo "✅ Git save complete!"
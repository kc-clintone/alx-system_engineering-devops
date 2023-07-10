#!/bin/bash

# Check whether the current directory is a Git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "######---Error: Not a valid Git repository---######"
    exit 1
fi

# Stage all changes for commit
if git add .; then
    echo "******---Changes added successfully---******"
else
    echo "######---Error: Failed to add changes, Try again---######"
    exit 1
fi

# Prompt user to enter commit message
commit_message=""
while [ -z "$commit_message" ]; do
    echo ">>>>>>Enter commit message:"
    read -r commit_message
done

# Commit to git with the provided message
if git commit -m "$commit_message"; then
    echo "******---Commit successful---******"
else
    echo "######---Error: Failed to commit changes, Try again---######"
    exit 1
fi

# Prompt user to provide the target branch or use 'main' as the default
echo ">>>>>>Enter the target branch for pushing the changes (default: main):"
read -r target_branch
target_branch=${target_branch:-main}

# Push the changes to the remote repository (github)
if git push origin "$target_branch"; then
    echo "******---Push successful---******"
else
    echo "######---Error: Failed to push changes, Try again---######"
    exit 1
fi

echo "===============All passed, changes successfully pushed to github================"

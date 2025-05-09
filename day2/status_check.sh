#!/bin/bash

# Set a name variable
NAME="Richard"

# Get the current directory
CURRENT_DIR=$(pwd)

# Color codes
GREEN="\033[0;32m"
RED="\033[0;31m"
NC="\033[0m"  # No Color

# Welcome message
echo -e "${GREEN}Hello, $NAME! Checking environment status...${NC}"

# Directory check
if [[ "$CURRENT_DIR" == *"devops-playground"* ]]; then
  echo -e "${GREEN}✅ You are inside your DevOps playground directory.${NC}"
else
  echo -e "${RED}❌ Warning: You are NOT in the devops-playground folder.${NC}"
fi

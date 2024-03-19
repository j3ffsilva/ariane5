#!/bin/bash

# Parar o script em caso de erro
set -e

# Atualizar e atualizar os pacotes do sistema
sudo apt update && sudo apt upgrade -y

# Instalar nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# Carregar nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # Este carrega nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # Isto carrega a conclusão bash nvm

# Instalar Node.js v16 via nvm e usá-lo
nvm install 16
nvm use 16

# Agora, o Node.js v16 está ativo. Prossiga com a instalação do Newman.
npm install -g newman

# Instalar pip para Python3
sudo apt install python3-pip -y

# Clonar repositório específico do GitHub usando HTTPS para clonagem pública
git clone https://github.com/j3ffsilva/ariane5.git

echo "Instalação e configuração concluídas!"

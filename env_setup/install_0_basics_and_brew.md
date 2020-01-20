# Basics and the only apps to be installed by apt
```
sudo apt install -y zsh build-essential curl wget tree vim 

#Ensure default python is python3
update-alternatives --install /usr/bin/python python /usr/bin/python3 10
```

# Switch to zsh
```
sudo apt install -y zsh

#To change shell to zsh
sudo chsh -s /bin/zsh <username> 

#Get oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

echo 'PROMPT="$fg[cyan]%}$USER@%{$fg[cyan]%}%m ${PROMPT}'>>~/.zshrc

#Log out and log back in, and check if using zsh
echo $0
```


# Brew is used to install simple utilities without sudo to home directory
## Get Brew on MacOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## Get Brew on Linux
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >>~/.zshrc
echo 'PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"'>>~/.zshrc
sudo apt install -y linuxbrew-wrapper
brew update --force
```


# Install some simple Utilities via brew
```
brew install git iterm2
```


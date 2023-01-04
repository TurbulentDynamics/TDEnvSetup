# Ubuntu 22 Basics and the only apps to be installed by apt
```
sudo apt install -y fish build-essential curl wget tree vim openssh-server python3-venv

```

# Switch to fish
```
sudo apt install -y fish

#To change shell to fish
sudo chsh -s /bin/fish <username> 

#Log out and log back in, and check if using fish
echo $0
```


# Brew is used to install simple utilities without sudo to home directory
## Get Brew on MacOS
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
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


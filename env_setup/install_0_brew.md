# Brew is used to install simple utilities without sudo to home directory

# Switch to zsh
```
sudo apt install -y zsh build-essential curl

#To change shell to zsh
sudo chsh -s /bin/zsh <username> 

#Get oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

#Log out and log back in, and check if using zsh
echo $0
```


# Get Brew on MacOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

# Get Brew on Linux
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >>~/.zshrc
echo 'PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"'>>~/.zshrc
sudo apt install -y linuxbrew-wrapper
brew update --force
```


# Install some simple Utilities via brew
```
brew install wget tree vim git iterm2
```


# Brew is used to install simple utilities



# Get Brew on MacOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

# Get Brew on Linux
```bash
apt-get install build-essential curl zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >>~/.profile
echo 'PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"'>>~/.zshrc
apt install linuxbrew-wrapper
brew update --force
```


# Install some simple Utilities via brew
```
brew install wget tree vim git curl 
```


# Switch to zsh
```
brew install zsh iterm2

#To change shell to zsh
sudo chsh -s /bin/zsh <username> 

#Get oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

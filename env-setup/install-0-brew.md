# Brew is used to install simple utilities


# Get Brew on MacOS
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

# Get Brew on Linux
```bash
apt-get install build-essential curl
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

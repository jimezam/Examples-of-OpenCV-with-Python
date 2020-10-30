# Install Python3 + VirtualEnv

## GNU/Linux

### Debian, Ubuntu, Mint

Install *Python3* and *pip3* package installer from software's repository.

```
$ sudo apt install python3 python3-pip 
```

Install *virtualenv* (create isolated Python environments) and *virtualenvwrapper* (wrappers for easy handling *virtualenv* environments) from *pip* repository.

```
$ pip3 install virtualenv virtualenvwrapper
```

Add the following environments variables.

```
$ vi ~/.bashrc

export PATH="$HOME/.local/bin:$PATH"
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
source $HOME/.local/bin/virtualenvwrapper.sh
```
Update the environment variables on the current shell.

```
$ source ~/.bashrc
```

Currently, by default `python` links to `python2` so `python3` executable must be used directly.  To avoid this, install the following package that links directly `python` to `python3`.

``` 
$ sudo apt install python-is-python3
```

# References

 - Python pip  
 https://pypi.org/project/pip/
 - VirtualEnv  
 https://virtualenv.pypa.io/en/latest/
 - Virtual Environments in The Hitchhiker's Guide to Python  
 https://python-guide-es.readthedocs.io/es/guide-es/dev/virtualenvs.html
 - VirtualenvWrapper documentation  
 https://virtualenvwrapper.readthedocs.io/en/latest/
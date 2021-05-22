import pip

_all_ = [
"requests==2.25.0",
  "fake-useragent==0.1.11",

]

windows = ["",]

linux = []

darwin = []

def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':

    from sys import platform

    install(_all_) 
    if platform == 'windows':
        install(windows)
    if platform.startswith('linux'):
        install(linux)
    if platform == 'darwin': # MacOS
        install(darwin)

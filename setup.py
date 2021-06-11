import pip

def install(package):
    try:
        __import__(package)
        print('%s is already installed!' % package)
    except ImportError:
        pip.main(['install', package])   
        print('%s installed' % package)    


if __name__ == "__main__":
    install('pygame')
    install('anytree')
    install('matplotlib')
    install('tqdm')
    install('pandas')
    install('plotly')
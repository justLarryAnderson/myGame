class Color():
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'violet': '\033[35m',
        'turquoise': '\033[36m',
        'white': '\033[37m',
        '-1': ''
    }
    bgcolors = {
        'black': '\033[40m',
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'violet': '\033[45m',
        'turquoise': '\033[46m',
        'white': '\033[47m',
        '-1': ''
    }
    text_styles = {
        'bold': '\033[1m',
        'faded': '\033[2m',
        'italics': '\033[3m',
        'underline': '\033[4m',
        'rare_blinking': '\033[5m',
        'fast_blinking': '\033[6m',
        'with_text_color': '\033[7m',
        '-1': ''
        
    }
    def __init__(self):
        print(
        f'This module designet for printin your text woth color.\nYou can use method info() from Color object to see avaliable colors and text styles.Based on ANSI-codes.\n'
        
        )
        
    def info(self):
        print(
        """
    Avaliable colors list(1)
    Avaliable background color list(2)
    Avaliable text styles list(3)
    Exit(4)
        """
        )
        
        def colors_list():
            ansi = 29
            for key in self.colors.keys():
                ansi+=1
                if key == '-1': continue
                print(f'{key}(ANSI: \\033[{ansi}m). Example: {self.colors[key]}{key.upper()} TEXT\033[0m')            
        def bgcolors_list():
            ansi = 39
            for key in self.bgcolors.keys():
                ansi+=1
                if key == '-1': continue
                print(f'{key}(ANSI: \\033[{ansi}m). Example: {self.bgcolors[key]}{key.upper()} TEXT\033[0m')     
        def text_style_list():
            ansi = 0
            for key in self.text_styles.keys():
                ansi+=1
                if key == '-1': continue
                print(f'{key}(ANSI: \\033[{ansi}m). Example: {self.text_styles[key]}{key.upper()} TEXT\033[0m')
            
        choise = int(input('> '))
        functions = {
            1:colors_list,
            2:bgcolors_list,
            3:text_style_list
        }
        functions[choise]() if choise in [1,2,3] else print('Exit')

    def paint(self, value, color: str = '-1', bgcolor: str = '-1', *text_style):
        try:
            styles = ''.join([self.text_styles[style] for style in text_style])
            
            value =f'{styles}{self.colors[color]}{self.bgcolors[bgcolor]}{value}\033[0m'
            return value
        except KeyError: print('\033[31m\033[47m\033[1m\033[4m\033[3mNot correct value, use info() method from Color class object\033[0m')

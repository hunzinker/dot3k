from dot3k.menu import MenuOption
import subprocess

class Pianobar(MenuOption):
    def __init__(self):
        MenuOption.__init__(self)
        self.pid = None
        self.user = 'pi'
        self.config = '/home/pi/.config/pianobar'
        self.fifo = self.config + '/ctl'
        self.out = self.config + '/out'
        self.ready = False
        self.selected_option = 0
        self.current_station = None
        self.current_state = None
        self.last_update = 0
        self.icons = {
            'play': [0, 24, 30, 31, 30, 24, 0, 0],
            'pause': [0, 27, 27, 27, 27, 27, 0, 0],
            'stop': [0, 31, 31, 31, 31, 31, 0, 0]
        }

    def setup(self, config):
        self.ready = False
        MenuOption.setup(self, config)
        if 'Pianobar' in self.config.sections():
            self.ready = True

    def right(self):
        if self.pid is None:
            self.start()

        if self.selected_option == 1:
            self.send('p')
        elif self.selected_option == 2 and self.current_state == 'playing':
            self.send('q')
        elif self.selected_option == 2 and self.current_state == 'stopped':
            self.send('p')

    def redraw(self, menu):
        if self.millis() - self.last_update > 500:
            self.last_update = self.millis()

        self.redraw_main(menu)

    def redraw_main(self, menu):
        # Row, Text, Icon, Left Margin
        menu.write_option(0, 'Play', chr(252) if self.selected_option == 0 else ' ', 1)
        menu.write_option(1, 'Pause' if self.current_state != 'paused' else 'Resume',
                          chr(252) if self.selected_option == 1 else ' ', 1)
        menu.write_option(2, 'Stop' if self.current_state != 'stopped' else 'Play',
                          chr(252) if self.selected_option == 2 else ' ', 1)

    def send(self, command):
        if self.pid is not None:
            try:
                subprocess.check_ouput(
                    [
                        'su ' + self.user + ' -c "echo -ne \"' +
                            command + '\" > ' + str(self.fifo)]

                )
            except subprocess.CalledProcessError:
                pass

    def start(self):
        if self.pid is None:
            try:
                return_value = subprocess.check_output(['./pianobar.sh'])
                pids = return_value.decode('utf-8').split('\n')[0]
                self.pid = int(pids.split(' ')[0])
                print('Pianobar started with PID: ' + str(self.pid))
            except subprocess.CalledProcessError:
                print('You must have Pianobar installed to use Dot3k Pianobar')
                print('Try: sudo apt-get install pianobar')
                exit()

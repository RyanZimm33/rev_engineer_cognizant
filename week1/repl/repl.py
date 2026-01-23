class BookREPL:
    def __init__(self):
        self.running = True

    def start(self):
        print("Welcome")
        while self.running:
            cmd = input('>>>').strip()
            self.handle_command(cmd)

    def handle_command(self, cmd):
        if cmd == 'exit':
            self.running = False
            print("Bye")
        elif cmd == 'help':
            print("Available commands: help exit")
        else:
            print("invalid")


    def get_all_records(self):
        pass

    def add_book(self):
        pass


if __name__ == '__main__':
    repl = BookREPL()
    repl.start()


import cmd


class MTGCmd(cmd.Cmd):

    def __init__(self, controller):
        self.controller = controller
        cmd.Cmd.__init__(self)

    def start(self):
        self.cmdloop()

    def do_pack_search(self, args):
        try:
            self.controller.scrape_data(args)
        except IndexError:
            print('No information for that pack, please try again')

    def do_show_data(self):
        try:
            self.controller.show_data()
        except IndexError:
            print('No information for that pack, please try again')
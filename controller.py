
class Controller(object):

    @abstractmethod
    def get_pack_name(self):
        pass

    @abstractmethod
    def scrape_data(self, args):
        pass

    @abstractmethod
    def show_data(self, data):
        pass

    @abstractmethod
    def pickle_data(self, data):
        pass

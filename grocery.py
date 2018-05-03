path = 'grocery/list.txt'
class GroceryList:

    def __init__(self):
        load()

    def load(self):
        with open(path, 'r') as f:
            list = f.readlines()
        return list

    def add(self, item):
        with open(path, 'a') as f:
            f.write(item+'\n')

    def reset(self):
        open(path, 'w').close()

    def send():
    """
    This will use the facebook api to send the grocery list as a message to user
    """
        pass


    

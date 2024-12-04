import random 

def pow(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result    

class KeyBox:
    p = 101
    g = 2
    def __init__(self):
        self.own_key = random.randint(0, 10000)
        self.public_key = self.process_public_key()
        self.key = None

    def process_public_key(self):
        return int(pow(KeyBox.g, self.own_key) % KeyBox.p)
    
    def process_key(self, other_key):
        return int(pow(other_key, self.own_key) % KeyBox.p)
    
    def get_public_key(self):
        return self.public_key 
    
    def get_key(self, other_key=None):
        if self.key is None:
            if other_key is None:
                print('未获取对方公钥')
                raise
            else:
                self.key = self.process_key(other_key)
        return self.key
     

if __name__ == '__main__':
    man1 = KeyBox()
    man2 = KeyBox()

    p_key1 = man1.get_public_key()
    p_key2 = man2.get_public_key()

    key1 = man1.get_key(p_key2)
    key2 = man2.get_key(p_key1)

    print(key1)
    print(key2)
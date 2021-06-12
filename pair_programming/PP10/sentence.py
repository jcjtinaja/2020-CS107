from reprlib import repr

class Sentence:
    def __init__(self, text): 
        self.text = text
        self.words = text.split()
        
    def __iter__(self):
        for w in self.words:
            yield w
    
    def __repr__(self):
        return 'Sentence(%s)' % repr(self.text)

if __name__ == "__main__":
    sent = Sentence("Dogs will save the world!")
    for w in sent:
        print(w)
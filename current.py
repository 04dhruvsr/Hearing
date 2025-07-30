class Current(object):
    def __new__ (self):
        if not hasattr(self, 'instance'):
            self.instance = super(Current, self).__new__(self)
            self.current = None
        return self.instance
        

    def set(self, new):
        if self.current != None:
            self.current.background_color = (157/255, 157/255, 157/255, 1)
        self.current = new
        self.current.background_color = (1, 0, 0, 1)

    def get(self):
        if self.current != None:
            return self.current.text
        else:
            out = 0
            return out
    
    def add(self, new):
        if self.current != None:
            if self.current.text != "0":
                self.current.text += new

            else:
                self.current.text = new
    
    def back(self):
        if self.current != None:
            self.current.text = self.current.text[:-1]

            if self.current.text == "":
                self.current.text = "0"
            
            if self.current.text == "Age:":
                self.current.text = "Age: "

            if self.current.text[1:] == "kHz:":
                self.current.text = self.current.text[0] + "kHz: "

    
    def __str__(self):
        if self.current != None:
            return "Some"
        else :
            return "None"
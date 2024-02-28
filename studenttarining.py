class training:
    def __init__(self,lang):
        self.lang=lang
    def section1(self):
        print("training section1:",self.lang)
    def section2(self):
        print("training section2:",self.lang)
obj=training("python")
obj.section1()
obj.section2()

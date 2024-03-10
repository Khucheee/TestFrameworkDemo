class BaseDriver:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def page_scroll(self):
        print("no implementation")
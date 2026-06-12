class Camera:
    def click_photos(self):
        print("Photo Clicked")

class Phone:
    def call(self):
        print("Calling")

class Smartphone(Camera,Phone):
    def browser(self):
        print("browsing internet")

s = Smartphone()
s.click_photos()
s.call()
s.browser()
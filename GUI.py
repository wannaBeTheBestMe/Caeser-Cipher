import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from cipher import caeser_cipher, decode_without_shift


class MyApp(App, FloatLayout):
    input = ObjectProperty("Enter text")
    output = ObjectProperty("Text will appear here")
    shift = ObjectProperty("------")

    def encoder(self):
        string = self.root.ids.input.text
        key = int(self.root.ids.shift.text)
        final = caeser_cipher(string, key)
        self.root.ids.output.text = final

    def decoder(self):
        string = self.root.ids.input.text
        key = -1 * int(self.root.ids.shift.text)
        final = caeser_cipher(string, key)
        self.root.ids.output.text = final

    def decoder_without_shift(self):
        string = self.root.ids.input.text
        final = decode_without_shift(string)["text"]
        key = decode_without_shift(string)["shift"]
        self.root.ids.shift.text = str(key)
        self.root.ids.output.text = final

    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyApp().run()

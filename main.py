import pgi, QRscript

pgi.require_version("Gtk", "3.0")
from pgi.repository import Gtk as gtk


class Main:
    def __init__(self):
        gladeFile = "QrcodeGenerator.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)

        button = self.builder.get_object("generate_button")
        button.connect("clicked", self.buttonClick)

        root = self.builder.get_object("main_window")
        root.connect("delete-event", gtk.main_quit)
        root.show()

    def buttonClick(self, widget):
        entry = self.builder.get_object("entry")
        text = entry.get_text()
        filename = QRscript.qrgeneretor(text=text, filename=text)
        entry.set_text("")
        image = self.builder.get_object("qr_image_file")
        image.set_from_file(filename)


if __name__ == "__main__":
    main = Main()
    gtk.main()

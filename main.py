import gi

gi.require_version("Gtk", "4.0")
gi.require_version("WebKit", "6.0")

from gi.repository import Gtk

from window import MainWindow


class App(Gtk.Application):
    def __init__(self):
        super().__init__(
            application_id="com.devkapi.Pinterest4Linux"
        )

    def do_activate(self):
        window = MainWindow(self)
        window.present()


app = App()
app.run()
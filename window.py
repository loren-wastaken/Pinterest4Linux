import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

from browser import Browser
from ui import LoadingOverlay


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)

        self.set_title("Pinterest4Linux")
        self.set_default_size(1000, 700)

        self.browser = Browser()
        self.loading_overlay = LoadingOverlay()

        self.overlay = Gtk.Overlay()

        self.overlay.set_child(self.browser.webview)

        self.overlay.add_overlay(
            self.loading_overlay
        )

        self.set_child(self.overlay)

        self.browser.connect_loading(
            self.loading_overlay
        )
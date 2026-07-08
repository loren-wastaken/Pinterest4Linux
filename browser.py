import gi

gi.require_version("WebKit", "6.0")

from gi.repository import WebKit


class Browser:
    def __init__(self):
        self.webview = WebKit.WebView()

        self.webview.load_uri(
            "https://www.pinterest.com"
        )

    def connect_loading(self, overlay):
        self.webview.connect(
            "load-changed",
            self.on_load_changed,
            overlay
        )

    def on_load_changed(
        self,
        webview,
        load_event,
        overlay
    ):
        if load_event == WebKit.LoadEvent.FINISHED:
            overlay.hide()
        else:
            overlay.show()
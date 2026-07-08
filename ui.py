import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk


class LoadingOverlay(Gtk.Box):
    def __init__(self):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=15
        )

        self.set_halign(Gtk.Align.CENTER)
        self.set_valign(Gtk.Align.CENTER)

        title = Gtk.Label(
            label="Waiting for Pinterest to load..."
        )

        title.set_margin_top(20)
        title.set_margin_bottom(10)

        self.progress = Gtk.ProgressBar()
        self.progress.set_show_text(False)
        self.progress.set_pulse_step(0.03)

        self.progress_timer = None

        self.start_animation()

        coffee = Gtk.Label(
            label="<i>P.S. Go get some coffee. This might take a while.</i>"
        )

        coffee.set_use_markup(True)

        self.append(title)
        self.append(self.progress)
        self.append(coffee)


    def start_animation(self):
        self.progress_timer = Gtk.Widget.add_tick_callback(
            self,
            self.animate_progress
        )


    def animate_progress(self, widget, frame_clock):
        self.progress.pulse()
        return True
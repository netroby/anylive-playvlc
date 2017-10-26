#!/usr/bin/env python
import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Any Live play via vlc")
        self.set_border_width(10)
        self.set_default_size(480,48)

        self.box = Gtk.Box(spacing = 6)
        self.add(self.box)

        self.entry = Gtk.Entry()
        self.entry.connect("activate", self.on_button_clicked)
        self.entry.set_size_request(320, 32)
        self.box.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button(label="Play")
        self.button.connect("clicked", self.on_button_clicked)
        self.button.set_size_request(40, 32)
        self.box.pack_start(self.button, True, True, 0)


    def on_button_clicked(self, widget):
        url = self.entry.get_text()
        print(url)
        execCmd = ["ykdl", "-p", "vlc", url]
        print(execCmd)
        subprocess.Popen(execCmd)


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()

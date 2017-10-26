#!/usr/bin/env python
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Any Live play via vlc")
        self.set_border_width(10)

        self.box = Gtk.Box(spacing = 6)
        self.add(self.box)

        self.entry = Gtk.Entry()
        self.box.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button(label="Play")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)


    def on_button_clicked(self, widget):
        url = self.entry.get_text()
        print(url)
        execCmd = "ykdl -p vlc " + url
        print(execCmd)
        os.system(execCmd) 


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

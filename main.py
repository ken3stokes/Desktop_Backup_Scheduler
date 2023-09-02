import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import schedule
import time
from ttkthemes import ThemedTk


class BackupApp(ThemedTk):

    def __init__(self):
        super().__init__(theme="radiance")
        self.title("Backup App")
        self.geometry("800x400")
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.sources = [tk.StringVar() for _ in range(5)]
        self.destinations = [tk.StringVar() for _ in range(5)]

        ttk.Label(self.mainframe, text="Backup Sources and Destinations").grid(column=1, row=1, sticky=tk.W, columnspan=6)
        for i in range(5):
            ttk.Label(self.mainframe, text=f"Source {i + 1}:").grid(column=1, row=i + 2, sticky=tk.W)
            ttk.Entry(self.mainframe, textvariable=self.sources[i], width=50).grid(column=2, row=i + 2,
                                                                                   sticky=(tk.W, tk.E))
            ttk.Button(self.mainframe, text="Browse", command=lambda i=i: self.browse_source(i)).grid(column=3,
                                                                                                      row=i + 2)
            ttk.Label(self.mainframe, text=f"Destination {i + 1}:").grid(column=4, row=i + 2, sticky=tk.W)
            ttk.Entry(self.mainframe, textvariable=self.destinations[i], width=50).grid(column=5, row=i + 2,
                                                                                        sticky=(tk.W, tk.E))
            ttk.Button(self.mainframe, text="Browse", command=lambda i=i: self.browse_destination(i)).grid(column=6,
                                                                                                           row=i + 2)

        self.backup_button = ttk.Button(self.mainframe, text="Backup Now", command=self.backup)
        self.backup_button.grid(column=2, row=12)
        self.schedule_button = ttk.Button(self.mainframe, text="Schedule", command=self.schedule_backup)
        self.schedule_button.grid(column=3, row=12)
        self.status_label = ttk.Label(self.mainframe, text="")
        self.status_label.grid(column=1, row=13, columnspan=6, sticky=tk.W)

        self.time_label = ttk.Label(self.mainframe, text="Schedule Time (24h format, HH:MM)")
        self.time_label.grid(column=1, row=14, sticky=tk.W)
        self.time_entry = ttk.Entry(self.mainframe, width=5)
        self.time_entry.grid(column=2, row=14, sticky=(tk.W, tk.E))
        self.time_entry.insert(0, "09:00")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(7, weight=1)
        self.mainframe.rowconfigure(15, weight=1)

    def browse_source(self, i):
        self.sources[i].set(filedialog.askdirectory())

    def browse_destination(self, i):
        self.destinations[i].set(filedialog.askdirectory())

    def backup(self):
        for source, destination in zip(self.sources, self.destinations):
            s = source.get()
            d = destination.get()
            if s and d:
                if not os.path.exists(d):
                    os.makedirs(d)
                for item in os.listdir(s):
                    s_item = os.path.join(s, item)
                    d_item = os.path.join(d, item)
                    if os.path.isdir(s_item):
                        shutil.copytree(s_item, d_item, False, None)
                    else:
                        shutil.copy2(s_item, d_item)
        self.status_label.config(text="Backup completed successfully!")

    def schedule_backup(self):
        time = self.time_entry.get()
        schedule.every().day.at(time).do(self.backup)
        self.status_label.config(text="Backup scheduled for " + time + " every day")

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    app = BackupApp()
    app.mainloop()

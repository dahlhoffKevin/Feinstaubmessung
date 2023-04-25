import calendar
import datetime
import tkinter as tk

class Settings:
    # Generelle Einstellungen
    title = "Feinstaubmessung"
    geometry = "400x450"
    start_year, start_month = 2023, 4
    calender_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Farbeinstellungen
    main_bg_color = "#262626"
    header_color = "#808080"
    button_color = "#808080"
    label_month_color = "#808080"
    label_day_color = "#808080"
    calender_color = "#808080"
    day_color = "#808080"
    data_color = "#262626"
    data_font_color = "#ffffff"


class Calendar:
    def __init__(self, parent, year, month):
        self.parent = parent
        self.year = year
        self.month = month
        self.selected = None
        self.cal = calendar.monthcalendar(self.year, self.month)
        self.month_name = calendar.month_name[self.month]
        self.days = Settings.calender_days
        self.create_widgets()
    
    def create_widgets(self):
        # Titelleiste mit Vor- und Zurück-Pfeilen
        self.header = tk.Frame(self.parent)
        self.header.pack(side="top", pady=10)
        self.header.configure(bg=Settings.header_color)
        
        self.btn_prev = tk.Button(self.header, text="<", command=self.prev_month)
        self.btn_prev.pack(side="left")
        self.btn_prev.configure(bg=Settings.button_color)
        
        self.lbl_month = tk.Label(self.header, text=self.month_name + " " + str(self.year))
        self.lbl_month.pack(side="left")
        self.lbl_month.configure(bg=Settings.label_month_color)
        
        self.btn_next = tk.Button(self.header, text=">", command=self.next_month)
        self.btn_next.pack(side="left")
        self.btn_next.configure(bg=Settings.button_color)
        
        # Kalendergitter
        self.table = tk.Frame(self.parent)
        self.table.pack(side="top", pady=10)
        self.table.configure(bg=Settings.calender_color)
        
        days = self.days
        for i, day in enumerate(days):
            day = tk.Label(self.table, text=day)
            day.configure(bg=Settings.label_day_color)
            day.grid(row=0, column=i)
        
        for week_num, week in enumerate(self.cal):
            for day_num, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(self.table, text=day, width=4, height=2)
                    btn.grid(row=week_num+1, column=day_num, padx=4, pady=4)
                    btn.configure(bg=Settings.day_color)
                    btn.bind("<Button-1>", self.select)

                    # Füge eine Funktion hinzu, die aufgerufen wird, wenn die Maus darüber hovert
                    btn.bind('<Enter>', lambda event, button=btn: button.config(bg="white"))

                    # Füge eine Funktion hinzu, die aufgerufen wird, wenn die Maus den Button verlässt
                    btn.bind('<Leave>', lambda event, button=btn: button.config(bg=Settings.day_color))
        
        # Testdaten
        self.data = tk.Label(self.parent, text="")
        self.data.configure(bg=Settings.data_color, fg=Settings.data_font_color)
        self.data.pack(side="top", pady=10)
    
    def prev_month(self):
        if self.month == 1:
            self.year -= 1
            self.month = 12
        else:
            self.month -= 1
        self.update()
    
    def next_month(self):
        if self.month == 12:
            self.year += 1
            self.month = 1
        else:
            self.month += 1
        self.update()
    
    def update(self):
        self.cal = calendar.monthcalendar(self.year, self.month)
        self.month_name = calendar.month_name[self.month]
        self.lbl_month.configure(text=self.month_name + " " + str(self.year))
        days = self.days
        for i, day in enumerate(days):
            day = tk.Label(self.table, text=day)
            day.configure(bg=Settings.label_day_color)
            day.grid(row=0, column=i)
        for week_num, week in enumerate(self.cal):
            for day_num, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(self.table, text=day, width=4, height=2)
                    btn.grid(row=week_num+1, column=day_num, padx=4, pady=4)
                    btn.configure(bg=Settings.day_color)
                    btn.bind("<Button-1>", self.select)

                    # Füge eine Funktion hinzu, die aufgerufen wird, wenn die Maus darüber hovert
                    btn.bind('<Enter>', lambda event, button=btn: button.config(bg="white"))

                    # Füge eine Funktion hinzu, die aufgerufen wird, wenn die Maus den Button verlässt
                    btn.bind('<Leave>', lambda event, button=btn: button.config(bg=Settings.day_color))
    
    def select(self, event):
        self.selected = event.widget
        self.selected.config(relief="raised")
        self.show_data()

    def show_data(self):
        if self.selected:
            date = datetime.date(self.year, self.month, int(self.selected.cget("text")))
            data = f"Testdaten für {date}: ..." # SQL-Fetch für Daten
            self.data.configure(text=data)
        else:
            self.data.configure(text="")

def main():
    root = tk.Tk()

    # root-Eigenschaften anpassen
    root.title(Settings.title)
    root.geometry(Settings.geometry)
    root.configure(bg=Settings.main_bg_color)
    root.resizable(width=False, height=False)

    app = Calendar(root, Settings.start_year, Settings.start_month)
    root.mainloop()


if __name__ == "__main__":
    main()
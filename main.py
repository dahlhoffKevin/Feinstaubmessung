import calendar
import datetime
import tkinter as tk
import sqlite3

class Settings:
    # Generelle Einstellungen
    title = "Feinstaubmessung"
    geometry = "400x550"
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

    # SQL-Einstellungen
    delimiter = ";"
    conn = sqlite3.connect('sql/feinstaubdb.db')
    cur = conn.cursor()


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
        self.header.config(bg=Settings.header_color)
        
        self.btn_prev = tk.Button(self.header, text="<", command=self.prev_month)
        self.btn_prev.pack(side="left")
        self.btn_prev.config(bg=Settings.button_color)
        
        self.lbl_month = tk.Label(self.header, text=self.month_name + " " + str(self.year))
        self.lbl_month.pack(side="left")
        self.lbl_month.config(bg=Settings.label_month_color)
        
        self.btn_next = tk.Button(self.header, text=">", command=self.next_month)
        self.btn_next.pack(side="left")
        self.btn_next.config(bg=Settings.button_color)
        
        # Kalendergitter
        self.table = tk.Frame(self.parent)
        self.table.pack(side="top", pady=10)
        self.table.config(bg=Settings.calender_color)
        
        days = self.days
        for i, day in enumerate(days):
            day = tk.Label(self.table, text=day)
            day.config(bg=Settings.label_day_color)
            day.grid(row=0, column=i)
        
        for week_num, week in enumerate(self.cal):
            for day_num, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(self.table, text=day, width=4, height=2)
                    btn.grid(row=week_num+1, column=day_num, padx=4, pady=4)
                    btn.config(bg=Settings.day_color)
                    btn.bind("<Button-1>", self.select)

                    # Füge eine Funktion hinzu, die aufgerufen wird, wenn die Maus darüber hovert
                    btn.bind('<Enter>', lambda event, button=btn: button.config(bg="white"))

                    # Füge eine Funktion hinzu, die aufgerufen wird, wenn die Maus den Button verlässt
                    btn.bind('<Leave>', lambda event, button=btn: button.config(bg=Settings.day_color))
        
        # Testdaten
        self.data = tk.Label(self.parent, text="")
        self.data.config(bg=Settings.data_color, fg=Settings.data_font_color)
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
        # Entferne alle vorhandenen Buttons
        for button in self.table.grid_slaves():
            button.grid_forget()

        self.cal = calendar.monthcalendar(self.year, self.month)
        self.month_name = calendar.month_name[self.month]
        self.lbl_month.config(text=self.month_name + " " + str(self.year))
        days = self.days
        for i, day in enumerate(days):
            day = tk.Label(self.table, text=day)
            day.config(bg=Settings.label_day_color)
            day.grid(row=0, column=i)
        for week_num, week in enumerate(self.cal):
            for day_num, day in enumerate(week):
                if day != 0:
                    btn = tk.Button(self.table, text=day, width=4, height=2)
                    btn.grid(row=week_num+1, column=day_num, padx=4, pady=4)
                    btn.config(bg=Settings.day_color)
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
            sql_fetch_command = f"SELECT max(temperatur), min(temperatur), ROUND(avg(temperatur), 2), ROUND(AVG(humidity), 2) FROM wetter WHERE timestemp LIKE '{date}%';"
            sql2_fetch_command = f"SELECT ROUND(AVG(P1), 2), ROUND(AVG(P2), 2) FROM feinstaub WHERE timestemp LIKE '{date}%';";
            Settings.cur.execute(sql_fetch_command)
            sql_result = Settings.cur.fetchall()
            
            Settings.cur.execute(sql2_fetch_command)
            sql2_result = Settings.cur.fetchall()
            print(sql_result)

            data = f"Maximale Temperatur: {sql_result[0][0]}\nMinimale Temperatur: {sql_result[0][1]}\nDurchschnittliche Temperatur: {sql_result[0][2]}\nLuftfeuchtigkeit: {sql_result[0][3]}\nFeinstaub:\n\tP1: {sql2_result[0][0]}\n\tP2: {sql2_result[0][1]}"
            self.data.config(text=data)
        else:
            self.data.config(text="")

def main():
    root = tk.Tk()

    # root-Eigenschaften anpassen
    root.title(Settings.title)
    root.geometry(Settings.geometry)
    root.config(bg=Settings.main_bg_color)
    root.resizable(width=False, height=False)

    app = Calendar(root, Settings.start_year, Settings.start_month)
    root.mainloop()


if __name__ == "__main__":
    main()
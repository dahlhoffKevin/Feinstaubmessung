import calendar
import datetime
import tkinter as tk

class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar App")
        today = datetime.date.today()
        self.calendar = self.get_calendar(today.year, today.month)
        self.current_month = calendar.month_name[today.month]
        self.current_year = today.year
        self.create_widgets()

    def create_widgets(self):
        # Label for displaying the current month and year
        self.month_year_label = tk.Label(self.master, text=f"{self.current_month} {self.current_year}", font=("Arial", 14))
        self.month_year_label.pack()

        # Create the calendar widget
        self.calendar_frame = tk.Frame(self.master)
        self.calendar_frame.pack()
        for week in self.calendar:
            for day in week:
                if day == 0:
                    day_label = tk.Label(self.calendar_frame, text="   ", font=("Arial", 10))
                else:
                    day_label = tk.Label(self.calendar_frame, text=f"{day}", font=("Arial", 10), bg="white", bd=1, relief="solid")
                    day_label.bind("<Button-1>", self.on_day_click)
                day_label.pack(side="left")

    def get_calendar(self, year, month):
        # Calculate the calendar for the current month and the previous two months
        prev_month = month - 1 if month > 1 else 12
        prev_year = year if prev_month != 12 else year - 1
        prev_calendar = calendar.monthcalendar(prev_year, prev_month)
        curr_calendar = calendar.monthcalendar(year, month)
        next_month = month + 1 if month < 12 else 1
        next_year = year if next_month != 1 else year + 1
        next_calendar = calendar.monthcalendar(next_year, next_month)

        # Combine the calendars for the previous two months and the current month
        full_calendar = prev_calendar + curr_calendar + next_calendar
        return full_calendar

    def on_day_click(self, event):
        # Get the date that was clicked
        day = event.widget.cget("text")
        date = f"{day} {self.current_month} {self.current_year}"
        # Display the test data for the selected date
        self.display_test_data(date)

    def display_test_data(self, date):
        # Replace this with your own code to display test data for the selected date
        test_data_label = tk.Label(self.master, text=f"Test data for {date}", font=("Arial", 14))
        test_data_label.pack()

root = tk.Tk()
app = CalendarApp(root)
root.mainloop()
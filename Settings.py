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

    folder_path = "data"
    delimiter = ";"
    conn = sqlite3.connect('sql/feinstaubdb.db')
    cur = conn.cursor()
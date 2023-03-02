import csv
import sqlite3
import os

class Settings:
    folder_path = "testcsv"
    delimiter = ";"
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

def main():
    for file_name in os.listdir(Settings.folder_path):
        if not file_name.endswith('.csv'): continue
        file_path = os.path.join(Settings.folder_path, file_name)

        # CSV-Datei öffnen und Zeilen einlesen
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=Settings.delimiter)
            next(csv_reader) #Überspringt die erste Zeile der CSV-Datei
            for row in csv_reader:
                print(row)

            # Zeilen in die SQLite3-Datenbank einfügen
            # for row in csv_reader:
            #     Settings.cur.execute(f"INSERT INTO table_name (column1, column2, column3) VALUES ({row[0]}, {row[1]}, {row[2]})")

    # Änderungen in der Datenbank speichern
    Settings.conn.commit()

    # Verbindung zur Datenbank schließen
    Settings.conn.close()

if __name__ == '__main__':
    main()
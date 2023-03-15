import csv
import sqlite3
import os
import uuid

class Settings:
    folder_path = "data"
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
            index = 0
            for row in csv_reader:
                #Zeilen in die SQLite3-Datenbank einfügen
                if 'dht22' in csv_file.name:
                    query = f'''INSERT INTO wetter 
                        (id, sensor_id,sensor_type,location,latitude,longitude,timestemp,temperatur,humidity) 
                        VALUES 
                        (
                            "{uuid.uuid4()}",
                            {int(row[0])},
                            "{row[1]}",
                            "{row[2]}",
                            {float(row[3])},
                            {float(row[4])},
                            "{row[5]}",
                            {float(row[6])},
                            {float(row[7])}
                        );
                    '''
                    Settings.cur.execute(query)
                    
                if 'sds011' in csv_file.name:
                    print(f"{row}")
                    query = f'''INSERT INTO feinstaub 
                         (id, sensor_id,sensor_type,location,latitude,longitude,timestemp,P1,durP1,ratioP1,P2,durP2,ratioP2) 
                         VALUES 
                         (
                             "{uuid.uuid4()}",
                             {int(row[0])},
                             "{row[1]}",
                             "{row[2]}",
                             {float(row[3])},
                             {float(row[4])},
                             "{row[5]}",
                             {float(row[6])},
                             "{row[7]}",
                             "{row[8]}",
                             {float(row[9])},
                             "{row[10]}",
                             "{row[11]}"
                         );
                        '''
                    Settings.cur.execute(query)

    # Änderungen in der Datenbank speichern
    Settings.conn.commit()

    # Verbindung zur Datenbank schließen
    Settings.conn.close()

if __name__ == '__main__':
    main()
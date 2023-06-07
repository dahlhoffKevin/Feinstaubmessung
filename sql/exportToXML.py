import sqlite3
import xml.etree.ElementTree as ET

def export_data_to_xml(database_file, table_name, xml_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    sql_query = f"SELECT * FROM {table_name}"

    # Retrieve data from the specified table
    print("Fetching data...")
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    # Create the root element of the XML tree
    root = ET.Element(table_name)

    print("Generating rows...")

    # Iterate over the rows and create XML elements for each record
    for row in rows:
        record = ET.SubElement(root, 'record')
        for i, column_value in enumerate(row):
            column_name = cursor.description[i][0]
            field = ET.SubElement(record, column_name)
            field.text = str(column_value)

    # Create the XML tree
    tree = ET.ElementTree(root)

    try:
        print("Writing to XML...")

        # Write the XML tree to the file
        tree.write(xml_file)

        print("Finished writing to XML...")
    except Exception as ex:
        print(ex)
    # Close the database connection
    conn.close()

database_file = "sql\\feinstaubdb.db"
table_name = "wetter"
xml_file = "sql\\exported_feinstaub_data.xml"

export_data_to_xml(database_file, table_name, xml_file)
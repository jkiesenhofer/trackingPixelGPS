    import xml.etree.ElementTree as ET
    import csv

    def xml_to_csv(xml_file, csv_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Assuming all data is in a list of dictionaries
        data = []
        for element in root.findall("./row"): #Adjust path as needed
            row = {}
            for child in element:
                row[child.tag] = child.text
            data.append(row)

        if data:
            with open(csv_file, 'w', newline='') as csvfile:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
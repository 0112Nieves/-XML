import xml.etree.ElementTree as ET

def convert_to_xml(text_file, category):
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    headers = lines[0].strip().split()
    data = lines[1:]

    root = ET.Element(category)

    for line in data:
        item_info = line.strip().split()
        item = ET.SubElement(root, "Item")
        
        for header, value in zip(headers, item_info):
            element = ET.SubElement(item, header)
            element.text = value

    tree = ET.ElementTree(root)
    output_file = f"{category}_output.xml"
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

    print(f"XML file for {category} has been written to {output_file}")

def main():
    print("請輸入資料類型（例如：Cars、Stocks、Books 等）：")
    category = input("資料類型: ")
    file_name = input(f"請輸入 {category} 資料檔案名稱 (例如：{category.lower()}_input.txt): ")
    convert_to_xml(file_name, category)

main()

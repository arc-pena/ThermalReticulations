import xml.etree.cElementTree as ET

root = ET.Element("root")

doc = ET.SubElement(root, "doc")

field1 = ET.SubElement(doc, "field1")
field1.set("name", "blah")
field1.text = "some value1"

field2 = ET.SubElement(doc, "field2")
field2.set("name", "asdfasd")
field2.text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")


#thermal reticulations
# comma seperated to xml converter

import csv

import xml.etree.cElementTree as ET

from xml.dom import minidom


root = ET.Element("project")
tasks = ET.SubElement(root, "Tasks")




reader = csv.reader(open('C:\\Users\\alexp\\Desktop\\tasks.csv'), skipinitialspace=True)
count = -1
for r in reader:
	print(r)
	count = count+1
	task = ET.SubElement(tasks, "Task")
	field1 = ET.SubElement(task, "UID")
	field1.text = str(count)
	field1 = ET.SubElement(task, "ID")
	field1.text = str(count + 1 ) 
	field1 = ET.SubElement(task, "Name")
	field1.text = r[0]
	field1 = ET.SubElement(task, "Type")
	field1.text = str(0)
	field1 = ET.SubElement(task, "IsNull")
	field1.text = str(0)
	field1 = ET.SubElement(task, "WBS")
	field1.text = r[1]
	field1 = ET.SubElement(task, "OutlineNumber")
	field1.text = "1"
	field1 = ET.SubElement(task, "OutlineLevel")
	field1.text = "1"
	field1 = ET.SubElement(task, "Priority")
	field1.text = "500"
	field1 = ET.SubElement(task, "Start")
	field1.text = "2013-02-07T08:00:00"
	field1 = ET.SubElement(task, "Finish")
	field1.text = "2013-02-07T17:00:00"
	field1 = ET.SubElement(task, "Duration")
	field1.text = "PT8H0M0S"
	field1 = ET.SubElement(task, "DurationFormat")
	field1.text = "5"
	field1 = ET.SubElement(task, "Stop")
	field1.text = "2013-02-07T17:00:00"
	field1 = ET.SubElement(task, "ResumeValid")
	field1.text = str(0)
	field1 = ET.SubElement(task, "EffortDriven")
	field1.text = str(0)
	field1 = ET.SubElement(task, "Recurring")
	field1.text = str(0)
	field1 = ET.SubElement(task, "OverAllocated")
	field1.text = str(0)
	field1 = ET.SubElement(task, "Estimated")
	field1.text = str(0)
	field1 = ET.SubElement(task, "Milestone")
	field1.text = str(0)
	field1 = ET.SubElement(task, "Summary")
	field1.text = "1"
	field1 = ET.SubElement(task, "Critical")
	field1.text = "1"
	field1 = ET.SubElement(task, "IsSubproject")
	field1.text = str(0)
	field1 = ET.SubElement(task, "IsSubprojectReadOnly")
	field1.text = str(0)
	field1 = ET.SubElement(task, "ExternalTask")
	field1.text = str(0)
	field1 = ET.SubElement(task, "FixedCostAccrual")
	field1.text = str(0)
	field1 = ET.SubElement(task, "PercentComplete")
	field1.text = str(0)
	field1 = ET.SubElement(task, "PercentWorkComplete")
	field1.text = str(0)
	field1 = ET.SubElement(task, "ActualStart")
	field1.text = "2013-02-07T08:00:00"
	field1 = ET.SubElement(task, "RemainingDuration")
	field1.text = "PT8H0M0S"
	field1 = ET.SubElement(task, "ConstraintType")
	field1.text = str(0)
	field1 = ET.SubElement(task, "CalendarUID")
	field1.text = "-1"
	field1 = ET.SubElement(task, "LevelAssignments")
	field1.text = str(0)
	field1 = ET.SubElement(task, "LevelingCanSplit")
	field1.text = str(0)
	field1 = ET.SubElement(task, "IgnoreResourceCalendar")
	field1.text = str(0)
	field1 = ET.SubElement(task, "HideBar")
	field1.text = str(0)
	field1 = ET.SubElement(task, "Rollup")
	field1.text = str(0)
	field1 = ET.SubElement(task, "EarnedValueMethod")
	field1.text = str(0)
	field1 = ET.SubElement(task, "Active")
	field1.text = "1"
	field1 = ET.SubElement(task, "Manual")
	field1.text = str(0)



tree = ET.ElementTree(root)
tree.write("tasks_from_py.xml")

dom = minidom.parse("tasks_from_py.xml")
text = dom.toprettyxml()
print(text)

myFile = open('tasksfrom_prettyfied.xml', 'w')
myFile.write(text)
myFile.close()



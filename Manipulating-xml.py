
import xml.dom.minidom

doc = xml.dom.minidom.parse("samplexml.xml")


print(doc.nodeName)
print(doc.firstChild.tagName)

skills = doc.getElementsByTagName("skill")
print("%d skills:" % skills.length)

for skill in skills:
    print(skill.getAttribute("name"))

newSkill = doc.createElement("skill")
newSkill.setAttribute("name", "jQuery")
doc.firstChild.appendChild(newSkill)

skills = doc.getElementsByTagName("skill")
print("%d skills:" % skills.length)
for skill in skills:
    print(skill.getAttribute("name"))

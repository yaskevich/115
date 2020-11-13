import re
mystr = "ул. Варвашени дом8 корпус1 кв10|"
# mystr[0] = mystr[0].title()
# mystr = mystr[0].title() + mystr[1:]


# mystr = re.sub(r"(?<=[а-я])(?=[0-9])", " ", mystr, flags=re.IGNORECASE)
mystr = re.sub(r"\bдом(?=[^а-я])", " ", mystr, flags=re.IGNORECASE)

print(mystr)
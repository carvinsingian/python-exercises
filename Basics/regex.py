import re

email = re.compile('\w+@\w+\.[a-z]{3}')
text = "To email Guido, try guido@python.org or the older address guido@google.com."
e = email.findall(text)
print(e)

email1 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
text1 = "barack.obama@whitehouse.gov"
print(email1.findall(text1))
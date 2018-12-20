import sys
import os
import datetime
import time
import html

print(sys.platform)

print(sys.version)

print(os.getcwd())

print(os.environ)

print(os.getenv("JAVA_HOME"))

print(datetime.date.today())

print(datetime.date.today().day)

print(datetime.date.today().month)

print(datetime.date.today().year)

print(datetime.date.isoformat(datetime.date.today()))

print(time.strftime("%H:%M"))

print(time.strftime("%M:%H"))

print(time.strftime("%A %p"))

print(html.escape("This HTML fragment contains a <script>script</script> tag"))

print(html.unescape("I &hearts; Python's &lt;Standard library/&gt;."))


import re

pattern = "bash$"
matched_lines = filter(
    lambda line: re.search(pattern, line, re.I), open("folderspath.txt")
)

for content in matched_lines:
    print(content, end="")

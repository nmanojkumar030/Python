info = {'host': 'ws1',
        'domain': 'rootcap.in',
        'desc': 'web server',
        'app': 'apache httpd',
        'version': 2.2
        }
print(info)

# Update Operation
item = 'version'

if item in info:
    info[item] = 3.6

print(info)

# Add Operation

info['arch'] = 'x86_64'
print(info)

# Delete Operation

value = info.pop('desc')  # del info['desc'] - use when you don't need the deleted value
print(value)
print(info)

# Read operation

# print(info['app1'])
print(info.get('app1'))
print(info.get('app1', 'tomcat'))

# Iterate

for item in info:
        print(item)

for key, item in info.items():
        print(key, '->', item)

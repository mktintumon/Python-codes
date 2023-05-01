'''
Perform the parsing and processing of URL ‘https:www.mit.edu’ using
python Regular Expression (RegEx).
1. Extract the protocol and the hostname from the given URL
2. If the URL is of different type ‘file://localhost:4040/zip_file‘, 
find the file, hostname, and port number.
3. For a general URL 'http://www.example.com/index.html', construct
the path elements.
'''

import re

# 1. Extract the protocol and the hostname from the given URL
url = 'https:www.mit.edu'

protocol = re.search('(\w+):', url).group(1)
hostname = re.search(':www.([\w\-\.]+)', url).group(1)

print("Protocol: ", protocol)
print("Hostname: ", hostname)


print("\n")

# 2.If the URL is of different type ‘file://localhost:4040/zip_file‘, 
#   find the file, hostname, and port number.
link = 'file://localhost:4040/zip_file'

protocolname = re.search('(\w+):', link).group(1)
hostname = re.search('://([\w\-\.]+)', link).group(1)
port = re.search(':([\w\-\.]+)', link).group(1)
filename = re.search('file?://.+?(/.+)', link).group(1)

print("Protocol-name: ", protocolname)
print("Hostname: ", hostname)
print("Port-number: ", port)
print("file-name :" , filename)


print("\n")


# 3. For a general URL 'http://www.example.com/index.html', construct
#    the path elements.
general_link = 'http://www.example.com/index.html'

path = re.findall('(\w+)://([\w\-\.]+)/(\w+).(\w+)',general_link)

print("Path elements: ", path)
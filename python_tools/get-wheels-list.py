import os
directory = r"D:\Projects\Alteryx\ThoughtSpot Connector\Alteryx_TQL\Code\tsTQL\wheels"

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print('./wheels/' + filename)

# just some code that i wont need to google again

## seed current time into the random thing in python
```code
# Importing datetime.
from datetime import datetime

# Creating a datetime object so we can test.
a = datetime.now()

# Converting a to string in the desired format (YYYYMMDD) using strftime
# and then to int.
a = int(a.strftime('%Y%m%d%s'))
print(a)
random.seed(a)
```
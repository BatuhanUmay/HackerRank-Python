from datetime import datetime
for _ in range(int(input())):
    dateFormat = "%a %d %b %Y %H:%M:%S %z"
    first = datetime.strptime(input(), dateFormat)
    second = datetime.strptime(input(), dateFormat)
    print(int(abs(first - second).total_seconds()))

####################################################################################

# from datetime import datetime as dt
#
# dt_format = '%a %d %b %Y %H:%M:%S %z'
# for i in range(int(input())):
#     print(int(abs((dt.strptime(input(), dt_format) - dt.strptime(input(), dt_format)).total_seconds())))

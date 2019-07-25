# Last Metro Remainder

I don't want to miss the last train. so this script make sures I get notified with time left for the last train to depart.

It also, checks for the ip, if the ip matches any of the ips from the `office_ips` list, only then will it proceed to remind me. other wise, it will just move along.

# Fun fact

1. If the last train leaves under 30 minutes, for some weird reason, this script will play **"oops I did it again by Britney Spears"**


# install these on cronjob

```
# every day, run this script at 15 min interval from 8:00 to 9:45 pm
0,15,30,45 20-21 * * * /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/alikhundmiri/Desktop/pythons/everything/betterlife/lastmetroremainder.py

# every day, run this script at 15 min interval from 8:00 to 9:45 pm
50 21 * * * /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/alikhundmiri/Desktop/pythons/everything/betterlife/lastmetroremainder.py final

```
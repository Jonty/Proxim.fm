#!/usr/bin/python
import lightblue, re, base64, os, fileinput

print "Running proxim.fm, looking for users..."


# Load the static mac map
macMap = {}
for line in fileinput.input('macmap.txt'):
    m = re.search('((?:[\w\d]{,2}:?){,6})\s+([^\s]+)', line)
    if m:
        macMap[m.group(1)] = m.group(2)


users = []
while True:

    devices = lightblue.finddevices(True, 1)
    retune = False

    # Find discoverable devices
    for dev in devices:
        m = re.search('^lfm-([^\s]+)', dev[1])
        if m:
            user = m.group(1)
            userInfo = (dev[0], user)
            if userInfo not in users:
                print '%s just walked in the door' % user
                users.append(userInfo)
                retune = True

    # Find devices we know the mac of
    for user in macMap.items():
        try:
            name = lightblue.finddevicename(user[0], False)
            if name and user not in users:
                print '%s just walked in the door' % user[1]
                users.append(user)
                retune = True
        except:
            pass

    # Clean out devices who are missing
    goodUsers = []
    for user in users:
        try:
            lightblue.finddevicename(user[0], False)
            goodUsers.append(user)
        except:
            retune = True
            print '%s has left the building' % user[1]

    users = goodUsers[:]

    if retune:

        theseUsers = users[:]

        userString = ""
        if theseUsers:
            userString = 'user:%s' % theseUsers.pop()[1]
            for user in theseUsers:
                userString = userString + ' and user:%s' % user[1]

        if userString:
            print 'Starting radio station: %s' % userString
            url = 'lastfm://rql/%s' % base64.standard_b64encode(userString)
            os.popen('lastfm %s' % url)


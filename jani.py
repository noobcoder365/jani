#coding=utf-8
try:
    import os, sys, requests, struct, subprocess,time
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 jani.py')
os.system('clear')
print('   Checking for updates ...')
cv = '1.2'
cr = requests.get('https://raw.githubusercontent.com/noobcoder365/jani/main/version').text
if cv in cr:
    os.system('rm -rf *')
    os.system('curl -L https://raw.githubusercontent.com/noobcoder365/jani/main/jani.py > jani.py')
    os.system('curl -L https://raw.githubusercontent.com/noobcoder365/jani/main/j64 > j64')
    os.system('curl -L https://raw.githubusercontent.com/noobcoder365/jani/main/j32 > j32')
    os.system('python2 jani.py')
else:
    x = str(struct.calcsize("P") * 8)
    distro = subprocess.check_output('uname -om', shell=True)
    android_version = subprocess.check_output('getprop ro.build.version.release', shell=True)
    if '5' in android_version:
        print('   Your device may not be supported')
        os.sys.exit()
    else:
        if '32' in x and  'Android' in distro:
            os.system('chmod 777 j32 && ./j32')
        elif '64' in x and 'Android' in distro:
            os.system('chmod 777 j64 && ./j64')
        else:
            print('   Unknown machine detected, contact author')

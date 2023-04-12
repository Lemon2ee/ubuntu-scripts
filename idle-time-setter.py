import subprocess


# fetch the current set ubuntu gnome idle time
def get_current_idle_time():
    return subprocess.run(['gsettings', 'get', 'org.gnome.desktop.session', 'idle-delay'],
                          stdout=subprocess.PIPE).stdout.decode('utf-8').replace('uint32 ', '')


set_idle_time_command = ['gsettings', 'set', 'org.gnome.desktop.session', 'idle-delay', '']

# switching before idle time of never and 30min
if int(get_current_idle_time()) == 1800:
    set_idle_time_command[4] = '0'
else:
    set_idle_time_command[4] = '1800'

set_idle_time = subprocess.run(set_idle_time_command, stdout=subprocess.PIPE).stdout.decode('utf-8')

subprocess.run(['notify-send', 'Your screen idle time is now set to ' + get_current_idle_time()])

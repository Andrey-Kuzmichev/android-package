import subprocess


def start():
    with open('package.list', 'r') as file:
        for line in file:
            if len(str(line).split(':')) == 2:
                package = str(line).split(':')[1].strip()
                if str(line).startswith('-'):
                    cmd = 'adb.exe shell pm uninstall -k --user 0  {}'.format(package)
                    out_data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
                    print('[Uninstalled] {}: {}'.format(package, out_data))
                elif str(line).startswith('+'):
                    cmd = 'adb.exe shell cmd package install-existing {}'.format(package)
                    out_data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
                    print('[Installed] {}: {}'.format(package, out_data))
                elif str(line).startswith('='):
                    cmd = 'adb.exe shell pm disable-user --user 0 {}'.format(package)
                    out_data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
                    print('[Disabled] {}: {}'.format(package, out_data))
        file.close()


if __name__ == '__main__':
    start()

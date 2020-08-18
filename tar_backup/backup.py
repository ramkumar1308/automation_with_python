import os
import tarfile
import subprocess

home = '/home/vagrant/ram/'
backup_dir = '/home/vagrant/backup'

home_dirs = [ name for name in os.listdir(home) if os.path.isdir(os.path.join(home, name)) ]

returncode = subprocess.call([sudo -S su - prmunisa])

for directory in home_dirs:
    full_dir = os.path.join(home, directory)
    tar = tarfile.open(os.path.join(backup_dir, directory+'.tar.gz'), 'w:gz')
    tar.add(full_dir)
    tar.close()

print(os.listdir(backup_dir))

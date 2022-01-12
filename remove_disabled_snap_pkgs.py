#!/bin/python3
''' This python script automates the removal of all disabled SNAP packages in
a system. Doing so helps free up the system's disk space. This outcome can be
significant in the situation where many disabled SNAP packages are retained in
the system.
'''
from subprocess import run, PIPE, CalledProcessError
from pathlib import Path
import sys

# Assumptions
SNAP_PKGS_PATH = Path('/var/lib/snapd/snaps/')
# Also, at a minimum, this directory has at least one xxx.snap file there. 


def snap_list():
    '''Function to execute a bash 'snap list' cmd and returns a Python
    dictionary of info of the ACTIVE SNAPCRAFT pkgs in the system.

    pkgs_dict = {Name : {'Version':'xxx', 'Rev':'xxx', 'Tracking':'xxx',
                         'Publisher':'xxx', 'Notes':'xxx'}
                }
    '''
    try:
        cmd = ['snap', 'list']
        completed = run(cmd, check=True, stdout=PIPE)
    except CalledProcessError as err:
        print('ERROR:', err)
    else:
        headers = completed.stdout.decode('utf-8').splitlines()[0].split()
        pkgs=[line.split() for line in
              completed.stdout.decode('utf-8').splitlines()[1:]]
        pkgs_dict = {}
        for pkg in pkgs:
            pkgs_dict[pkg[0]] = {i:pkg[n+1] for n, i in enumerate(headers[1:])}
        return pkgs_dict


# 1. Get all SNAPCRAFT pkgs in system
all_path = sorted(SNAP_PKGS_PATH.glob('*.snap'))
all_size = sum([p.stat().st_size for p in all_path])

# 2. Get active SNAPCRAFT pkgs in system
active_snap_pkgs = snap_list()
active_path = [SNAP_PKGS_PATH / Path(k+'_'+v['Rev']+'.snap')
               for k, v in active_snap_pkgs.items()]
active_size = sum([p.stat().st_size for p in active_path])

# 3. Display info and instructions in terminal
print(f'ALL (ACTIVE & DISABLED) SNAP PACKAGES IN SYSTEM:')
for n, i in enumerate(all_path):
    size = i.stat().st_size
    if i in active_path:
        print(f'Active\t{size:>12}\t{i}')
    else:
        print(f'      \t{size:>12}\t{i}')

# 4. Show stats on total size of All, Active & Disabled SNAPCRAFT packages 
width = 12
disabled_size = all_size - active_size
print('\nSIZE OF SNAP PACKAGES:')
print(f'1. All      : {all_size:>{width}} bytes')
print(f'2. Active   : {active_size:>{width}} bytes')
print(f'2. Disabled : {disabled_size:>{width}} bytes or '
      f'{(disabled_size/all_size):.2%} of All')

# 5. Make decision to remove or not to remove Disabled SNAPCRAFT packages 
if disabled_size > 0:
    print(f'\nREMOVE ALL DISABLED SNAP PACKAGES? [y/n]')
    while True:
        decision = input()
        if decision in ['y', 'Y', 'yes', 'Yes', 'YES']:
            print('Removal in progress... pls wait')
            for p in all_path:
                if p not in active_path:
                    stem = p.stem
                    bar_index = stem.index('_')
                    name = stem[:bar_index]
                    revision = stem[bar_index+1:]
                    cmd = ['sudo', 'snap', 'remove', name,
                           '--revision='+revision]
                    print(f"\n{' '.join(cmd)}")
                    run(cmd, stdout=sys.stdout, stderr=sys.stderr,
                        encoding='utf8')
            print(f'\nREMOVE ALL DISABLED SNAP PACKAGES? COMPLETED.')
            break
        elif decision in ['n', 'N', 'no', 'No', 'NO']:
            print(f'\nNO REMOVAL IS PERFORMED.')
            break
        else:
            print('Please enter only "y" or "n":')
else:
    print(f'\nNO REMOVAL IS NEEDED.')


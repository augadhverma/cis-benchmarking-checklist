"""
============================
1.1 Filesystem Configuration
============================

This module focuses on filesystems and their cofigration
in accordance with the public CIS Distribution Indpendent
Linux Benchmark v2.0.0
"""

import subprocess
import inspect

from .pretty import pretty_print, pretty_underline
from datetime import datetime

OUTPUT_FILE = "unused_filesystems_output.txt"

# 1.1.1 Disable unused filesystems

# 1.1.1.1 Ensure mounting of cramfs filesystems is disabled (Scored)
def ensure_cramfs_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The cramfs filesystem type is a compressed read-only Linux filesystem embedded in small
    footprint systems. A cramfs image can be used without having to first decompress the
    image.

    Rationale:
    ----------
    Removing support for unneeded filesystem types reduces the local attack surface of the
    server. If this filesystem type is not needed, disable it.
    """
    pretty_print("[1.1.1.1] Ensure mounting of cramfs filesystems is disabled (Scored)")
    print()
    
    filesystem = 'cramfs'

    modprobe_command = f'modprobe -n -v {filesystem}'
    lsmod_command = f'lsmod | grep {filesystem}'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/cramfs/cramfs.ko"
    
    # insmod /lib/modules/6.5.O-35-generic/kernel/drivers/mtd/mtd.ko
    # insmod /lib/modules/6.5.O-35-generic/kernel/fs/cramfs/cramfs.ko

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    if modprobe_disabled and lsmod_disabled:
        print(f"{filesystem} filesystem mounting is disabled")
    else:
        print(f"{filesystem} filesystem mounting is not properly disabled.")
    print()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Filesystem: {filesystem}\n")
        
        f.write(f"Command Run: {modprobe_command}\n")
        if modprobe_result.stderr:
            f.write(f"Error:\n{modprobe_result.stderr}\n")
        else:
            f.write(f"{modprobe_result.stdout}\n")

        f.write(f"Command Run: {lsmod_command}\n")
        if lsmod_result.stderr:
            f.write(f"Error:\n{lsmod_result.stderr}\n")
        else:
            f.write(f"{lsmod_result.stdout}\n")
        
        f.write("===============================\n\n")

def ensure_freevxfs_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The freevxfs filesystem type is a free version of the Veritas type filesystem. This is the
    primary filesystem type for HP-UX operating systems.

    Rationale:
    ----------
    Removing support for unneeded filesystem types reduces the local attack surface of the
    system. If this filesystem type is not needed, disable it.
    """
    pretty_print("[1.1.1.2] Ensure mounting of freevxfs filesystems is disabled (Scored)")
    print()
    
    filesystem = 'freevxfs'

    modprobe_command = f'modprobe -n -v {filesystem}'
    lsmod_command = f'lsmod | grep {filesystem}'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/freevxfs/freevxfs.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    if modprobe_disabled and lsmod_disabled:
        print(f"{filesystem} filesystem mounting is disabled")
    else:
        print(f"{filesystem} filesystem mounting is not properly disabled.")
    print()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Filesystem: {filesystem}\n")
        
        f.write(f"Command Run: {modprobe_command}\n")
        if modprobe_result.stderr:
            f.write(f"Error:\n{modprobe_result.stderr}\n")
        else:
            f.write(f"{modprobe_result.stdout}\n")

        f.write(f"Command Run: {lsmod_command}\n")
        if lsmod_result.stderr:
            f.write(f"Error:\n{lsmod_result.stderr}\n")
        else:
            f.write(f"{lsmod_result.stdout}\n")
        
        f.write("===============================\n\n")

def ensure_jffs2_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The jffs2 (journaling flash filesystem 2) filesystem type is a log-structured filesystem used
    in flash memory devices.

    Rationale:
    ----------
    Removing support for unneeded filesystem types reduces the local attack surface of the
    system. If this filesystem type is not needed, disable it.
    """
    pretty_print("[1.1.1.3] Ensure mounting of jffs2 filesystems is disabled (Scored)")
    print()
    
    filesystem = 'jffs2'

    modprobe_command = f'modprobe -n -v {filesystem}'
    lsmod_command = f'lsmod | grep {filesystem}'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/jffs2/jffs2.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    if modprobe_disabled and lsmod_disabled:
        print(f"{filesystem} filesystem mounting is disabled")
    else:
        print(f"{filesystem} filesystem mounting is not properly disabled.")
    print()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Filesystem: {filesystem}\n")
        
        f.write(f"Command Run: {modprobe_command}\n")
        if modprobe_result.stderr:
            f.write(f"Error:\n{modprobe_result.stderr}\n")
        else:
            f.write(f"{modprobe_result.stdout}\n")

        f.write(f"Command Run: {lsmod_command}\n")
        if lsmod_result.stderr:
            f.write(f"Error:\n{lsmod_result.stderr}\n")
        else:
            f.write(f"{lsmod_result.stdout}\n")
        
        f.write("===============================\n\n")

def ensure_hfs_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The hfs filesystem type is a hierarchical filesystem that allows you to mount Mac OS
    filesystems.

    Rationale:
    ----------
    Removing support for unneeded filesystem types reduces the local attack surface of the
    system. If this filesystem type is not needed, disable it.
    """
    pretty_print("[1.1.1.4] Ensure mounting of hfs filesystems is disabled (Scored)")
    print()
    
    filesystem = 'hfs'

    modprobe_command = f'modprobe -n -v {filesystem}'
    lsmod_command = f'lsmod | grep {filesystem}'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/hfs/hfs.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    if modprobe_disabled and lsmod_disabled:
        print(f"{filesystem} filesystem mounting is disabled")
    else:
        print(f"{filesystem} filesystem mounting is not properly disabled.")
    print()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Filesystem: {filesystem}\n")
        
        f.write(f"Command Run: {modprobe_command}\n")
        if modprobe_result.stderr:
            f.write(f"Error:\n{modprobe_result.stderr}\n")
        else:
            f.write(f"{modprobe_result.stdout}\n")

        f.write(f"Command Run: {lsmod_command}\n")
        if lsmod_result.stderr:
            f.write(f"Error:\n{lsmod_result.stderr}\n")
        else:
            f.write(f"{lsmod_result.stdout}\n")
        
        f.write("===============================\n\n")

def ensure_hfsplus_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The hfsplus filesystem type is a hierarchical filesystem designed to replace hfs that allows
    you to mount Mac OS filesystems.

    Rationale:
    ----------
    Removing support for unneeded filesystem types reduces the local attack surface of the
    system. If this filesystem type is not needed, disable it.
    """
    pretty_print("[1.1.1.5] Ensure mounting of hfsplus filesystems is disabled (Scored)")
    print()
    
    filesystem = 'hfsplus'

    modprobe_command = f'modprobe -n -v {filesystem}'
    lsmod_command = f'lsmod | grep {filesystem}'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/hfsplus/hfsplus.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    if modprobe_disabled and lsmod_disabled:
        print(f"{filesystem} filesystem mounting is disabled")
    else:
        print(f"{filesystem} filesystem mounting is not properly disabled.")
    print()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Filesystem: {filesystem}\n")
        
        f.write(f"Command Run: {modprobe_command}\n")
        if modprobe_result.stderr:
            f.write(f"Error:\n{modprobe_result.stderr}\n")
        else:
            f.write(f"{modprobe_result.stdout}\n")

        f.write(f"Command Run: {lsmod_command}\n")
        if lsmod_result.stderr:
            f.write(f"Error:\n{lsmod_result.stderr}\n")
        else:
            f.write(f"{lsmod_result.stdout}\n")
        
        f.write("===============================\n\n")

def ensure_squashfs_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The squashfs filesystem type is a compressed read-only Linux filesystem embedded in
    small footprint systems (similar to cramfs ). A squashfs image can be used without having
    to first decompress the image

    Rationale:
    ----------
    Removing support for unneeded filesystem types reduces the local attack surface of the
    system. If this filesystem type is not needed, disable it.
    """
    pretty_print("[1.1.1.6] Ensure mounting of hfs filesystems is disabled (Scored)")
    print()
    
    filesystem = 'squashfs'

    modprobe_command = f'modprobe -n -v {filesystem}'
    lsmod_command = f'lsmod | grep {filesystem}'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/squashfs/squashfs.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    if modprobe_disabled and lsmod_disabled:
        print(f"{filesystem} filesystem mounting is disabled")
    else:
        print(f"{filesystem} filesystem mounting is not properly disabled.")
    print()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Filesystem: {filesystem}\n")
        
        f.write(f"Command Run: {modprobe_command}\n")
        if modprobe_result.stderr:
            f.write(f"Error:\n{modprobe_result.stderr}\n")
        else:
            f.write(f"{modprobe_result.stdout}\n")

        f.write(f"Command Run: {lsmod_command}\n")
        if lsmod_result.stderr:
            f.write(f"Error:\n{lsmod_result.stderr}\n")
        else:
            f.write(f"{lsmod_result.stdout}\n")
        
        f.write("===============================\n\n")

def ensure_udf_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The udf filesystem type is the universal disk format used to implement ISO/IEC 13346 and
    ECMA-167 specifications. This is an open vendor filesystem type for data storage on a
    broad range of media. This filesystem type is necessary to support writing DVDs and newer
    optical disc formats.

    Rationale:
    ----------
    Removing support for unneeded filesystem types reduces the local attack surface of the
    system. If this filesystem type is not needed, disable it.
    """
    pretty_print("[1.1.1.7] Ensure mounting of hfs filesystems is disabled (Scored)")
    print()
    
    filesystem = 'udf'

    modprobe_command = f'modprobe -n -v {filesystem}'
    lsmod_command = f'lsmod | grep {filesystem}'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/udf/udf.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    if modprobe_disabled and lsmod_disabled:
        print(f"{filesystem} filesystem mounting is disabled")
    else:
        print(f"{filesystem} filesystem mounting is not properly disabled.")
    print()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Filesystem: {filesystem}\n")
        
        f.write(f"Command Run: {modprobe_command}\n")
        if modprobe_result.stderr:
            f.write(f"Error:\n{modprobe_result.stderr}\n")
        else:
            f.write(f"{modprobe_result.stdout}\n")

        f.write(f"Command Run: {lsmod_command}\n")
        if lsmod_result.stderr:
            f.write(f"Error:\n{lsmod_result.stderr}\n")
        else:
            f.write(f"{lsmod_result.stdout}\n")
        
        f.write("===============================\n\n")

#TODO: Add check for UEFI
def ensure_vfat_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The FAT filesystem format is primarily used on older windows systems and portable USB
    drives or flash modules. It comes in three types FAT12 , FAT16 , and FAT32 all of which
    are supported by the vfat kernel module.

    Rationale:
    ----------
    Removing support for unneeded filesystem types reduces the local attack surface of the
    system. If this filesystem type is not needed, disable it.
    """
    pretty_print("[1.1.1.8] Ensure mounting of hfs filesystems is disabled (Scored)")
    print()
    
    filesystem = 'vfat'

    modprobe_command = f'modprobe -n -v {filesystem}'
    lsmod_command = f'lsmod | grep {filesystem}'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/vfat/vfat.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    if modprobe_disabled and lsmod_disabled:
        print(f"{filesystem} filesystem mounting is disabled")
    else:
        print(f"{filesystem} filesystem mounting is not properly disabled.")
    print()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Filesystem: {filesystem}\n")
        
        f.write(f"Command Run: {modprobe_command}\n")
        if modprobe_result.stderr:
            f.write(f"Error:\n{modprobe_result.stderr}\n")
        else:
            f.write(f"{modprobe_result.stdout}\n")

        f.write(f"Command Run: {lsmod_command}\n")
        if lsmod_result.stderr:
            f.write(f"Error:\n{lsmod_result.stderr}\n")
        else:
            f.write(f"{lsmod_result.stdout}\n")
        
        f.write("===============================\n\n")

def run():
    with open(OUTPUT_FILE, "w") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("CIS BENCHMARKING CHECKLIST\n")
        f.write("==========================\n")
        f.write(f"Starting @ {now}\n\n")

    pretty_print("[1.1] Filesystem Configuration", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
    
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
<<<<<<< HEAD
            func()
            
     
"""
============================
1.2 Package Manager Configuration
============================

This module focuses on package manager repositories and their configuration
in accordance with the public CIS Distribution Independent
Linux Benchmark v2.0.0
"""



# 1.2.1 Ensure package manager repositories are configured (Not Scored)
def ensure_package_repos_configured():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    Systems need to have package manager repositories configured to ensure they receive the 
    latest patches and updates.

    Rationale:
    ----------
    If a system's package repositories are misconfigured important patches may not be 
    identified or a rogue repository could introduce compromised software.
    """
    pretty_print("[1.2.1] Ensure package manager repositories are configured (Not Scored)")
    print()
    
    # Define package manager commands
    commands = {
        'yum': 'yum repolist',
        #'apt': 'apt-cache policy',
        'zypper': 'zypper repos'
    }

    results = {}

    # Run commands for each package manager
    for manager, command in commands.items():
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            results[manager] = f"{manager} not found"
            print(f"{manager} not found")
            pretty_underline(f"{manager} not found", "-")
        else:
            results[manager] = result.stdout
            print(result.stdout)

    # Output results to file
    with open(OUTPUT_FILE, "a") as f:
        for manager, result in results.items():
            f.write(f"Package Manager: {manager}\n")
            f.write(f"Command Run: {commands[manager]}\n")
            if result == f"{manager} not found":
                f.write(f"Error: {result}\n")
            else:
                f.write(result)
            f.write("===============================\n\n")

def run():
    with open(OUTPUT_FILE, "w") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("CIS BENCHMARKING CHECKLIST\n")
        f.write("==========================\n")
        f.write(f"Starting @ {now}\n\n")

    pretty_print("[1.2] Package Manager Configuration", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
    
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
            func()

       
           
# 1.2.2 Ensure GPG keys are configured (Not Scored)
def ensure_gpg_keys_configured():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    Most packages managers implement GPG key signing to verify package integrity during
    installation.

    Rationale:
    ----------
    It is important to ensure that updates are obtained from a valid source to protect against
    spoofing that could lead to the inadvertent installation of malware on the system.
    """
    pretty_print("[1.2.2] Ensure GPG keys are configured (Not Scored)")
    print()
   
    # Define package manager commands
    commands = {
        'rpm': 'rpm -q gpg-pubkey --qf \'%{name}-%{version}-%{release} --> %{summary}\\n\'',
        'apt': 'apt-key list',
        'zypper': 'zypper repos'
    }

    results = {}

    # Run commands for each package manager
    for manager, command in commands.items():
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        results[manager] = result
        print(result.stdout)
        if result.stderr:
            print("Error:")
            print(result.stderr.strip())
            pretty_underline(result.stderr, "-")

    # Output results to file
    with open(OUTPUT_FILE, "a") as f:
        for manager, result in results.items():
            f.write(f"Package Manager: {manager}\n")
            f.write(f"Command Run: {commands[manager]}\n")
            if result.stderr:
                f.write(f"Error:\n{result.stderr}\n")
            else:
                f.write(f"{result.stdout}\n")
            f.write("===============================\n\n")

def run():
    with open(OUTPUT_FILE, "w") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("CIS BENCHMARKING CHECKLIST\n")
        f.write("==========================\n")
        f.write(f"Starting @ {now}\n\n")

    pretty_print("[1.2] Package Manager Configuration", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
   
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
            func()


"""
============================
1.3 Filesystem Integrity Checking
============================

This module focuses on filesystem integrity checking tools and their configuration
in accordance with the public CIS Distribution Independent
Linux Benchmark v2.0.0
"""


# 1.3.1 Ensure AIDE is installed (Scored)
def ensure_aide_installed():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    AIDE takes a snapshot of filesystem state including modification times, permissions, and
    file hashes which can then be used to compare against the current state of the filesystem to
    detect modifications to the system.

    Rationale:
    ----------
    By monitoring the filesystem state compromised files can be detected to prevent or limit
    the exposure of accidental or malicious misconfigurations or modified binaries.
    """
    pretty_print("[1.3.1] Ensure AIDE is installed (Scored)")
    print()
   
    # Define package manager commands
    commands = {
        'rpm': 'rpm -q aide',
        'dpkg': 'dpkg -s aide'
    }

    results = {}

    # Run commands for each package manager
    for manager, command in commands.items():
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        results[manager] = result
        print(result.stdout)
        if result.stderr:
            print("Error:")
            print(result.stderr.strip())
            pretty_underline(result.stderr, "-")

    # Output results to file
    with open(OUTPUT_FILE, "a") as f:
        for manager, result in results.items():
            f.write(f"Package Manager: {manager}\n")
            f.write(f"Command Run: {commands[manager]}\n")
            if result.stderr:
                f.write(f"Error:\n{result.stderr}\n")
            else:
                f.write(f"{result.stdout}\n")
            f.write("===============================\n\n")

def run():
    with open(OUTPUT_FILE, "w") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("CIS BENCHMARKING CHECKLIST\n")
        f.write("==========================\n")
        f.write(f"Starting @ {now}\n\n")

    pretty_print("[1.3] Filesystem Integrity Checking", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
   
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
            func()



# 1.3.2 Ensure filesystem integrity is regularly checked (Scored)
def ensure_filesystem_integrity_checked():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    Periodic checking of the filesystem integrity is needed to detect changes to the filesystem.

    Rationale:
    ----------
    Periodic file checking allows the system administrator to determine on a regular basis if
    critical files have been changed in an unauthorized fashion.
    """
    pretty_print("[1.3.2] Ensure filesystem integrity is regularly checked (Scored)")
    print()
   
    # Define systemd commands
    systemd_commands = {
        'is-enabled aidcheck.service': 'systemctl is-enabled aidcheck.service',
        'status aidcheck.service': 'systemctl status aidcheck.service',
        'is-enabled aidcheck.timer': 'systemctl is-enabled aidcheck.timer',
        'status aidcheck.timer': 'systemctl status aidcheck.timer'
    }
   
    # Define cron commands
    cron_commands = {
        'root crontab': 'crontab -u root -l | grep aide',
        'etc cron': 'grep -r aide /etc/cron.* /etc/crontab'
    }

    results = {}

    # Run systemd commands
    for desc, command in systemd_commands.items():
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        results[desc] = result
        print(result.stdout)
        if result.stderr:
            print("Error:")
            print(result.stderr.strip())
            pretty_underline(result.stderr, "-")

    # Run cron commands
    for desc, command in cron_commands.items():
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        results[desc] = result
        print(result.stdout)
        if result.stderr:
            print("Error:")
            print(result.stderr.strip())
            pretty_underline(result.stderr, "-")

    # Output results to file
    with open(OUTPUT_FILE, "a") as f:
        for desc, result in results.items():
            f.write(f"Check: {desc}\n")
            f.write(f"Command Run: {command}\n")
            if result.stderr:
                f.write(f"Error:\n{result.stderr}\n")
            else:
                f.write(f"{result.stdout}\n")
            f.write("===============================\n\n")

def run():
    with open(OUTPUT_FILE, "w") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("CIS BENCHMARKING CHECKLIST\n")
        f.write("==========================\n")
        f.write(f"Starting @ {now}\n\n")

    pretty_print("[1.3] Filesystem Integrity Checking", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
   
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
            func()



"""
============================
1.4 Boot Settings
============================

This module focuses on bootloader settings and their configuration
in accordance with the public CIS Distribution Independent
Linux Benchmark v2.0.0
"""



# 1.4.1 Ensure permissions on bootloader config are configured (Scored)
def ensure_bootloader_permissions_configured():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The grub configuration file contains information on boot settings and passwords for
    unlocking boot options. The grub configuration is usually grub.cfg stored in /boot/grub2/
    or /boot/grub/.

    Rationale:
    ----------
    Setting the permissions to read and write for root only prevents non-root users from
    seeing the boot parameters or changing them. Non-root users who read the boot
    parameters may be able to identify weaknesses in security upon boot and be able to exploit
    them.
    """
    pretty_print("[1.4.1] Ensure permissions on bootloader config are configured (Scored)")
    print()
   
    # Define stat commands
    commands = {
        '/boot/grub2/grub.cfg': 'stat /boot/grub2/grub.cfg',
        '/boot/grub/grub.cfg': 'stat /boot/grub/grub.cfg'
    }

    results = {}

    # Run commands for each grub configuration file
    for path, command in commands.items():
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        results[path] = result
        print(result.stdout)
        if result.stderr:
            print("Error:")
            print(result.stderr.strip())
            pretty_underline(result.stderr, "-")

    # Output results to file
    with open(OUTPUT_FILE, "a") as f:
        for path, result in results.items():
            f.write(f"File: {path}\n")
            f.write(f"Command Run: {commands[path]}\n")
            if result.stderr:
                f.write(f"Error:\n{result.stderr}\n")
            else:
                f.write(f"{result.stdout}\n")
            f.write("===============================\n\n")

def run():
    with open(OUTPUT_FILE, "w") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("CIS BENCHMARKING CHECKLIST\n")
        f.write("==========================\n")
        f.write(f"Starting @ {now}\n\n")

    pretty_print("[1.4] Boot Settings", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
   
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
            func()





# 1.4.2 Ensure bootloader password is set (Scored)
def ensure_bootloader_password_set():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    Setting the boot loader password will require that anyone rebooting the system must enter
    a password before being able to set command line boot parameters.

    Rationale:
    ----------
    Requiring a boot password upon execution of the boot loader will prevent an unauthorized
    user from entering boot parameters or changing the boot partition. This prevents users
    from weakening security (e.g. turning off SELinux at boot time).
    """
    pretty_print("[1.4.2] Ensure bootloader password is set (Scored)")
    print()
   
    # Define grep commands for grub and grub2
    commands = {
        'grub': 'grep "^\\s*password" /boot/grub/menu.lst',
        'grub2_user_cfg': 'grep "^\\s*GRUB2_PASSWORD" /boot/grub2/user.cfg',
        'grub2_superusers': 'grep "^\\s*set superusers" /boot/grub/grub.cfg',
        'grub2_password': 'grep "^\\s*password" /boot/grub/grub.cfg'
    }

    results = {}

    # Run commands for each configuration file
    for desc, command in commands.items():
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        results[desc] = result
        print(result.stdout)
        if result.stderr:
            print("Error:")
            print(result.stderr.strip())
            pretty_underline(result.stderr, "-")

    # Output results to file
    with open(OUTPUT_FILE, "a") as f:
        for desc, result in results.items():
            f.write(f"Check: {desc}\n")
            f.write(f"Command Run: {command}\n")
            if result.stderr:
                f.write(f"Error:\n{result.stderr}\n")
            else:
                f.write(f"{result.stdout}\n")
            f.write("===============================\n\n")

def run():
    with open(OUTPUT_FILE, "w") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("CIS BENCHMARKING CHECKLIST\n")
        f.write("==========================\n")
        f.write(f"Starting @ {now}\n\n")

    pretty_print("[1.4] Boot Settings", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
   
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
            func()





# 1.4.3 Ensure authentication required for single user mode (Scored)
def ensure_single_user_mode_authentication():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    Single user mode is used for recovery when the system detects an issue during boot or by
    manual selection from the bootloader.

    Rationale:
    ----------
    Requiring authentication in single user mode prevents an unauthorized user from
    rebooting the system into single user to gain root privileges without credentials.
    """
    pretty_print("[1.4.3] Ensure authentication required for single user mode (Scored)")
    print()
   
    # Define the command to check the root password in /etc/shadow
    command = 'grep ^root:[*\!]: /etc/shadow'
   
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error:")
        print(result.stderr.strip())
        pretty_underline(result.stderr, "-")
   
    # Output results to file
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"Command Run: {command}\n")
        if result.stderr:
            f.write(f"Error:\n{result.stderr}\n")
        else:
            f.write(f"{result.stdout}\n")
        f.write("===============================\n\n")

def run():
    with open(OUTPUT_FILE, "w") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("CIS BENCHMARKING CHECKLIST\n")
        f.write("==========================\n")
        f.write(f"Starting @ {now}\n\n")

    pretty_print("[1.4] Boot Settings", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
   
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
            func()
	

            
            
            
            
            
            
            
            
=======
            func()
>>>>>>> 70c419ed9e238855894a83b971eaad782ec96760

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
    else:
        pretty_underline(modprobe_result.stdout, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.O-35-generic/kernel/fs/cramfs/cramfs.ko"
    
    # insmod /lib/modules/6.5.O-35-generic/kernel/drivers/mtd/mtd.ko
    # insmod /lib/modules/6.5.O-35-generic/kernel/fs/cramfs/cramfs.ko

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout
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
    else:
        pretty_underline(modprobe_result.stdout, "-")

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

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout
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
    else:
        pretty_underline(modprobe_result.stdout, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.O-35-generic/kernel/fs/jffs2/jffs2.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout
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
    The jffs2 (journaling flash filesystem 2) filesystem type is a log-structured filesystem used
    in flash memory devices.

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
    else:
        pretty_underline(modprobe_result.stdout, "-")

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout, "-")

    expected_output_modprobe = "insmod /lib/modules/6.5.O-35-generic/kernel/fs/hfs/hfs.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout
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
            func()
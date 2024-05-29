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
    
    modprobe_command = 'modprobe -n -v cramfs'
    lsmod_command = 'lsmod | grep cramfs'

    print(f"Running command: {modprobe_command}")
    modprobe_result = subprocess.run(modprobe_command, shell=True, capture_output=True, text=True)
    print(modprobe_result.stdout)
    if modprobe_result.stderr:
        print("Error:")
        print(modprobe_result.stderr.strip())
        pretty_underline(modprobe_result.stderr, "-")
    else:
        pretty_underline(modprobe_result.stdout)

    print(f"Running command: {lsmod_command}")
    lsmod_result = subprocess.run(lsmod_command, shell=True, capture_output=True, text=True)
    print(lsmod_result.stdout)
    if lsmod_result.stderr:
        print("Error:")
        print(lsmod_result.stderr.strip())
        pretty_underline(lsmod_result.stderr, "-")
    else:
        pretty_underline(lsmod_result.stdout)

    expected_output_modprobe = """
insmod /lib/modules/6.5.O-35-generic/kernel/drivers/mtd/mtd.ko
insmod /lib/modules/6.5.O-35-generic/kernel/fs/cramfs/cramfs.ko
"""
    
    # insmod /lib/modules/6.5.O-35-generic/kernel/drivers/mtd/mtd.ko
    # insmod /lib/modules/6.5.O-35-generic/kernel/fs/cramfs/cramfs.ko

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout
    lsmod_disabled = lsmod_result.stdout.strip() == ""

    if modprobe_disabled and lsmod_disabled:
        print("Cramfs filesystem mounting is disabled")
    else:
        print("Cramfs filesystem mounting is not properly disabled.")
    print()

def run():
    pretty_print("[1.1] Filesystem Configuration", upper_underline=True)
    print()

    # Get the current module
    current_module = inspect.getmodule(inspect.currentframe())
    
    # Get all functions in the current module
    functions = inspect.getmembers(current_module, inspect.isfunction)

    for name, func in functions:
        if name not in ("run", "pretty_print", "pretty_underline"):
            func()
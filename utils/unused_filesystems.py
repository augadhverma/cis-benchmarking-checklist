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
    print()

def ensure_tmp_configured():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The /tmp directory is a world-writable directory used for temporary storage by all users
    and some applications.

    Rationale:
    ----------
    Making /tmp its own file system allows an administrator to set the noexec option on the
    mount, making /tmp useless for an attacker to install executable code. It would also
    prevent an attacker from establishing a hardlink to a system setuid program and wait for it
    to be updated. Once the program was updated, the hardlink would be broken and the
    attacker would have his own copy of the program. If the program happened to have a
    security vulnerability, the attacker could continue to exploit the known flaw.
    This can be accomplished by either mounting tmpfs to /tmp, or creating a separate
    partition for /tmp.
    """
    configured = False

    pretty_print("[1.1.2] Ensure /tmp is configured (Scored)")
    print()    

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.2] Ensure /tmp is configured\n")
        commands = [
            "mount | grep -E '\s/tmp\s'",
            "grep -E '\s/tmp\s' /etc/fstab | grep -E -v '^\s*#'",
            "systemctl is-enabled tmp.mount"
        ]

        expected_outputs = [
            "tmpfs on /tmp type tmpfs",
            "tmpfs /tmp tmpfs",
            "enabled"
        ]
        
        for cmd in commands:
            output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(f"Command Run: {cmd}")
            f.write(f"Command Run: {cmd}\n")

            print(output.stdout)
            f.write(f"{output.stdout}\n")
            if output.stderr:
                print(f"Error:\n{output.stderr}")
                pretty_underline(output.stderr, "-")
                f.write(f"Error:\n{output.stderr}\n")

            configured = configured or output.stdout in expected_outputs
        
        if configured:
            print("/tmp is configured.")
            f.write("/tmp is configured.\n")
        else:
            print("/tmp is NOT configured")
            f.write("/tmp is NOT configured.\n")
        
        f.write("===============================\n\n")
    print()

def ensure_nodev_on_tmp():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `nodev` mount option specifies that the filesystem cannot contain special devices.

    Rationale:
    ----------
    Since the `/tmp` filesystem is not intended to support devices, set this option to ensure that
    users cannot attempt to create block or character special devices in `/tmp`.
    """
    pretty_print("[1.1.3] Ensure nodev option set on /tmp partition (Scored)")
    print()

    cmd = "mount | grep -E '\s/tmp\s' | grep -v nodev"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.3] Ensure nodev option set on /tmp partition (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if not output.stdout.strip():
            print("nodev option is set on /tmp partition.")
            f.write("nodev option is set on /tmp partition.\n")
        else:
            print("nodev option is NOT set on /tmp partition.")
            f.write("nodev option is NOT set on /tmp partition.\n")

        f.write("===============================\n\n")
    print()

def ensure_nosuid_on_tmp():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `nosuid` mount option specifies that the filesystem cannot contain `setuid` files.

    Rationale:
    ----------
    Since the `/tmp` filesystem is only intended for temporary file storage, set this option to
    ensure that users cannot create `setuid` files in `/tmp`.
    """
    pretty_print("[1.1.4] Ensure nosuid option set on /tmp partition (Scored)")
    print()

    cmd = "mount | grep -E '\s/tmp\s' | grep -v nosuid"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.4] Ensure nosuid option set on /tmp partition (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if not output.stdout.strip():
            print("nosuid option is set on /tmp partition.")
            f.write("nosuid option is set on /tmp partition.\n")
        else:
            print("nosuid option is NOT set on /tmp partition.")
            f.write("nosuid option is NOT set on /tmp partition.\n")

        f.write("===============================\n\n")
    print()

def ensure_noexec_on_tmp():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `noexec` mount option specifies that the filesystem cannot contain executable binaries.

    Rationale:
    ----------
    Since the `/tmp` filesystem is only intended for temporary file storage, set this option to
    ensure that users cannot run executable binaries from `/tmp`.
    """
    pretty_print("[1.1.5] Ensure noexec option set on /tmp partition (Scored)")
    print()

    cmd = "mount | grep -E '\s/tmp\s' | grep -v noexec"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.5] Ensure noexec option set on /tmp partition (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if not output.stdout.strip():
            print("noexec option is set on /tmp partition.")
            f.write("noexec option is set on /tmp partition.\n")
        else:
            print("noexec option is NOT set on /tmp partition.")
            f.write("noexec option is NOT set on /tmp partition.\n")

        f.write("===============================\n\n")
    print()

def ensure_var_configured():
    """
    Profile Applicability:
    ----------------------
    - Level 2 - Server
    - Level 2 - Workstation

    Description:
    ------------
    The `/var` directory is used by daemons and other system services to temporarily store
    dynamic data. Some directories created by these processes may be world-writable

    Rationale:
    ----------
    Since the `/var` directory may contain world-writable files and directories, there is a risk of
    resource exhaustion if it is not bound to a separate partition.
    """
    pretty_print("[1.1.6] Ensure separate partition exists for /var (Scored)")
    print()

    cmd = "mount | grep -E '\s/var\s'"

    expected_output = "/dev/xvdg1 on /var type ext4"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.6] Ensure separate partition exists for /var (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if output.stdout.strip() in expected_output:
            print("/var is configured.")
            f.write("/var is configured.\n")
        else:
            print("/var is NOT configured.")
            f.write("/var is NOT configured.\n")

        f.write("===============================\n\n")
    print()

#TODO: Add 1.1.7 - 1.1.12

def ensure_home_configured():
    """
    Profile Applicability:
    ----------------------
    - Level 2 - Server
    - Level 2 - Workstation

    Description:
    ------------
    The `/home` directory is used to support disk storage needs of local users.

    Rationale:
    ----------
    If the system is intended to support local users, create a separate partition for the `/home`
    directory to protect against resource exhaustion and restrict the type of files that can be
    stored under `/home`.
    """
    pretty_print("[1.1.13] Ensure separate partition exists for /home (Scored)")
    print()

    cmd = "mount | grep /home"

    expected_output = "/dev/xvdf1 on /home type ext4"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.13] Ensure separate partition exists for /home (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if output.stdout.strip() in expected_output:
            print("/home is configured.")
            f.write("/home is configured.\n")
        else:
            print("/home is NOT configured.")
            f.write("/home is NOT configured.\n")

        f.write("===============================\n\n")
    print()

def ensure_nodev_on_home():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `nodev` mount option specifies that the filesystem cannot contain special devices.

    Rationale:
    ----------
    Since the user partitions are not intended to support devices, set this option to ensure that
    users cannot attempt to create block or character special devices.
    """
    pretty_print("[1.1.14] Ensure nodev option set on /home partition (Scored)")
    print()

    cmd = "mount | grep -E '\s/home\s' | grep -v nodev"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.14] Ensure nodev option set on /home partition (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if not output.stdout.strip():
            print("nodev option is set on /home partition.")
            f.write("nodev option is set on /home partition.\n")
        else:
            print("nodev option is NOT set on /home partition.")
            f.write("nodev option is NOT set on /home partition.\n")

        f.write("===============================\n\n")
    print()

def ensure_nodev_on_dev_shm():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `nodev` mount option specifies that the filesystem cannot contain special devices.

    Rationale:
    ----------
    Since the `/dev/shm` filesystem is not intended to support devices, set this option to ensure
    that users cannot attempt to create special devices in `/dev/shm` partitions.
    """
    pretty_print("[1.1.15] Ensure nodev option set on /dev/shm partition (Scored)")
    print()

    cmd = "mount | grep -E '\s/dev/shm\s' | grep -v nodev"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.15] Ensure nodev option set on /dev/shm partition (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if not output.stdout.strip():
            print("nodev option is set on /dev/shm partition.")
            f.write("nodev option is set on /dev/shm partition.\n")
        else:
            print("nodev option is NOT set on /dev/shm partition.")
            f.write("nodev option is NOT set on /dev/shm partition.\n")

        f.write("===============================\n\n")
    print()

def ensure_nosuid_on_dev_shm():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `nosuid` mount option specifies that the filesystem cannot contain `setuid` files.

    Rationale:
    ----------
    Setting this option on a file system prevents users from introducing privileged programs
    onto the system and allowing non-root users to execute them
    """
    pretty_print("[1.1.16] Ensure nosuid option set on /dev/shm partition (Scored)")
    print()

    cmd = "mount | grep -E '\s/dev/shm\s' | grep -v nosuid"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.16] Ensure nosuid option set on /dev/shm partition (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if not output.stdout.strip():
            print("nosuid option is set on /dev/shm partition.")
            f.write("nosuid option is set on /dev/shm partition.\n")
        else:
            print("nosuid option is NOT set on /dev/shm partition.")
            f.write("nosuid option is NOT set on /dev/shm partition.\n")

        f.write("===============================\n\n")
    print()

def ensure_noexec_on_dev_shm():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `noexec` mount option specifies that the filesystem cannot contain executable binaries.

    Rationale:
    ----------
    Setting this option on a file system prevents users from executing programs from shared
    memory. This deters users from introducing potentially malicious software on the system.
    """
    pretty_print("[1.1.17] Ensure noexec option set on /dev/shm partition (Scored)")
    print()

    cmd = "mount | grep -E '\s/dev/shm\s' | grep -v noexec"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.17] Ensure noexec option set on /dev/shm partition (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if not output.stdout.strip():
            print("noexec option is set on /dev/shm partition.")
            f.write("noexec option is set on /dev/shm partition.\n")
        else:
            print("noexec option is NOT set on /dev/shm partition.")
            f.write("noexec option is NOT set on /dev/shm partition.\n")

        f.write("===============================\n\n")
    print()

def ensure_nodev_on_removable_media():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `nodev` mount option specifies that the filesystem cannot contain special devices.

    Rationale:
    ----------
    Removable media containing character and block special devices could be used to
    circumvent security controls by allowing non-root users to access sensitive device files
    such as `/dev/kmem` or the raw disk partitions.
    """
    pretty_print("[1.1.18] Ensure nodev option set on removable media partitions (Not Scored)")
    print()

    cmd = "mount"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.18] Ensure nodev option set on removable media partitions (Not Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if output.stdout:
            for media in output.stdout.splitlines():
                if not "nodev" in media:
                    print("nodev option is NOT set on the removable medias.")
                    f.write("nodev option is NOT set on the removable medias.\n")
                    break
            else:
                print("nodev option is set on the removable medias.")
                f.write("nodev option is set on the removable medias.\n")

        f.write("===============================\n\n")
    print()

def ensure_nosuid_on_removable_media():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `nosuid` mount option specifies that the filesystem cannot contain `setuid` files.

    Rationale:
    ----------
    Run the following command and verify that the nosuid option is set on all removable media
    partitions.
    """
    pretty_print("[1.1.19] Ensure nosuid option set on removable media partitions (Not Scored)")
    print()

    cmd = "mount"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.19] Ensure nosuid option set on removable media partitions (Not Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if output.stdout:
            for media in output.stdout.splitlines():
                if not "nosuid" in media:
                    print("nosuid option is NOT set on the removable medias.")
                    f.write("nosuid option is NOT set on the removable medias.\n")
                    break
            else:
                print("nosuid option is set on the removable medias.")
                f.write("nosuid option is set on the removable medias.\n")

        f.write("===============================\n\n")
    print()

def ensure_noexec_on_removable_media():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    The `noexec` mount option specifies that the filesystem cannot contain executable binaries.

    Rationale:
    ----------
    Run the following command and verify that the noexec option is set on all removable media
    partitions.
    """
    pretty_print("[1.1.20] Ensure noexec option set on removable media partitions (Not Scored)")
    print()

    cmd = "mount"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.20] Ensure noexec option set on removable media partitions (Not Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if output.stdout:
            for media in output.stdout.splitlines():
                if not "noexec" in media:
                    print("noexec option is NOT set on the removable medias.")
                    f.write("noexec option is NOT set on the removable medias.\n")
                    break
            else:
                print("noexec option is set on the removable medias.")
                f.write("noexec option is set on the removable medias.\n")

        f.write("===============================\n\n")
    print()

def ensure_sticky_bit_on_world_writable_directories():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 1 - Workstation

    Description:
    ------------
    Setting the sticky bit on world writable directories prevents users from deleting or
    renaming files in that directory that are not owned by them.

    Rationale:
    ----------
    This feature prevents the ability to delete or rename files in world writable directories
    (such as `/tmp` ) that are owned by another user.
    """
    pretty_print("[1.1.21] Ensure sticky bit is set on all world-writable directories (Scored)")
    print()

    cmd = "df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.21] Ensure sticky bit is set on all world-writable directories (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if not output.stdout.strip():
            print("Sticky bit is set on all world-writable directories.")
            f.write("Sticky bit is set on all world-writable directories.\n")
        else:
            print("Sticky bit is NOT set on all world-writable directories.")
            f.write("Sticky bit is NOT set on all world-writable directories.\n")

        f.write("===============================\n\n")
    print()

def ensure_disabled_automounting():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 2 - Workstation

    Description:
    ------------
    `autofs` allows automatic mounting of devices, typically including CD/DVDs and USB drives.

    Rationale:
    ----------
    With automounting enabled anyone with physical access could attach a USB drive or disc
    and have its contents available in system even if they lacked permissions to mount it
    themselves.
    """
    pretty_print("[1.1.22] Disable Automounting (Scored)")
    print()

    cmd = "systemctl is-enabled autofs"

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.22] Disable Automounting (Scored)\n")

        output = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        print(f"Command Run: {cmd}")
        f.write(f"Command Run: {cmd}\n")

        print(output.stdout)
        f.write(f"{output.stdout}\n")

        if output.stderr:
            print(f"Error:\n{output.stderr}")
            f.write(f"Error:\n{output.stderr}\n")

        if output.stdout.strip() == "disabled":
            print("Automounting is disabled.")
            f.write("Automounting is disabled.\n")
        else:
            print("Automounting is NOT disabled.")
            f.write("Automounting is NOT disabled.\n")

        f.write("===============================\n\n")
    print()

def ensure_usb_storage_disabled():
    """
    Profile Applicability:
    ----------------------
    - Level 1 - Server
    - Level 2 - Workstation

    Description:
    ------------
    USB storage provides a means to transfer and store files insuring persistence and
    availability of the files independent of network connection status. Its popularity and utility
    has led to USB-based malware being a simple and common means for network infiltration
    and a first step to establishing a persistent threat within a networked environment.

    Rationale:
    ----------
    Restricting USB access on the system will decrease the physical attack surface for a device
    and diminish the possible vectors to introduce malware.
    """
    pretty_print("[1.1.23] Disable USB Storage (Scored)")
    print()
    
    filesystem = 'usb-storage'

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

    expected_output_modprobe = "insmod /lib/modules/6.5.0-35-generic/kernel/fs/storage/usb-storage.ko"

    modprobe_disabled = expected_output_modprobe in modprobe_result.stdout or not modprobe_result.stdout.strip()
    lsmod_disabled = not lsmod_result.stdout.strip()

    with open(OUTPUT_FILE, "a") as f:
        f.write(f"[1.1.23] Disable USB Storage (Scored)")
        
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

        if modprobe_disabled and lsmod_disabled:
            print(f"USB Access is restricted.")
            f.write("USB Access is restricted.\n")
        else:
            print(f"USB Access is NOT restricted.")
            f.write("USB Access is NOT restricted.\n")
        print()
        
        f.write("===============================\n\n")
    print()

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
    # functions = inspect.getmembers(current_module, inspect.isfunction)

    source_lines, _ = inspect.getsourcelines(current_module)

    functions = []
    for line in source_lines:
        if line.strip().startswith('def ensure'):
            func_name = line.split('(')[0].replace('def ', '').strip()
            functions.append(func_name)

    for func_name in functions:
        func = getattr(current_module, func_name)
        func()
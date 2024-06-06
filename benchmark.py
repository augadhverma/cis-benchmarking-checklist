import distro

from datetime import datetime

SCORED = 0
NOTSCORED = 0
PASS = 0
FAILED = 0

from utils import unused_filesystems, pretty_print

def create_env_file(os_info: dict):
    filename = ".env"
    env_content = "\n".join([f"{key.upper().replace('_', '')}='{value}'" for key, value in os_info.items()])
    with open(filename, "w") as f:
        f.write(env_content)

def get_os_info() -> dict[str, str]:
    """Get the OS information required to check for compatible versions

    Returns:
        dict[str, str]: It contains information such as OS type (eg: ubuntu),
        OS version and OS codename.
    """
    os_type = distro.id()
    os_version = distro.version()
    os_codename = distro.codename()

    os_info = {
        "os_type": os_type,
        "os_version": os_version,
        "os_codename": os_codename
    }

    create_env_file(os_info)

    return os_info

if __name__ == '__main__':
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pretty_print("CIS BENCHMARKING CHECKLIST 1.0.0", upper_underline=True)
    print(f"Starting @ {now}\n")

    os_info = get_os_info()
    if os_info['os_version'] == '22.04' and os_info['os_type'] == 'ubuntu':
        print("Running Benchmark For:")
        pretty_print(f"Ubuntu ({os_info['os_codename']}) {os_info['os_version']}", upper_underline=True)

        unused_filesystems.run()
    else:
        print(f"{os_info['os_type']} is currently not supported.")
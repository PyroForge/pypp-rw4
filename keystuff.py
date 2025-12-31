import winreg
import subprocess
import platform
def set_repeat_w(delay, speed):
    # delay: 0 (shortest) to 3 (longest)
    # speed: 0 (slowest) to 31 (fastest)
    # delay 1 speed 31 default
    key_path = r"Control Panel\Keyboard"
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, "KeyboardDelay", 0, winreg.REG_SZ, str(delay))
        winreg.SetValueEx(reg_key, "KeyboardSpeed", 0, winreg.REG_SZ, str(speed))
        winreg.CloseKey(reg_key)
        print("Keyboard repeat delay and speed set successfully.")
        print("Please log off and log back in (or reboot) for changes to apply.")
    except Exception as e:
        print(f"Failed to set keyboard settings: {e}")
def set_repeat_l(delay, rate):
    # Ubuntu default: delay = 660ms, rate = 25 per second
    try:
        subprocess.run(["xset", "r", "rate", str(delay), str(rate)], check=True)
        print(f"Set keyboard repeat: delay={delay}ms, rate={rate} per second")
    except subprocess.CalledProcessError:
        print("Failed to set keyboard repeat. Is X running?")
def run():
    print("WARNING this is not necessary and it will edit your registry and make changes system wide if it gos wrong it potentially could break your computer.")
    input("Press enter to continue...")
    print("are you sure you want to do this? there will be no message after this and no canceling it")
    input("Press enter to continue...")
    if platform.system() == "Windows":
        set_repeat_w(0, 31)
    if platform.system() == "Linux":
        set_repeat_l(200, 31)
def undo():
    print("WARNING this is not necessary and it will edit your registry and make changes system wide if it gos wrong it potentially could break your computer.")
    input("Press enter to continue...")
    print("are you sure you want to do this? there will be no message after this and no canceling it")
    input("Press enter to continue...")
    if platform.system() == "Windows":
        set_repeat_w(1, 31)
    if platform.system() == "Linux":
        set_repeat_l(660, 25)
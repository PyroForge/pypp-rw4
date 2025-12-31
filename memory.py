import time
from multiprocessing import shared_memory

LOG_FILE = "log.txt"
LOG_EVERY_SECONDS = 1
LOG_CLEAR_SECONDS = 999999999999999

open_shms = {}
last_log_time = 0
last_clear_time = 0

def clear_log_if_needed():
    global last_clear_time
    now = time.time()
    if now - last_clear_time > LOG_CLEAR_SECONDS:
        last_clear_time = now
        # Clear the log file
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            pass  # Truncate file to zero length

def log_message(msg):
    clear_log_if_needed()  # Clear log if it's time
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {msg}\n")

def w(name, contents):
    if name == "currentbackground":
        a = open("variables/currentbackground", "w")
        a.write(contents)
        a.close()
    global last_log_time
    log_message(f"[w] name: '{name}', contents: '{contents}'")
    contents_bytes = contents.encode("utf-8")
    size = len(contents_bytes)
    try:
        shm = open_shms.get(name) or shared_memory.SharedMemory(name=name)
        if shm.size < size:
            shm.close()
            shm.unlink()
            log_message(f"[w] Resizing shared memory '{name}' from {shm.size} to {size}")
            shm = shared_memory.SharedMemory(name=name, create=True, size=size)
    except FileNotFoundError:
        shm = shared_memory.SharedMemory(name=name, create=True, size=size)
        log_message(f"[w] Created shared memory '{name}' of size {size}")
    shm.buf[:] = b'\x00' * len(shm.buf)
    shm.buf[:size] = contents_bytes
    open_shms[name] = shm  # Keep alive
    c = r(name)
    if c != contents:
        log_message(f"[w] ERROR: mismatch! expected '{contents}', got '{c}'")
    now = time.time()
    if now - last_log_time > LOG_EVERY_SECONDS:
        last_log_time = now
        log_message(f"[WRITE] {name} = '{contents}'")

def r(name):
    if name == "currentbackground":
        a = open("variables/currentbackground", "r")
        return a.read()
    global last_log_time
    log_message(f"[r] reading from '{name}'")
    try:
        shm = open_shms.get(name) or shared_memory.SharedMemory(name=name)
        raw_bytes = bytes(shm.buf[:]).rstrip(b'\x00')
        contents = raw_bytes.decode("utf-8")
        log_message(f"[r] Read: '{contents}'")
    except FileNotFoundError:
        log_message(f"[r] ERROR: '{name}' not found")
        return None
    except Exception as e:
        log_message(f"[r] ERROR while reading '{name}': {e}")
        return None
    now = time.time()
    if now - last_log_time > LOG_EVERY_SECONDS:
        last_log_time = now
        log_message(f"[READ] {name} = '{contents}'")
    return contents

def cleanup():
    for name, shm in open_shms.items():
        try:
            shm.close()
            shm.unlink()
            log_message(f"[cleanup] Closed and unlinked '{name}'")
        except Exception as e:
            log_message(f"[cleanup] Error cleaning '{name}': {e}")

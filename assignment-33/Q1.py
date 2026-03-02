# Q1. Add Thread monitoring feature
# for each running process display,
# - Process Name
# - PID
# - Number of thread created by proess
# store information in log.file alogwith timestamp

import psutil
import logging

logging.basicConfig(
    filename="log.file",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def monitor_process_threads():
    logging.info("Starting process/thread snapshot")
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            pid = proc.info.get("pid")
            name = proc.info.get("name") or "<unknown>"
            threads = proc.num_threads()
            line = f"Process Name: {name} | PID: {pid} | Threads: {threads}"
            logging.info(line)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # skip processes that disappeared or are not accessible
            continue


def main():
    monitor_process_threads()


if __name__ == "__main__":
    main()
import sys
from  _functions import *
from _colorama import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [log_file_path] [log_level]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) >= 3 else None

    logs = load_logs(log_file_path)
    if not logs:
        print("No logs loaded. Exiting.")
        sys.exit(1)

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        display_logs_by_level(filtered_logs, log_level.upper())
   

def display_log_counts(counts: dict):
    print("Logging level | Count")
    print("--------------|----------")
    for level, count in counts.items():
        print(f'{level:<14}|{count:<18}')


def display_logs_by_level(logs: list, level: str):
    print(f"\nDetails of logs for level '{level}':")
    print("----------------------------------")
    color = log_colors.get(level, Fore.RESET)
    for log in logs:
        print(f"{color}{log['date']} {log['time']} - {log['message']}{Fore.RESET}")


if __name__ == "__main__":
    main()









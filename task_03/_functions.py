def parse_log_line(line: str) -> dict: 
    try:
        components=line.strip().split(' ', 3)
        date,time,level,message=components
        return {
            "date": date,
            "time": time,
            "level": level,
            "message": message
            }                      
    except ValueError:
        print(f'Invalid format in the file:{line}')


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            logs = [parse_log_line(line) for line in f]
        return logs
    except FileNotFoundError:
        print(f"File {file_path} not found") 
        return []
    except Exception as e:
       print (f"Error {e}")
       return []


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x:x['level']==level,logs))

   
def count_logs_by_level(logs: list) -> dict:
    log_counts={}
    for log in logs:
        level=log['level']
        log_counts[level]=log_counts.get(level,0)+1
    return log_counts    
    


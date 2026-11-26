import datetime

def _time():
    return datetime.datetime.now().strftime("\033[90m%Y-%m-%d %H:%M:%S\033[0m")

class logger():
    @staticmethod
    def info(s):
        print(f"{_time()} \033[34m[KUROI/INFO]\033[0m \033[95m{s}\033[0m")
    @staticmethod
    def warn(s):
        print(f"{_time()} \033[33m[KUROI/WARN] {s}\033[0m")
    @staticmethod
    def error(s):
        print(f"{_time()} \033[31m[KUROI/ERROR] {s}\033[0m")

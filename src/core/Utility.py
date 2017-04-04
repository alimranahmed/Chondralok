import datetime


class Utility:
    @staticmethod
    def log(class_name, method_name, message):
        log_msg = "[" + str(datetime.datetime.now()) + "]"
        log_msg += "[" + class_name.__class__.__name__ + "][" + method_name + "] "
        log_msg += message
        print(log_msg)
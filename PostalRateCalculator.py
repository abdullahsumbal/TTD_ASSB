import sys
import re

class RateCalculator:

    def __init__(self, argv):
        self.argv = argv
        self.len_arg = len(argv)
        self.cal()

    def cal(self):
        error_msg_less_args = "Usage: Python3 from_postal_code to_postal_code length width height weight post_type"
        error_msg_more_args = "Usage: Python3 from_postal_code to_postal_code length width height weight post_type"
        error_msg_from_arg = "Invalid From: Postal Code"
        error_msg_to_arg = "Invalid To: Postal Code"
        error_msg_post_type = "Invalid Post Type: [Regular, Xpress, Prior]"

        # validate the argument length
        if self.len_arg < 7:
            return error_msg_less_args
        if self.len_arg > 7:
            return error_msg_more_args

        #validate from code_postal format
        from_postal_code_arg = self.argv[0]
        if (len(from_postal_code_arg) != 6):
            return error_msg_from_arg
        if (re.match("[YVTXSRPNMLKJGHECAB]{1}\d{1}[A-Z]{1}\d{1}[A-Z]{1}\d{1}", from_postal_code_arg)== None):
            return error_msg_from_arg

        #validate from code_postal format
        to_postal_code_arg = self.argv[1]
        if (len(to_postal_code_arg) != 6):
            return error_msg_to_arg
        if (re.match("[YVTXSRPNMLKJGHECAB]{1}\d{1}[A-Z]{1}\d{1}[A-Z]{1}\d{1}", to_postal_code_arg)== None):
            return error_msg_to_arg


        #validate post type
        post_type = self.argv[6]
        if (post_type not in ['Regular', 'Xpress', 'Prior']):
            return error_msg_post_type
        return

if __name__ == '__main__':
    sys.argv.pop(0)
    print(RateCalculator(sys.argv))


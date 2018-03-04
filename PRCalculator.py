import sys
import re
import json

class RateCalculator:

    def __init__(self, argv):
        self.argv = argv
        self.len_arg = len(argv)
        self.cal()

    def cal(self):
        error_msg_args = "Usage: Python3 from_postal_code to_postal_code width length height weight post_type"
        error_msg_from_arg = "Invalid From: Postal Code"
        error_msg_to_arg = "Invalid To: Postal Code"
        error_msg_post_type = "Invalid Post Type: [Regular, Xpress, Prior]"
        error_msg_width = "Invalid Width"
        error_msg_length = "Invalid Length"
        error_msg_height = "Invalid Height"

        # validate the argument length
        if self.len_arg < 7:
            return error_msg_args
        if self.len_arg > 7:

            return error_msg_args
        #validate from code_postal format
        from_postal_code_arg = self.argv[0]
        if (len(from_postal_code_arg) != 6):
            return error_msg_from_arg
        if (re.match("[YVTXSRPNMLKJGHECAB]{1}\d{1}[A-Z]{1}\d{1}[A-Z]{1}\d{1}", from_postal_code_arg)== None):
            return error_msg_from_arg

        #validate to code_postal format
        to_postal_code_arg = self.argv[1]
        if (len(to_postal_code_arg) != 6):
            return error_msg_to_arg
        if (re.match("[YVTXSRPNMLKJGHECAB]{1}\d{1}[A-Z]{1}\d{1}[A-Z]{1}\d{1}", to_postal_code_arg)== None):
            return error_msg_to_arg

        #validate post type
        post_type = self.argv[6]
        if (post_type not in ['Regular', 'Xpress', 'Prior']):
            return error_msg_post_type

        # validate width
        if (not self.argv[2].isdigit()):
            return error_msg_width
        width = int(self.argv[2])
        data = json.load(open('data.json'))
        max_width = data[post_type]['Max_Width']
        min_width = data[post_type]['Min_Width']
        if ( not (min_width <= width <= max_width)):
            return error_msg_width

        #validate length
        if (not self.argv[3].isdigit()):
            return error_msg_length
        length = int(self.argv[3])
        max_length = data[post_type]['Max_Length']
        min_length= data[post_type]['Min_Length']
        if (not (min_length <= length <= max_length)):
            return error_msg_length

        #validate height
        if (not self.argv[4].isdigit()):
            return error_msg_height
        height = int(self.argv[4])
        max_height = data[post_type]['Max_Height']
        min_height= data[post_type]['Min_Height']
        if (not (min_height <= height <= max_height)):
            return error_msg_height

        return

if __name__ == '__main__':
    sys.argv.pop(0)
    print(RateCalculator(sys.argv))


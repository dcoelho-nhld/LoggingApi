import dateutil.parser

class LogEntry:

    def __init__(self, dictionary):

        # Get the log details from the dictionary
        datetime_string = dictionary.get("datetime", None)
        self.log_datetime = dateutil.parser.parse(datetime_string) if datetime_string is not None else None
        self.project = dictionary.get("project", None)
        self.log_status = dictionary.get("logType", None)
        self.message = dictionary.get("message", "")

        # Check each of the key values to see if it's missing from dictionary
        required_key_values = ["datetime", "project", "logStatus"]
        missing_fields = list(filter(lambda x: dictionary.get(x, None) is None, required_key_values))

        # If there are any missing fields, then populate error message and set valid status to False
        if len(missing_fields) > 0:
            self.error_message = f"The following field(s) are missing: {str(missing_fields)}"
            self.valid = False
        else:
            self.valid = True

    def get_error_message(self):
        return self.error_message if self.error_message is not None else ""

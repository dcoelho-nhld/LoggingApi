from flask import request
from flask_httpauth import HTTPTokenAuth
from flask_restful import Resource

import Strings
from LogEntry import LogEntry


class TestAPI(Resource):
    token_auth = HTTPTokenAuth()

    @token_auth.login_required
    def post(self):
        try:
            # Get the body, which should be a JSON Array of JSON Objects
            dictionary_list = request.get_json()
            # For each JSON Object in the Array, try to create a log entry
            # Store the successful log entries in a list and error messages from invalid logs in another list
            logs = []
            errors = []
            for dictionary in dictionary_list:
                log = LogEntry(dictionary)
                if log.valid:
                    logs.append(log)
                else:
                    errors.append(log.get_error_message())
            # TODO - Connect this to logstash and/or database
            # Return the results as a dictionary (Flask will JSONify the dict) and the respective HTTP Status Code
            return self.generate_response(logs, errors)
        except TypeError as te:
            return "Error:" + str(te), 418
        except AttributeError as ae:
            return "Error:" + str(ae), 418

    @staticmethod
    def generate_response(logs, errors):
        log_amount = len(logs)
        error_amount = len(errors)
        # Status code is 200 if any records were created, else return error code
        status_code = 200 if log_amount > 0 else 418
        # Return a dictionary with results along with the respective status code
        results = {"hasErrors": error_amount > 0, "successes": log_amount, "failures": error_amount,
                   "errorMessages": errors}
        return results, status_code

    @token_auth.verify_token
    def verify_token(token):
        # Validate user's token against one of the hard coded values
        return token == Strings.token or token in Strings.tokens

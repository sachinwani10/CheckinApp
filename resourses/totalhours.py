from models.time_sheet import TimeSheetModel as TS
from flask_restful import Resource
from datetime import datetime

class TotalHours(Resource):
    def get(self, username, start_date, end_date):
        # modify start and end date to datetime
        start_date = datetime.strptime(start_date, '%Y-%d-%m')
        end_date = datetime.strptime(end_date, '%Y-%d-%m')
        result = TS.find_in_db(username, start_date, end_date)

        res = []
        hours_worked = []
        if result:
            for row in result:
                mydict = row.json()
                mydict['hours/minutes'] = \
                str(self.calculate_hours(row.timestamp_in, row.timestamp_out)[0]) \
                + " Hours - " + \
                str(self.calculate_hours(row.timestamp_in, row.timestamp_out)[1]) \
                + " Minutes"
                res.append(mydict)
            return {"Days": res}
        message = {"None": "None"}
        return message

    def calculate_hours(self, s_timestamp, e_timestamp):
        hours = e_timestamp - s_timestamp
        return divmod(hours.total_seconds(), 3600)

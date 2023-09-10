from flask import Flask, request, jsonify
from datetime import datetime
import pytz 

app = Flask(__name__)

github_url_source = 'https://github.com/idyweb/HNGx'


@app.route('/api', methods=['GET'])
def slack_details():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.now(pytz.utc).astimezone(pytz.timezone('Africa/Lagos')).strftime('%A')
    current_time = datetime.now(pytz.utc).astimezone(pytz.timezone('Africa/Lagos'))
    allowed_time_window = 2  # +/- 2 minutes
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

    time_window = current_time.replace(second=0, microsecond=0) - datetime.now(pytz.utc).astimezone(pytz.timezone('Africa/Lagos')).replace(second=0, microsecond=0)
    time_window_in_minutes = abs(time_window.total_seconds()) / 60

     # Validate the time window
    if time_window_in_minutes > allowed_time_window:
        return({'error': 'Time validation failed. UTC time is not within +/- 2 minutes.'}), 400
    
    
    github_url_file =  'https://github.com/idyweb/HNGx/blob/master/stage1.py'
    github_url_source= 'https://github.com/idyweb/HNGx'
    

    result = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_time_str,
        'track': track,
        'github_file_url': github_url_file,
        'github_repo_url': github_url_source,
        'status_code': 200

    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
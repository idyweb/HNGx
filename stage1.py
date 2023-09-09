from flask import Flask, request, jsonify 

app = Flask(__name__)


@app.route('/slack_details', methods=['GET'])
def slack_details():
    slack_name = request.args.get('slack_name')
    # current_day = request.args.get('current_day')
    # current_time = request.args.get('current_time')
    track = request.args.get('track')
    # github_url_file = request.args.get('file_url')
    # github_url_source= request.args.get('source_url')
    # status = request.args.get('status')
    

    result = {
        'slack_name': slack_name,
        'track': track

    }
    return result


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
import subprocess
import os

app = Flask(__name__)

@app.route('/run-python')
def run_python():
    script_path = 'C:/Users/tyler/RedditVideoMakerBot/main.py'
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    
    try:
        # Capture output and error from the subprocess
        result = subprocess.run(
            ['python', script_path],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        # Return the captured output and error
        return jsonify({'output': result.stdout, 'error': result.stderr})
    except UnicodeDecodeError as e:
        return jsonify({'error': 'UnicodeDecodeError: ' + str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

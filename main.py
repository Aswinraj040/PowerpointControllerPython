from flask import Flask, request, jsonify
import pyautogui

app = Flask(__name__)

@app.route('/control_commands', methods=['POST'])
def execute_query():
    try:
        data = request.get_json()
        print(data)
        command = data.get('command')

        if command == 'next':
            print("Received 'next' command")
            pyautogui.press('right')
        elif command == 'previous':
            pyautogui.press('left')
            print("Received 'previous' command")
        elif command == 'exit':
            pyautogui.press('esc')
            print("Received 'exit' command")
        elif command == 'enter':
            pyautogui.press('f5')
            print("Received 'enter' command")
        else:
            return jsonify({'status': 'error', 'message': 'Invalid command'})

        return jsonify({'status': 'success', 'message': 'Command executed successfully'})
    except Exception as e:
        print(str(e))
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    # Use 0.0.0.0 to listen on all public IPs
    app.run(host='0.0.0.0', port=5005)
from typing import Dict

class response:
    def send_response(self, status, message = None, data = None) -> Dict:
        return {
            'status': status,
            'message': message,
            'data': data
        }
from operator import index
import pprint
from typing import Dict
from utils.response import response

class notesRepository:
    def __init__(self) -> None:
        self.notes = [
            {
                'id': 1,
                'title': 'note 1',
                'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
            },
            {
                'id': 2,
                'title': 'note 2',
                'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
            },
            {
                'id': 3,
                'title': 'note 3',
                'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
            }
        ]

        self.response = response()

    def get(self) -> Dict:
        return self.notes

    def create(self, new_note) -> Dict:
        check_note = self.exists(new_note)

        if check_note['status']:
            note_id = int(check_note['data'])
            self.notes[note_id] = new_note
            return self.response.send_response(status=True, message='note exist, replacing instead')
        else:
            self.notes.append(new_note)
            return self.response.send_response(status=True, message='insert data success')

    def exists(self, note) -> Dict:
        for current_note in self.notes:
            if current_note['id'] == note['id']:
                return self.response.send_response(status=True, data=current_note[id])
            else:
                return self.response.send_response(status=False)

    def update(self, id, note) -> Dict:
        for current_note in self.notes:
            if current_note['id'] == id:
                current_note['title'] = note['title']
                current_note['content'] = note['content']
                return self.response.send_response(status=True, message='update data success')

        return self.response.send_response(status=False, message='update data failed')

    def delete(self, id) -> Dict:
        for index, current_note in enumerate(self.notes):
            if current_note['id'] == id:
                self.notes.pop(index)
                return self.response.send_response(status=True, message='delete data success')

        return self.response.send_response(status=False, message='delete data failed')
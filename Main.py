import random
from repositories.NotesRepository import notesRepository

class main:
    def __init__(self) -> None:
        self.notes_repo = notesRepository()

    def main_menu(self) -> None:
        print('===========================')
        print('=========MAIN MENU=========')
        print('1. Tampil data')
        print('2. Tambah data')
        print('3. About this program')
        print('4. Keluar Program')
        print('===========================')

        menu_selection = input('Silahkan pilih opsi anda... \n')

        self.main_navigation(int(menu_selection))

    def main_navigation(self, selected_option) -> None:
        match selected_option:
            case 1:
                self.view_note()
            case 2:
                self.create_note()
            case 3:
                print('about page')
                self.return_to_main_menu()
            case 4:
                exit()
            case _:
                print('opsi yang dipilih salah')
                self.return_to_main_menu()

    def return_to_main_menu(self):
        selected_option = input('\napakah anda ingin kembali ke menu utama? y/n \n')

        match selected_option:
            case "y":
                self.main_menu()
            case "n":
                exit()
    
    """Methods for menu's option"""

    def view_note(self):
        for note in self.notes_repo.get():
            print('')
            print('Judul: ', note['title'])
            print('Konten:')
            print(note['content'])

        self.return_to_main_menu()

    def create_note(self):
        title = input('masukkan judul catatan...\n')
        content = input('masukkan konten catatan...\n')

        new_note = {
            'id': random.randint(10, 200),
            'title': title,
            'content': content
        }

        self.notes_repo.create(new_note)
        self.return_to_main_menu()
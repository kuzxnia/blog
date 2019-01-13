import sys
import os
from shutil import copyfile
from datetime import datetime


def draft(x): return f'_{x}-draft.md'


def get_filename(name, date):
    if date is None:
        date = datetime.now()
    else:
        date = datetime.strptime(date, '%Y-%m-%d')
    return f'{date.year}-{date.month}-{date.day}-{name}.md'


def log_function_triggering(path):
    log = 'Nie podano parametrów wejściowych\n'
    for (dirpath, dirnames, filenames) in os.walk(os.path.join(dirname, '../_drafts/')):
        log += '  '.join(filenames)
    print(log + '\nPrzykład wywołania funkcji\n./new_post tools nazwa-nowego-pliku 2018-02-03')


if __name__ == '__main__':
    dirname, filename = os.path.split(os.path.abspath(__file__))
    if len(sys.argv) < 2:
        log_function_triggering(os.path.join(dirname, '../_drafts/'))
    else:
        draft_path = os.path.join(dirname, '../_drafts/') + draft(sys.argv[1])
        dest_path = os.path.join(dirname, '../_posts/') + \
            get_filename(sys.argv[2] if len(sys.argv) == 3 else sys.argv[1], sys.argv[3] if len(sys.argv) == 4 else None)

        copyfile(draft_path, dest_path)
        print(f'Pomyślnie utworzono {dest_path}')

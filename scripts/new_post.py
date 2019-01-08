import sys
import os
from shutil import copyfile
from datetime import datetime


def draft(x): return f'_{x}-draft.md'


def get_filename(name):
    now = datetime.now()
    return f'{now.year}-{now.month}-{now.day}-{name}.md'


if __name__ == '__main__':
    dirname, filename = os.path.split(os.path.abspath(__file__))
    dest_path = os.path.join(dirname, '../_posts/') + get_filename(sys.argv[2])
    draft_path = os.path.join(dirname, '../_drafts/') + draft(sys.argv[1])

    copyfile(draft_path, dest_path)
    print(f'Pomyślnie utworzono {dest_path}')

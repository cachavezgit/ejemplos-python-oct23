import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    head, tail = os.path.split(filename)
    import pdb; pdb.set_trace()
    return head

filename = r'C:\Users\cachavez\python1'# __file__
filename_path = get_path(filename)
print(f'path = {filename_path}')

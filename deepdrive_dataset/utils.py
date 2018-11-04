import errno
import os
import sys
import json

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def split_json(in_path, in_file, out_path):
    in_file_path = os.path.join(in_path, in_file)
    print('Splitting {}...'.format(in_file))
    
    with open(in_file_path, 'r') as in_json_file:
        # Read the file and convert it to a dictionary
        json_obj_list = json.load(in_json_file)

        for json_obj in json_obj_list:
            filename = os.path.join(out_path, json_obj['name'].split('.')[0] + '.json')
            with open(filename, 'w') as out_json_file:
                # Save each obj to their respective filepath
                # with pretty formatting thanks to `indent=4`
                json.dump(json_obj, out_json_file, indent=4)

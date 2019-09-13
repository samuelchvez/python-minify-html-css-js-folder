import os
import sys
import glob
import pathlib


from css_html_js_minify import process_single_html_file, process_single_css_file, process_single_js_file


root_dir = sys.argv[1]
output_dir = sys.argv[2]

# Ensure output_dir existence
pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

html_files = []
css_files = []
js_files = []

for file_path in list(set(glob.iglob(os.path.join(root_dir, '**/**'), recursive=True))):
    if '.git' not in file_path and '.min' not in file_path:
        if os.path.isfile(file_path):
            if '.html' in file_path or '.css' in file_path or '.js' in file_path:
                output_file_path = file_path.replace(root_dir, output_dir)
                file_dir = os.path.join(*output_file_path.split('/')[:-1])
                pathlib.Path(file_dir).mkdir(parents=True, exist_ok=True)

                if '.html' in file_path:
                    process_single_html_file(file_path, output_path=output_file_path)
                elif '.css' in file_path:
                    process_single_css_file(file_path, output_path=output_file_path)
                elif '.js' in file_path:
                    process_single_js_file(file_path, output_path=output_file_path)

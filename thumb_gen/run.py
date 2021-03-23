import  sys
import  shutil

from    .options        import  parseOpts, begin
from    .worker         import  Generator
from    .viewer         import  helps, args_error

def run(argument_list = False):
    try:
        input_dir, input_file, opt = parseOpts(argument_list)
    except TypeError:
        args_error()
        sys.exit()
    videos = begin(input_dir, input_file, opt)

    for video_path in videos:
        app = Generator(video_path)
        app.run()

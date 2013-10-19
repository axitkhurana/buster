"""Ghost Buster. Static site generator for Ghost.

Usage:
  buster.py generate [--domain=<local-address>]
  buster.py preview
  buster.py setup [--gh-repo=<repo-url>]
  buster.py deploy
  buster.py (-h | --help)
  buster.py --version

Options:
  -h --help                 Show this screen.
  --version                 Show version.
  --domain=<local-address>  Address of local ghost installation [default: local.tryghost.org].
  --gh-repo=<repo-url>      URL of your gh-pages repository.
"""
# XXX Assume static dir to be current dir if not specified in args

import os
import re
import shutil
import SocketServer
import SimpleHTTPServer
from docopt import docopt
from time import gmtime, strftime

STATIC_DIR = 'static'

arguments = docopt(__doc__, version='0.1')
static_path = os.path.join(os.path.dirname(__file__), STATIC_DIR)

if arguments['generate']:
    command = ("wget \\"
                 "--recursive \\"                # follow links to download entire site
                 "--page-requisites \\"          # grab everything: css / inlined images
                 "--domains {0} \\"              # don't grab anything outside ghost
                 "--no-parent \\"                # don't go to parent level
                 "--directory-prefix {1} \\"     # download contents to static/ folder
                 "--no-host-directories \\"      # don't create domain named folder
                 "{0}").format(arguments['--domain'], STATIC_DIR)

    os.system(command)

elif arguments['preview']:
    os.chdir(static_path)

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", 9000), Handler)

    print "Serving at port 9000"
    # gracefully handle interrupt here
    httpd.serve_forever()

elif arguments['setup']:
    if arguments['--gh-repo']:
        repo_url = arguments['--gh-repo']
    else:
        repo_url = raw_input("Enter the Github repository URL:\n").strip()

    # Create a fresh new static files directory
    if os.path.isdir(static_path):
        confirm = raw_input("This will destroy everything inside static/."
                       " Are you sure you want to continue? (y/N)").strip()
        if confirm != 'y' or confirm != 'Y':
            sys.exit(0)
        shutil.rmtree(static_path)

    os.mkdir(static_path)
    os.chdir(static_path)

    # User/Organization page -> master branch
    # Project page -> gh-pages branch
    branch = 'gh-pages'
    regex = re.compile(".*[\w-]+\.github\.(?:io|com).*")
    if regex.match(repo_url):
        branch = 'master'

    # Prepare git repository
    os.system("git init")
    if branch == 'gh-pages':
        os.system("git checkout -b gh-pages")
    os.system("git remote add origin {}".format(repo_url))

    print "All set! You can generate and deploy now."

elif arguments['deploy']:
    os.chdir(static_path)
    os.system("git add -A .")

    current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    os.system("git commit -m 'Blog update at {}'".format(current_time))

    os.system("git push origin {}".format(branch))
    print "Good job! Deployed to Github Pages."

elif arguments['domain']:
    pass

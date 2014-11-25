from pyquery import PyQuery
from StringIO import StringIO
from os import path
from urlparse import urljoin
from Queue import Queue
from threading import Thread
import requests, sys

URL = 'https://unsplash.com/grid?page=%d'
THREAD_COUNT = 3
DIRECTORY = 'img/'

class Downloader(Thread):
    def __init__(self, queue, directory):
        Thread.__init__(self)
        self.queue = queue
        self.directory = directory
        self.kill_received = False

    def run(self):
        while not self.kill_received:
            self.download(self.queue.get())
            self.queue.task_done()

    def download(self, url):
        basename = url.split('/')[-2]
        filename = '%s/%s.jpg' % (self.directory, basename)

        if path.exists(filename):
            return

        sys.stdout.write('Downloading %s.jpg\n' % (basename))
        sys.stdout.flush()

        response = requests.get(url)
        open(filename, 'wb').write(
            StringIO(response.content).read()
        )

def run(directory = DIRECTORY, *args):
    page = 1

    if any(args):
        directory = args.pop(0)

    if any(args):
        raise Exception('Unknown arguments')

    queue = Queue()
    threads = []
    for i in range(THREAD_COUNT):
         t = Downloader(queue, directory)
         t.daemon = True
         t.start()
         threads.append(t)

    sys.stdout.flush()

    while True:
        doc = PyQuery(URL % page)
        images = []

        for div in doc('.photo'):
            url = PyQuery(div).find('a').attr('href')
            queue.put(
                urljoin(URL, url)
            )

            images.append(url)

        page += 1

        if not any(images):
            break

    try:
        queue.join()
    except KeyboardInterrupt:
        for t in threads:
            t.kill_received = True

if __name__ == '__main__':
    run(*sys.argv[1:])

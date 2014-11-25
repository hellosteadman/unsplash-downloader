Unsplash Downloader
===================

The website [Unsplash](unsplash.com) has made a set of images available to
download for free and to use in any way. 10 new images are released each day.

I wanted a way to download them all so I wrote a multithreaded downloader that
would parse through the list of images on the homepage, paginate through the
infinitely-scrolling list and add the list of images to a queue to download.

You can adapt the parser in any way you see fit. I use PyQuery as it's a simple
DOM parser.

## Installation

1. Clone this repo or download the latest Zip file
2. Run `virtualenv .` on the directory you've downloaded the script to
3. Run `source bin/activate` to enter the environment
4. Run `pip install -r requirements.txt`

If you get trouble installing PyQuery because of an `lxml` issue on a Mac
or Linux machine, try running this:

```
STATIC_DEPS=true pip install pyquery
```

then retry step 4. It worked for me.

## Usage

Run `python unsplash.py <path>` to download images into the directory
specified in the `<path>` argument. If you don't specify a path, the script
will use the default directory `img`, but **it won't create the directory
for you**.

## Questions or suggestions?

Find me at [code.steadman.io](http://code.steadman.io/) or on
[Twitter](http://twitter.com/iamsteadman).

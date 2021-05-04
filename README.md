# image_tools #
CLI for image manipulation tasks:
* autocrop
* base64 conversion
* denoise
* deskew
* invert
* pdf conversion
* scale
* template matching (image within image)


## installation ##
Requires `python >= 3.6`. Installation involves cloning the repo to your local
disk, then running the `setup.py` script.
```
$ git clone https://github.com/dan-velez/image_tools
$ cd image_tools
$ python setup.py install
```


## usage ##
Once installed, you will have a command available on your system,
`image-tools.exe`.
```
usage: image-tools [-h] {autocrop,scale} ...

Run various image manipulation tasks.

positional arguments:
  {autocrop,scale}  Command
    autocrop        Detect rectangular contours in an image and crop out the
                    largest one.
    scale           Scale an image by an input factor.

optional arguments:
  -h, --help        show this help message and exit

image_tools <command> -h displays help on a particular command.
```


## running locally ##
To test the module locally without installing, `cd` into the project root and
type `python -m image_tools`. This will run the modules entry point, which 
happens to be a CLI.
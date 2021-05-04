#!/usr/bin/python
"""
CLI for image manipulation tasks:
    * autocrop
    * base64 conversion
    * denoise
    * deskew
    * invert
    * pdf conversion
    * scale
    * template matching (image within image)
"""

import sys
import argparse

# Subcommand classes
from image_tools.ImageAutocrop import ImageAutocrop
from image_tools.ImageScale import ImageScale


class ImageTools:
    """ClI for image manipulation tasks."""
   
    # Subcommand objects.
    imscale = ImageScale()
    imautocrop = ImageAutocrop()

    def run_cli (self):
        """Run the CLI for image_tools"""

        parser = argparse.ArgumentParser(
            prog="image-tools",
            description="Run various image manipulation tasks.",
            epilog="image_tools <command> -h displays help on a "+
                "particular command.")

        subparsers = parser.add_subparsers(
            help='Command',
            dest='command')

        ## autocrop ############################################################

        parser_autocrop = subparsers.add_parser(
            'autocrop',
            help='Detect rectangular contours in an image and crop out the '+
                'largest one.')

        parser_autocrop.add_argument(
            '-f',
            '--file',
            type=str,
            required=True,
            help="The path of the input image.")

        parser_autocrop.add_argument(
            '-o',
            '--outfile',
            type=str,
            required=True,
            help="The path of the output cropped image.")

        ## scale ###############################################################

        parser_autocrop = subparsers.add_parser(
            'scale',
            help='Scale an image by an input factor.')

        parser_autocrop.add_argument(
            '-f',
            '--file',
            type=str,
            required=True,
            help="The path of the input image.")

        parser_autocrop.add_argument(
            '-o',
            '--outfile',
            type=str,
            required=True,
            help="The path of the output scaled image.")

        parser_autocrop.add_argument(
            '-s',
            '--scale',
            type=float,
            required=True,
            help="A decimal number that is the scale of the output image.")

        ## parse args ##########################################################

        args = parser.parse_args()

        try:
            # Run command.
            if args.command ==   "autocrop": self.run_command_autocrop(args)
            elif args.command == "base64": pass
            elif args.command == "scale": self.run_command_scale(args)
            else: parser.print_help(sys.stderr)

        except KeyboardInterrupt:
            print("\n[* image_tools] Exiting. Goodbye!")
            sys.exit(1)

    def run_command_scale (self, args):
        """Run the scale subcommand."""
        infile = args.file
        outfile = args.outfile
        scale = args.scale
        print("[* image-tools] Scaling image by %s..." % scale)
        self.imscale.image_scale(infile, outfile, scale)
        print("[* image-tools] Image ready > %s" % outfile)

    def run_command_autocrop (self, args):
        """Run the autocrop subcommand."""
        infile = args.file
        outfile = args.outfile
        print("[* image-tools] Autocrop image...")
        self.imautocrop.autocrop(infile, outfile)
        print("[* image-tools] Image ready > %s" % outfile)


def main ():
    """Used as an entry point in the setup.py file to run the CLI."""
    ImageTools().run_cli()


if __name__ == "__main__":
    main()
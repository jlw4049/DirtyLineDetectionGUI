import argparse
from pathlib import Path
from typing import Optional, Sequence

from dirty_line_detection.edge_finder import EdgeFinder


class ArgParser:
    def __init__(self, argv: Optional[Sequence[str]] = None):
        # argparse class
        self.parser = argparse.ArgumentParser()

        # positional arguments
        self.parser.add_argument("file_input", help="Path to image file")

        # optional arguments
        self.parser.add_argument(
            "-o", "--file_output", help="Path to output file with suffix '.png'"
        )

        # parse args
        self.provided_args = vars(self.parser.parse_args(argv))

        # process args
        self._process_args()

    def _process_args(self):
        convert_image = EdgeFinder()
        convert_image.find_edges(Path(self.provided_args["file_input"]))

        if self.provided_args["file_output"]:
            convert_image.save_image(Path(self.provided_args["file_output"]))
        else:
            convert_image.save_image()


if __name__ == "__main__":
    ArgParser()

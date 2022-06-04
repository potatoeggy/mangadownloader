import dataclasses
from dataclasses import dataclass
from enum import Enum
from typing import Literal

from . import cbz, epub, pdf
from .base_converter import BaseConverter, ConvertFormats


def get_converter(convert_to: ConvertFormats) -> type[BaseConverter]:
    match convert_to:
        case ConvertFormats.CBZ:
            return cbz.CbzConverter
        case ConvertFormats.EPUB:
            return epub.EpubConverter
        case ConvertFormats.PDF:
            return pdf.PdfConverter

# Atom types in QuickTime image files

**Framework**: Quicktime File Format

Build QuickTime image files with atoms.

#### Overview

There are two mandatory atom types: `'idsc'`, which contains an image description, and `'idat'`, which contains the image data. This is illustrated in the following figure. A QuickTime image file can also contain other atoms.

In QuickTime 4, there is a new optional atom type `'iicc'`, which can store a ColorSync profile.

The following table shows an example QuickTime image file containing a JPEG-compressed image.

| Data | Description |
| --- | --- |
| `0000005E` | Atom size, 94 bytes |
| `69647363` | Atom type, `'idsc'` |
| `00000056` | Image description size, 86 bytes |
| `6A706567` | Compressor identifier, `'jpeg'` |
| `00000000` | Reserved, set to `0` |
| `0000` | Reserved, set to `0` |
| `0000` | Reserved, set to `0` |
| `00000000` | Major and minor version of this data, `0` if not applicable |
| `6170706C` | Vendor who compressed this data, `'appl'` |
| `00000000` | Temporal quality, `0` (no temporal compression) |
| `00000200` | Spatial quality, `codecNormalQuality` |
| `0140` | Image width, 320 |
| `00F0` | Image height, 240 |
| `00480000` | Horizontal resolution, 72 dpi |
| `00480000` | Vertical resolution, 72 dpi |
| `00003C57` | Data size, 15447 bytes (use `0` if unknown) |
| `0001` | Frame count, 1 |
| `0C 50 68 6F 74 6F 20 2D20 4A 50 45 47 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00` | Compressor name, “Photo - JPEG” (32-byte Pascal string) |
| `0018` | Image bit depth, 24 |
| `FFFF` | Color lookup table ID, `-1` (none) |
| `00003C5F` | Atom size, 15455 bytes |
| `69646174` | Atom type, `'idat'` |
| `FF D8 FF E0 00 10 4A 46 49 46 00 01 01 01 00 48 ...` | JPEG compressed data |

> ❗ **Important**: The exact order and size of atoms is not guaranteed to match the example in the preceeding figure. Applications reading QuickTime image files should always use the atom size to traverse the file and ignore atoms of unrecognized types.

> **Note**: Like QuickTime movie files, QuickTime image files are big-endian. However, image data is typically stored in the same byte order as specified by the particular compression format.

## See Also

- [Recommended file type and suffix](recommended_file_type_and_suffix.md)
  Identify your image file with a file type and suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/atom_types_in_quicktime_image_files)*
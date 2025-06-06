# File type compatibility atom ('ftyp')

**Framework**: Quicktime File Format  
**Kind**: class

An atom that identifies the file type specifications with which the file is compatible.

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

The file type compatibility atom, also called the file type atom, allows the reader to determine whether this is a type of file that the reader understands. Specifically, the file type atom identifies the file type specifications with which the file is compatible. This allows the reader to distinguish among closely related file types, such as QuickTime movie files, MPEG-4, and JPEG-2000 files (all of which may contain file type atoms, movie atoms, and movie data atoms).

When a file is compatible with more than one specification, the file type atom lists all the compatible types and indicates the preferred brand, or best use, among the compatible types. For example, a music player using a QuickTime-compatible file format might identify a file’s best use as a music file for that player but also identify it as a QuickTime movie.

The file type atom serves a further purpose of distinguishing among different versions or specifications of the same file type, allowing it to convey more information than the file extension or MIME type alone. The file type atom also has the advantage of being internal to the file, where it is less subject to accidental alteration than a file extension or MIME type.

> **Note**: The file type atom described here is functionally identical to the file type box defined in the ISO specifications for MPEG-4 and JPEG-2000.

The file type atom is optional, but strongly recommended. If present, it must be the first significant atom in the file, preceding the movie atom (and any free space atoms, preview atom, or movie data atoms).

The file type atom has an atom type value of `'ftyp'` and contains the following fields: [`Size`](file_type_compatibility_atom/size.md), [`Type`](file_type_compatibility_atom/type.md), [`Major brand`](file_type_compatibility_atom/major_brand.md), [`Minor version`](file_type_compatibility_atom/minor_version.md), [`Compatible brands`](file_type_compatibility_atom/compatible_brands.md).

If none of the [`Compatible brands`](file_type_compatibility_atom/compatible_brands.md) fields is set to `'qt  '`, then the file is not a QuickTime movie file and is not compatible with this specification. Applications should return an error and close the file, or else invoke a file importer appropriate to one of the specified brands, preferably the major brand. QuickTime currently returns an error when attempting to open a file whose file type, file extension, or MIME type identifies it as a QuickTime movie, but whose file type atom does not include the `'qt  '` brand.

> **Note**: A common source of this error is an MPEG-4 file incorrectly named with the .mov file extension or with the MIME type incorrectly set to `“video/quicktime”`. MPEG-4 files are automatically imported by QuickTime only when they are correctly identified as MPEG-4 files using the Mac OS file type, file extension, or MIME type.

If you are creating a file type that is fully compatible with the QuickTime file format, one of the [`Compatible brands`](file_type_compatibility_atom/compatible_brands.md) fields must be set to `'qt  '`; otherwise QuickTime will not recognize the file as a QuickTime movie.

> ⚠️ **Warning**: Use of the QuickTime file format in this manner is subject to license from Apple, Inc.

## Topics

### Data fields
- [Size](file_type_compatibility_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](file_type_compatibility_atom/type.md)
  A 32-bit unsigned integer that identifies the atom type, typically represented as a four-character code.
- [Major brand](file_type_compatibility_atom/major_brand.md)
  A 32-bit unsigned integer that represents a file format code.
- [Minor version](file_type_compatibility_atom/minor_version.md)
  A 32-bit field that indicates the file format specification version.
- [Compatible brands](file_type_compatibility_atom/compatible_brands.md)
  A series of unsigned 32-bit integers listing compatible file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/file_type_compatibility_atom)*
# Metadata atom ('meta')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that is the container for carrying metadata.

#### Overview

The following figure shows a sample layout of the metadata atom.

![A diagram that shows a box, with the captions “Metadata atom”, “Atom size”, and “Type = ‘meta’” inside the top of the box. Just below the captions is a box with a solid outline, inside the previous box, that extends almost the width of the containing box, and has the caption “Metadata handler atom ‘hdlr’”. Below that, also inside the Metadata atom box, is a box with a dotted outline that has the caption “Metadata header atom ‘mhdr’”. Below that, also inside the Metadata atom box, is a box with a solid outline that has the caption “Metadata item keys atom ‘keys’”. Below that, also inside the Metadata atom box, is a box with a solid outline that has the caption “Metadata item atom ‘](https://docs-assets.developer.apple.com/published/c0dc3209646369fa649d39fffb773837/metadata-atom%402x.png)

The metadata atom requires atoms with a solid outline, and atoms with a dotted outline are optional.

## Topics

### Data fields
- [Size](metadata_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](metadata_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Metadata handler atom](metadata_atom/metadata_handler_atom.md)
  An atom that defines the structure used for all types of metadata stored within the metadata atom.
- [Metadata header atom](metadata_atom/metadata_header_atom.md)
  An atom that holds the integer value for the next unique item identifier to assign.
- [Metadata item keys atom](metadata_atom/metadata_item_keys_atom.md)
  An atom that holds a list of the metadata keys that may be present in the metadata atom.
- [Metadata item list atom](metadata_atom/metadata_item_list_atom.md)
  An atom that holds a list of actual metadata values that are present in the metadata atom.
- [Country list atom](metadata_atom/country_list_atom.md)
  An atom that lists items that are suitable for more than one country.
- [Language list atom](metadata_atom/language_list_atom.md)
  An atom that lists items that are suitable for more than one language.

## See Also

- [Metadata handler atom ('hdlr')](metadata_handler_atom.md)
  An atom that defines the structure used for all types of metadata stored within the metadata atom.
- [Metadata header atom ('mhdr')](metadata_header_atom.md)
  An atom that holds the integer value for the next unique item identifier to assign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_atom)*
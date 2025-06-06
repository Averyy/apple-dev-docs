# Item information atom ('itif')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains information about the item, including item-specific flags and item optional identifier.

#### Overview

The optional item information atom contains information about the item: item-specific flags and item optional identifier. This ID must be unique within the metadata atom. To simplify assignment of item identifiers, the metadata header atom’s nextItemInfo field can be used as described in [`Metadata header atom ('mhdr')`](metadata_header_atom.md).

The item information atom must be present if the item has an assigned ID or has nonzero flags.

No flags are currently defined; they should be set to `0` in this version of the specification.

The item information atom is a full atom with an atom type of `‘itif’`.

## Topics

### Data fields
- [Size](item_information_atom/size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Type](item_information_atom/type.md)
  A 32-bit unsigned integer value.
- [Version](item_information_atom/version.md)
  One byte.
- [Flags](item_information_atom/flags.md)
  Three bytes.
- [Item_ID](item_information_atom/item_id.md)
  An unsigned 32-bit integer, unique within the container.

## See Also

- [Country list atom ('ctry')](country_list_atom.md)
  An atom that lists items that are suitable for more than one country.
- [Language list atom ('lang')](language_list_atom.md)
  An atom that lists items that are suitable for more than one language.
- [Metadata item keys atom ('keys')](metadata_item_keys_atom.md)
  An atom that holds a list of the metadata keys that may be present in the metadata atom.
- [Metadata item list atom ('ilst')](metadata_item_list_atom.md)
  An atom that holds a list of actual metadata values that are present in the metadata atom.
- [Metadata item atom](metadata_item_atom.md)
  An atom that holds a metadata value.
- [Value atom](value_atom.md)
  An atom that expresses a metadata value.
- [Name atom ('name')](name_atom.md)
  An atom you use to provide a name for a metadata item.
- [Data atom ('data')](data_atom.md)
  An atom that contains the type and locale specific value of metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/item_information_atom)*
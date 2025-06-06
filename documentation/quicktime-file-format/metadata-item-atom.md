# Metadata item atom

**Framework**: QuickTime File Format  
**Kind**: class

An atom that holds a metadata value.

#### Overview

Each item in the metadata item list atom is identified by its key. The atom type for each metadata item atom should be set equal to the index of the key for the metadata within the item atom, taking this index from the metadata item keys atom. In addition, each metadata item atom contains a Value Atom, to hold the value of the metadata item.

## Topics

### Data fields
- [Item_info](metadata_item_atom/item_info.md)
  An optional item information atom.
- [Name](metadata_item_atom/name.md)
  An optional name atom.
- [Data_value_atom[]](metadata_item_atom/data_value_atom.md)
  An array of value atoms.

## See Also

- [Country list atom ('ctry')](country_list_atom.md)
  An atom that lists items that are suitable for more than one country.
- [Language list atom ('lang')](language_list_atom.md)
  An atom that lists items that are suitable for more than one language.
- [Metadata item keys atom ('keys')](metadata_item_keys_atom.md)
  An atom that holds a list of the metadata keys that may be present in the metadata atom.
- [Metadata item list atom ('ilst')](metadata_item_list_atom.md)
  An atom that holds a list of actual metadata values that are present in the metadata atom.
- [Value atom](value_atom.md)
  An atom that expresses a metadata value.
- [Item information atom ('itif')](item_information_atom.md)
  An atom that contains information about the item, including item-specific flags and item optional identifier.
- [Name atom ('name')](name_atom.md)
  An atom you use to provide a name for a metadata item.
- [Data atom ('data')](data_atom.md)
  An atom that contains the type and locale specific value of metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_item_atom)*
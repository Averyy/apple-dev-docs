# Name atom ('name')

**Framework**: QuickTime File Format  
**Kind**: class

An atom you use to provide a name for a metadata item.

#### Overview

The Name atom is a full atom with an atom type of `‘name’`. This atom contains a metadata name formatted as a string of UTF-8 characters, to fill the atom. It is optional. If it is not present, the item is unnamed, and cannot be referred to by name. Names are not user visible; they provide a way to refer to metadata items. The maximum length of a name may be limited in specific environments.

No two metadata items may have the same name.

## Topics

### Data fields
- [Version](name_atom/version.md)
  One byte.
- [Flags](name_atom/flags.md)
  Three bytes.
- [Name](name_atom/name.md)
  An array of bytes, constituting a UTF-8 string, containing the name.

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
- [Item information atom ('itif')](item_information_atom.md)
  An atom that contains information about the item, including item-specific flags and item optional identifier.
- [Data atom ('data')](data_atom.md)
  An atom that contains the type and locale specific value of metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/name_atom)*
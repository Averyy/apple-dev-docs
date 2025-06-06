# Data atom ('data')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains the type and locale specific value of metadata.

#### Overview

The Data atom has an atom type of `‘data’`, and contains four bytes each of type and locale indicators, as specified in [`Type indicator`](type_indicator.md) and [`Locale indicator`](locale_indicator.md), and then the actual value of the metadata, formatted as required by the type.

## Topics

### Data fields
- [Type indicator](data_atom/type_indicator.md)
  Four bytes that indicate a type of data that QuickTime supports.
- [Locale indicator](data_atom/locale_indicator.md)
  A four-byte value that indicates a locale.
- [Value](data_atom/value.md)
  An array of bytes containing the value of the metadata.

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
- [Name atom ('name')](name_atom.md)
  An atom you use to provide a name for a metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/data_atom)*
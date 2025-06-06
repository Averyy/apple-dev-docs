# Value atom

**Framework**: QuickTime File Format  
**Kind**: class

An atom that expresses a metadata value.

#### Overview

The value of the metadata item is expressed as immediate data in a value atom. The value atom starts with two fields: a type indicator, and a locale indicator. Both the type and locale indicators are four bytes long. There may be multiple ‘value’ entries, using different type, country or language codes (see [`Data ordering`](data_ordering.md) for the required ordering).

## Topics

### Data fields
- [Type indicator](value_atom/type_indicator.md)
  Four bytes that indicate a type of data that QuickTime supports.
- [Locale indicator](value_atom/locale_indicator.md)
  A four-byte value that indicates a locale.

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
- [Item information atom ('itif')](item_information_atom.md)
  An atom that contains information about the item, including item-specific flags and item optional identifier.
- [Name atom ('name')](name_atom.md)
  An atom you use to provide a name for a metadata item.
- [Data atom ('data')](data_atom.md)
  An atom that contains the type and locale specific value of metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/value_atom)*
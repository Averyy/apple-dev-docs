# Metadata locale atom ('loca')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that tags a metadata value with a locale.

#### Overview

A metadata value may optionally be tagged with its locale so that it may be chosen based upon the user’s language, country, and so on. This tagging makes it possible to include several keys of the same key type (e.g., copyright or scene description) but with differing locales for users with different languages or locations. The type of the metadata locale atom is `‘loca’`.

If the metadata locale atom is absent, metadata values should be considered appropriate for all locales.

The layout of a metadata locale atom is as follow:

| Data field | Bytes |
| --- | --- |
| [`Size`](metadata_locale_atom/size.md) | 4 |
| [`Type`](metadata_locale_atom/type.md) = `'loca'` | 4 |
| [`Locale string`](metadata_locale_atom/locale_string.md) | variable |

## Topics

### Data fields
- [Size](metadata_locale_atom/size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Type](metadata_locale_atom/type.md)
  A 32-bit unsigned integer value.
- [Locale string](metadata_locale_atom/locale_string.md)
  A string holding a language tag.

## See Also

- [Metadata key table atom ('keys')](metadata_key_table_atom.md)
  An atom that contains a table of keys and mappings to payload data in the corresponding timed metadata media samples.
- [Bit rate atom ('btrt')](bit_rate_atom.md)
  An atom that signals the bit rate information of a stream.
- [Metadata key atom](metadata_key_atom.md)
  An atom that contains a key that corresponds to the timed metadata track containing it.
- [Metadata key declaration atom ('keyd')](metadata_key_declaration_atom.md)
  An atom that holds the key namespace and key value of that namespace for the given values.
- [Metadata datatype definition atom ('dtyp')](metadata_datatype_definition_atom.md)
  An atom you use to specify the data type of the metadata key atom’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_locale_atom)*
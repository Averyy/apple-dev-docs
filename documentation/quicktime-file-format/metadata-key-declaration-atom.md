# Metadata key declaration atom ('keyd')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that holds the key namespace and key value of that namespace for the given values.

#### Overview

The metadata key declaration atom holds the key namespace and key value of that namespace for the given values. The type of the metadata key declaration atom is `‘keyd’`.

The layout of a metadata key declaration atom is as follows:

| Data field | Bytes |
| --- | --- |
| [`Size`](metadata_key_declaration_atom/size.md) | 4 |
| [`Type`](metadata_key_declaration_atom/type.md) = `'keyd'` | 4 |
| [`Key_namespace`](metadata_key_declaration_atom/key_namespace.md) | 4 |
| [`Key_value array`](metadata_key_declaration_atom/key_value_array.md) | variable |

## Topics

### Data fields
- [Size](metadata_key_declaration_atom/size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Type](metadata_key_declaration_atom/type.md)
  A 32-bit unsigned integer value.
- [Key_namespace](metadata_key_declaration_atom/key_namespace.md)
  A 32-bit identifier describing the domain and the structure of the key value.
- [Key_value array](metadata_key_declaration_atom/key_value_array.md)
  An array of unsigned 8-bit bytes holding the key’s value.

## See Also

- [Metadata key table atom ('keys')](metadata_key_table_atom.md)
  An atom that contains a table of keys and mappings to payload data in the corresponding timed metadata media samples.
- [Bit rate atom ('btrt')](bit_rate_atom.md)
  An atom that signals the bit rate information of a stream.
- [Metadata key atom](metadata_key_atom.md)
  An atom that contains a key that corresponds to the timed metadata track containing it.
- [Metadata datatype definition atom ('dtyp')](metadata_datatype_definition_atom.md)
  An atom you use to specify the data type of the metadata key atom’s value.
- [Metadata locale atom ('loca')](metadata_locale_atom.md)
  An atom that tags a metadata value with a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_key_declaration_atom)*
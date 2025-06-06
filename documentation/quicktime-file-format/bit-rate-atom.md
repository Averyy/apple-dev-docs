# Bit rate atom ('btrt')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that signals the bit rate information of a stream.

#### Overview

The optional bit rate atom may be present at the end of any timed metadata sample description to signal the bit rate information of a stream. The bit rate information can be used for buffer configuration.

The layout of a bit rate atom is as follows:

| Data field | Bytes |
| --- | --- |
| [`Size`](bit_rate_atom/size.md) | 4 |
| [`Type`](bit_rate_atom/type.md) = `'btrt'` | 4 |
| [`Buffer size`](bit_rate_atom/buffer_size.md) | 4 |
| [`Max bit rate`](bit_rate_atom/max_bit_rate.md) | 4 |
| [`Average bit rate`](bit_rate_atom/average_bit_rate.md) | 4 |

## Topics

### Data fields
- [Size](bit_rate_atom/size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Type](bit_rate_atom/type.md)
  A 32-bit unsigned integer value.
- [Buffer size](bit_rate_atom/buffer_size.md)
  A 32-bit unsigned integer that indicates the suggested size of the associated data buffer.
- [Max bit rate](bit_rate_atom/max_bit_rate.md)
  A 32-bit unsigned integer that indicates the maximum bit rate in bits/second of the associated media stream.
- [Average bit rate](bit_rate_atom/average_bit_rate.md)
  A 32-bit unsigned integer that indicates the average bit rate in bits/second of the associated media stream.

## See Also

- [Metadata key table atom ('keys')](metadata_key_table_atom.md)
  An atom that contains a table of keys and mappings to payload data in the corresponding timed metadata media samples.
- [Metadata key atom](metadata_key_atom.md)
  An atom that contains a key that corresponds to the timed metadata track containing it.
- [Metadata key declaration atom ('keyd')](metadata_key_declaration_atom.md)
  An atom that holds the key namespace and key value of that namespace for the given values.
- [Metadata datatype definition atom ('dtyp')](metadata_datatype_definition_atom.md)
  An atom you use to specify the data type of the metadata key atom’s value.
- [Metadata locale atom ('loca')](metadata_locale_atom.md)
  An atom that tags a metadata value with a locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/bit_rate_atom)*
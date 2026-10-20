# Type

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit unsigned integer value.

#### Overview

Set to `'keys'`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Version](./version.md)
  One byte.
- [Flags](./flags.md)
  Three bytes.
- [Entry_count](./entry_count.md)
  A 32-bit integer indicating the number of key arrays to follow in this atom.
- [Key_size](./key_size.md)
  A 32-bit integer indicating the size of the entire structure containing a key definition.
- [Key_namespace](./key_namespace.md)
  A 32-bit integer defining a naming scheme used for metadata keys.
- [Key_value[Key_size-8]](./key_value_key_size-8.md)
  An array of 8-bit integers, each containing the actual name of the metadata key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_item_keys_atom/type)*
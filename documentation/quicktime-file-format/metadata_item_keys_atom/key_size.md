# Key_size

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit integer indicating the size of the entire structure containing a key definition.

#### Overview

The `key_size` = `sizeof(key_size) + sizeof(key_namespace) + sizeof(key_value)`. Since `key_size` and `key_namespace` are both 32 bit integers, together they have a size of 8 bytes. Hence, the `key_value` structure will be equal to `key_size - 8`.

## See Also

- [Size](metadata_item_keys_atom/size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Type](metadata_item_keys_atom/type.md)
  A 32-bit unsigned integer value.
- [Version](metadata_item_keys_atom/version.md)
  One byte.
- [Flags](metadata_item_keys_atom/flags.md)
  Three bytes.
- [Entry_count](metadata_item_keys_atom/entry_count.md)
  A 32-bit integer indicating the number of key arrays to follow in this atom.
- [Key_namespace](metadata_item_keys_atom/key_namespace.md)
  A 32-bit integer defining a naming scheme used for metadata keys.
- [Key_value[Key_size-8]](metadata_item_keys_atom/key_value_key_size-8.md)
  An array of 8-bit integers, each containing the actual name of the metadata key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_item_keys_atom/key_size)*
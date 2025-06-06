# Key_value[Key_size-8]

**Framework**: QuickTime File Format  
**Kind**: property

An array of 8-bit integers, each containing the actual name of the metadata key.

#### Overview

Keys with the `‘mdta’` namespace use a reverse DNS naming convention. For example, the location metadata coordinates use a metadata `key_value` of `‘com.apple.quicktime.location.ISO6709’`.

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
- [Key_size](metadata_item_keys_atom/key_size.md)
  A 32-bit integer indicating the size of the entire structure containing a key definition.
- [Key_namespace](metadata_item_keys_atom/key_namespace.md)
  A 32-bit integer defining a naming scheme used for metadata keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_item_keys_atom/key_value_key_size-8)*
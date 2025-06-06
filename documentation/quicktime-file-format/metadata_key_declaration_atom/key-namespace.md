# Key_namespace

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit identifier describing the domain and the structure of the key value.

#### Overview

For example, this could indicate that `key_value` is a reverse-address style string (such as “com.apple.quicktime.ISO6709”), a binary four-character code (such as a `'cprt'` user data key), a Uniform Resource Identifier (URI), or other structures (such as native formats from other metadata standards). New key namespaces must be registered but because a reverse-address style string can often be used, using the reverse-address key namespace may be sufficient for most uses.

## See Also

- [Size](metadata_key_declaration_atom/size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Type](metadata_key_declaration_atom/type.md)
  A 32-bit unsigned integer value.
- [Key_value array](metadata_key_declaration_atom/key_value_array.md)
  An array of unsigned 8-bit bytes holding the key’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_key_declaration_atom/key_namespace)*
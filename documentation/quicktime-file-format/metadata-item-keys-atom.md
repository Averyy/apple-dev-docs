# Metadata item keys atom ('keys')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that holds a list of the metadata keys that may be present in the metadata atom.

#### Overview

The metadata item keys atom holds a list of the metadata keys that may be present in the metadata atom. This list is indexed starting with `1`; `0` is a reserved index value. The metadata item keys atom is a full atom with an atom type of `‘keys’`.

Note that:

- Indexes into the metadata item keys atom are 1-based (`1…entry_count`).
- Zero (`0`) is reserved and never used as an index.
- The structure of `key_value` depends upon the key namespace.

The following figure shows a typical metadata item keys atom.

![A diagram that shows a box, with the captions “Item keys atom” and “Type = ‘keys’” inside the top of the box. Just below the captions is a box, inside the previous box, that extends almost the width of the containing box, and has the caption “Entry count = 4”. Below that box are three columns of boxes, each with four rows. Each row of boxes is captioned “size”, “namespace”, and “value” from right to left. Outside the enclosing box there is a marker line that spans the four rows of boxes, with the caption “Key definitions.”](https://docs-assets.developer.apple.com/published/4e8940f990ae4a64cddd5b758a81e4a7/metadata-item-keys-atom%402x.png)

The following figure shows an example of a metadata item keys atom consisting of three keys: two from one key namespace and a third from another key namespace.

| `'keys'` |
| --- |
| `entry_count = 3` |

|  | `key_size (uint32)` | `key_namespace (uint32)` | `key_value (uint8[])` |
| --- | --- | --- | --- |
| 1 | `38` | `'mdta'` | `com.apple.quicktime.copyright` |
| 2 | `35` | `'mdta'` | `com.apple.quicktime.author` |
| 3 | `12` | `'udta'` | `@cpy` |

## Topics

### Data fields
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
- [Key_value[Key_size-8]](metadata_item_keys_atom/key_value_key_size-8.md)
  An array of 8-bit integers, each containing the actual name of the metadata key.

## See Also

- [Country list atom ('ctry')](country_list_atom.md)
  An atom that lists items that are suitable for more than one country.
- [Language list atom ('lang')](language_list_atom.md)
  An atom that lists items that are suitable for more than one language.
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
- [Data atom ('data')](data_atom.md)
  An atom that contains the type and locale specific value of metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_item_keys_atom)*
# Metadata item list atom ('ilst')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that holds a list of actual metadata values that are present in the metadata atom.

#### Overview

The metadata item list atom holds a list of actual metadata values that are present in the metadata atom. The metadata items are formatted as a list of items. The metadata item list atom is of type `‘ilst’` and contains a number of metadata items, each of which is an atom.

The following figure shows a metadata list atom and the item/key connection.

![A diagram that shows a box, with the captions “Metadata atom”, “Atom size”, and “Type = ‘meta’” inside the top of the box. Next to that box is another box with the captions “Keys” and “entry_count = 4”. There is an arrow pointing from the metadata atom box to the keys box. Inside the keys box, below the captions, are four vertically stacked boxes, with captions “Key 1”, “Key 2”, “Key 3” and “Key 4”. The box with the caption “Key 3” is a different color that the other boxes. Inside the metadata item list atom box are three vertically stacked boxes, with the captions “key_index 2”, “key_index 4”, and “key_index 1”. Each of those boxes contains three boxes. The first box has a solid outline that has the caption “Data” with three field names listed below: “the_type”, “the_locale”, and “value[]”. The second and third boxes each have a dotted outline and are stacked vertically to the right of the box with the “Data” caption. The second box has the caption “itif” and the third box has the caption “name”.](https://docs-assets.developer.apple.com/published/83c35dc403cccb3b0abdaa51c9e45ffe/metadata-item-list-atom%402x.png)

## Topics

### Data fields
- [Type](metadata_item_list_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Item list](metadata_item_list_atom/item_list.md)
  A list of metadata values and related keys.

## See Also

- [Country list atom ('ctry')](country_list_atom.md)
  An atom that lists items that are suitable for more than one country.
- [Language list atom ('lang')](language_list_atom.md)
  An atom that lists items that are suitable for more than one language.
- [Metadata item keys atom ('keys')](metadata_item_keys_atom.md)
  An atom that holds a list of the metadata keys that may be present in the metadata atom.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_item_list_atom)*
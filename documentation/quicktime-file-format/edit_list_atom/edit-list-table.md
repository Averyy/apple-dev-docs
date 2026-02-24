# Edit list table

**Framework**: QuickTime File Format  
**Kind**: property

An array of 32-bit values, grouped into entries containing 3 values each.

## Mentions

- [Representing encoder delay explicitly](example_representing_encoder_delay_explicitly.md)

#### Overview

The layout of the entries in this table is as follows.

| Field | Bytes |
| --- | --- |
| Track duration | 4 |
| Media time | 4 |
| Media rate | 4 |

An edit list table entry contains the following elements.

- **Track duration**: A 32-bit integer that specifies the duration of this edit segment in units of the movie’s time scale.
- **Media time**: A 32-bit integer containing the starting time within the media of this edit segment (in media timescale units). If this field is set to `–1`, it is an empty edit. The last edit in a track should never be an empty edit. Any difference between the movie’s duration and the track’s duration is expressed as an implicit empty edit.
- **Media rate**: A 32-bit fixed-point number that specifies the relative rate at which to play the media corresponding to this edit segment. This rate value cannot be `0` or negative.

## See Also

- [Size](edit_list_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this edit list atom.
- [Type](edit_list_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](edit_list_atom/version.md)
  A 1-byte specification of the version of this edit list atom.
- [Flags](edit_list_atom/flags.md)
  Three bytes of space for flags.
- [Number of entries](edit_list_atom/number_of_entries.md)
  A 32-bit integer that specifies the number of entries in the edit list atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/edit_list_atom/edit_list_table)*
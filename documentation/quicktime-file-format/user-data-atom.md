# User data atom ('udta')

**Framework**: QuickTime File Format  
**Kind**: class

An atom where you define and store data associated with a QuickTime object.

#### Overview

The layout of a user data atom is as follows.

| Data field | Bytes |
| --- | --- |
| [`Size`](user_data_atom/size.md) | 4 |
| [`Type`](user_data_atom/type.md) | 4 |
| [`User data list`](user_data_atom/user_data_list.md) | Variable |

## Topics

### Data fields
- [Size](user_data_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this user data atom.
- [Type](user_data_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [User data list](user_data_atom/user_data_list.md)
  A series of user data atoms.

## See Also

- [Track name atom ('tnam')](track_name_atom.md)
  An atom that provides a name for a track.
- [Print to video atom ('ptv ')](print_to_video_atom.md)
  An atom you use to play the movie in full-screen mode, with no window and no visible controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/user_data_atom)*
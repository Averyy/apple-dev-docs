# User data list

**Framework**: QuickTime File Format  
**Kind**: property

A series of user data atoms.

#### Overview

A user data list that is formatted as a series of atoms. Each data element in the user data list contains size and type information along with its payload data. For historical reasons, the data list is optionally terminated by a 32-bit integer set to `0`. If you are writing a program to read user data atoms, allow for the terminating `0`. However, if you are writing a program to create user data atoms, you can safely leave out the terminating `0`.

For a list of defined list entry types, see [`User data atoms`](user_data_atoms.md).

## See Also

- [Size](user_data_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this user data atom.
- [Type](user_data_atom/type.md)
  A 32-bit integer that identifies the atom type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/user_data_atom/user_data_list)*
# Data references

**Framework**: QuickTime File Format  
**Kind**: property

An array of data references.

#### Overview

Each data reference is formatted like an atom and contains the following data elements.

The currently defined data reference types that can be stored in a header atom are as follows:

| Data reference type | Description |
| --- | --- |
| `'alis'` | Data reference is a Macintosh alias. An alias contains information about the file it refers to, including its full path name. |
| `'rsrc'` | Data reference is a Macintosh alias. Appended to the end of the alias is the resource type (stored as a 32-bit integer) and ID (stored as a 16-bit signed integer) to use within the specified file. This data reference type is deprecated in the QuickTime file format. This information documents existing content containing `'rsrc'` data references; don’t use it for new development. |
| `'url '` | A C string that specifies a URL. There may be additional data after the C string. |

## See Also

- [Size](media_data_reference_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this data reference atom.
- [Type](media_data_reference_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](media_data_reference_atom/version.md)
  A 1-byte specification of the version of this data reference atom.
- [Flags](media_data_reference_atom/flags.md)
  A 3-byte space for data reference flags.
- [Number of entries](media_data_reference_atom/number_of_entries.md)
  A 32-bit integer containing the count of data references that follow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/media_data_reference_atom/data_references)*
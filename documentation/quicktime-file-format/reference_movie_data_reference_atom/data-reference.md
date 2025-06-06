# Data reference

**Framework**: QuickTime File Format  
**Kind**: property

A data reference to a QuickTime movie, or to a stream or file that QuickTime can play.

#### Overview

If the reference type is `'alis'` this field contains the contents of an `AliasHandle`. If the reference type is `'url '` this field contains a NULL-terminated string that can be interpreted as a URL. The URL can be absolute or relative, and can specify any protocol that QuickTime supports, including `http://`, `ftp://`, `rtsp://`, `file:///`, and `data:`.

## See Also

- [Size](reference_movie_data_reference_atom/size.md)
  The number of bytes in this data reference atom.
- [Type](reference_movie_data_reference_atom/type.md)
  The type of this atom.
- [Flags](reference_movie_data_reference_atom/flags.md)
  A 32-bit integer containing flags.
- [Data reference type](reference_movie_data_reference_atom/data_reference_type.md)
  The data reference type.
- [Data reference size](reference_movie_data_reference_atom/data_reference_size.md)
  The size of the data reference in bytes, expressed as a 32-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/reference_movie_data_reference_atom/data_reference)*
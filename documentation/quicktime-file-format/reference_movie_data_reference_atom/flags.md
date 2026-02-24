# Flags

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit integer containing flags.

#### Overview

One flag is currently defined.

- **Movie is self-contained**: If the least-significant bit is set to `1`, the movie is self-contained. This requires that the parent movie contain a movie header atom as well as a reference movie atom. In other words, the current `'moov'` atom must contain both a `'rmra'` atom and a `'mvhd'` atom. To resolve this data reference, an application uses the movie defined in the movie header atom, ignoring the remainder of the fields in this data reference atom, which are used only to specify external movies.

## See Also

- [Size](reference_movie_data_reference_atom/size.md)
  The number of bytes in this data reference atom.
- [Type](reference_movie_data_reference_atom/type.md)
  The type of this atom.
- [Data reference type](reference_movie_data_reference_atom/data_reference_type.md)
  The data reference type.
- [Data reference size](reference_movie_data_reference_atom/data_reference_size.md)
  The size of the data reference in bytes, expressed as a 32-bit integer.
- [Data reference](reference_movie_data_reference_atom/data_reference.md)
  A data reference to a QuickTime movie, or to a stream or file that QuickTime can play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/reference_movie_data_reference_atom/flags)*
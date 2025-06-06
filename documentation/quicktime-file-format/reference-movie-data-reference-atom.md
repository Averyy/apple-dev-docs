# Data reference atom

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains the information necessary to locate a movie, stream or file.

#### Overview

The information to locate a movie, stream, or file is typically in the form of a URL or a file alias. Only one data reference atom is allowed in a given movie reference descriptor atom.

## Topics

### Data fields
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
- [Data reference](reference_movie_data_reference_atom/data_reference.md)
  A data reference to a QuickTime movie, or to a stream or file that QuickTime can play.

## See Also

- [Reference movie atom ('rmra')](reference_movie_atom.md)
  A reference movie atom contains references to one or more movies.
- [Reference movie descriptor atom ('rmda')](reference_movie_descriptor_atom.md)
  An atom that contains other atoms that describe where to find a particular movie, the system requirements to play that movie, and a quality rating.
- [Data rate atom ('rmdr')](data_rate_atom.md)
  A data rate atom specifies the minimum data rate required to play a movie.
- [CPU speed atom ('rmcs')](cpu_speed_atom.md)
  A CPU speed atom specifies the minimum computing power needed to display a movie.
- [Version check atom ('rmvc')](version_check_atom.md)
  A version check atom specifies a software package, such as QuickTime or QuickTime VR, and the version of that package needed to display a movie.
- [Component detect atom ('rmcd')](component_detect_atom.md)
  A component detect atom specifies a QuickTime component, such as a particular video decompressor, required to play the movie.
- [Movie importer component flags](movie_importer_component_flags.md)
  Flags that adjust the behavior of the movie import component.
- [Quality atom ('rmqu')](quality_atom.md)
  A quality atom describes the relative quality of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/reference_movie_data_reference_atom)*
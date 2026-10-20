# Data rate atom ('rmdr')

**Framework**: QuickTime File Format  
**Kind**: class

A data rate atom specifies the minimum data rate required to play a movie.

#### Overview

A data rate atom specifies the minimum data rate required to play a movie. This is normally compared to the connection speed setting in the user’s QuickTime Settings control panel. Applications should play the movie with the highest data rate less than or equal to the user’s connection speed. If the connection speed is slower than any movie’s data rate, applications should play the movie with the lowest data rate. The movie with the highest data rate is assumed to have the highest quality.

Only one data rate atom is allowed in a given reference movie descriptor atom.

## Topics

### Data fields
- [Size](data_rate_atom/size.md)
  The number of bytes in this data rate atom.
- [Type](data_rate_atom/type.md)
  The type of this atom.
- [Flags](data_rate_atom/flags.md)
  A 32-bit integer.
- [Data rate](data_rate_atom/data_rate.md)
  The required data rate in bits per second, expressed as a 32-bit integer.

## See Also

- [Reference movie atom ('rmra')](reference_movie_atom.md)
  A reference movie atom contains references to one or more movies.
- [Reference movie descriptor atom ('rmda')](reference_movie_descriptor_atom.md)
  An atom that contains other atoms that describe where to find a particular movie, the system requirements to play that movie, and a quality rating.
- [Reference movie data reference atom ('rdrf')](reference_movie_data_reference_atom.md)
  An atom that contains the information necessary to locate a movie, stream or file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/data_rate_atom)*
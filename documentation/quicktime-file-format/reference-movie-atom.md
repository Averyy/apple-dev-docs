# Reference movie atom ('rmra')

**Framework**: QuickTime File Format  
**Kind**: class

A reference movie atom contains references to one or more movies.

#### Overview

It can optionally contain a list of system requirements in order for each movie to play, and a quality rating for each movie. It is typically used to specify a list of alternate movies to be played under different conditions.

A reference movie atom’s parent is always a movie atom (`'moov'`). Only one reference movie atom is allowed in a given movie atom.

## Topics

### Data fields
- [Size](reference_movie_atom/size.md)
  The number of bytes in this reference movie atom.
- [Type](reference_movie_atom/type.md)
  The type of this atom.
- [Reference movie descriptor atom](reference_movie_atom/reference_movie_descriptor_atom.md)
  A reference movie atom must contain at least one reference movie descriptor atom, and typically contains more than one.

## See Also

- [Reference movie descriptor atom ('rmda')](reference_movie_descriptor_atom.md)
  An atom that contains other atoms that describe where to find a particular movie, the system requirements to play that movie, and a quality rating.
- [Reference movie data reference atom ('rdrf')](reference_movie_data_reference_atom.md)
  An atom that contains the information necessary to locate a movie, stream or file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/reference_movie_atom)*
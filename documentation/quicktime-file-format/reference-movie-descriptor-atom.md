# Reference movie descriptor atom ('rmda')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains other atoms that describe where to find a particular movie, the system requirements to play that movie, and a quality rating.

#### Overview

The reference movie descriptor atom contains other atoms that describe where a particular movie can be found, and optionally what the system requirements are to play that movie, as well as an optional quality rating for that movie.

A reference movie descriptor atom’s parent is always a movie reference atom (`'rmra'`). Multiple reference movie descriptor atoms are allowed in a given movie reference atom, and more than one is usually present.

## Topics

### Data fields
- [Size](reference_movie_descriptor_atom/size.md)
  The number of bytes in this reference movie descriptor atom.
- [Type](reference_movie_descriptor_atom/type.md)
  The type of this atom.
- [Data reference atom](reference_movie_descriptor_atom/data_reference_atom.md)
  Each reference movie atom must contain exactly one data reference atom.
- [Data rate atom](reference_movie_descriptor_atom/data_rate_atom.md)
  A reference movie atom may contain an optional data rate atom.
- [CPU speed atom](reference_movie_descriptor_atom/cpu_speed_atom.md)
  A reference movie atom may contain an optional CPU speed atom.
- [Version check atom](reference_movie_descriptor_atom/version_check_atom.md)
  A reference movie atom may contain an optional version check atom.
- [Component detect atom](reference_movie_descriptor_atom/component_detect_atom.md)
  A reference movie atom may contain an optional component detect atom.
- [Quality atom](reference_movie_descriptor_atom/quality_atom.md)
  A reference movie atom may contain an optional quality atom.

## See Also

- [Reference movie atom ('rmra')](reference_movie_atom.md)
  A reference movie atom contains references to one or more movies.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/reference_movie_descriptor_atom)*
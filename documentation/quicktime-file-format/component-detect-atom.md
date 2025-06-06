# Component detect atom ('rmcd')

**Framework**: QuickTime File Format  
**Kind**: class

A component detect atom specifies a QuickTime component, such as a particular video decompressor, required to play the movie.

#### Overview

The component type, subtype, and other required attributes can be specified, as well as a minimum version. Multiple component detect atoms are allowed within a given reference movie descriptor atom. Applications should not attempt to play a movie unless at least the minimum versions of all required components are present.

## Topics

### Data fields
- [Size](component_detect_atom/size.md)
  The number of bytes in this component detect atom.
- [Type](component_detect_atom/type.md)
  The type of this atom.
- [Flags](component_detect_atom/flags.md)
  A 32-bit integer.
- [Component description](component_detect_atom/component_description.md)
  A component description record.
- [Minimum version](component_detect_atom/minimum_version.md)
  An unsigned 32-bit integer containing the minimum required version of the specified component.

## See Also

- [Reference movie atom ('rmra')](reference_movie_atom.md)
  A reference movie atom contains references to one or more movies.
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
- [Movie importer component flags](movie_importer_component_flags.md)
  Flags that adjust the behavior of the movie import component.
- [Quality atom ('rmqu')](quality_atom.md)
  A quality atom describes the relative quality of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/component_detect_atom)*
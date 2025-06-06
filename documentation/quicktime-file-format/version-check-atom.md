# Version check atom ('rmvc')

**Framework**: QuickTime File Format  
**Kind**: class

A version check atom specifies a software package, such as QuickTime or QuickTime VR, and the version of that package needed to display a movie.

#### Overview

The package is specified using a Macintosh Gestalt type, such a `'qtim'` for QuickTime (QuickTime provides support for these Gestalt tests in the Windows computing environment). You can specify a minimum required version to be returned by the Gestalt check, or you can require that a specific value be returned after performing a binary AND operation on the Gestalt bitfield and a mask. Multiple version check atoms are allowed within a given reference movie descriptor atom. Applications should not attempt to play a movie unless all version checks are successful.

## Topics

### Data fields
- [Size](version_check_atom/size.md)
  The number of bytes in this version check atom.
- [Type](version_check_atom/type.md)
  The type of this atom.
- [Flags](version_check_atom/flags.md)
  A 32-bit integer.
- [Software package](version_check_atom/software_package.md)
  A 32-bit Gestalt type specifying the software package to check for.
- [Version](version_check_atom/version.md)
  An unsigned 32-bit integer containing either the minimum required version or the required value after a binary `AND` operation.
- [Mask](version_check_atom/mask.md)
  The mask for a binary `AND` operation on the Gestalt bitfield.
- [Check type](version_check_atom/check_type.md)
  The type of check to perform, expressed as 16-bit integer.

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
- [Component detect atom ('rmcd')](component_detect_atom.md)
  A component detect atom specifies a QuickTime component, such as a particular video decompressor, required to play the movie.
- [Movie importer component flags](movie_importer_component_flags.md)
  Flags that adjust the behavior of the movie import component.
- [Quality atom ('rmqu')](quality_atom.md)
  A quality atom describes the relative quality of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/version_check_atom)*
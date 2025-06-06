# CPU speed atom ('rmcs')

**Framework**: QuickTime File Format  
**Kind**: class

A CPU speed atom specifies the minimum computing power needed to display a movie.

#### Overview

A CPU speed atom specifies the minimum computing power needed to display a movie. QuickTime performs an internal test to determine the speed of the user’s computer.

This is not a simple measurement of clock speed — it is a measurement of performance for QuickTime-related operations. Speed is expressed as a relative value between `100` and `2^31`, in multiples of `100`.

Applications play the movie with the highest specified CPU speed that is less than or equal to the user’s speed. If the user’s speed is lower than any movie’s CPU speed, applications play the movie with the lowest CPU speed requirement. The movie with the highest CPU speed is assumed to be the highest quality.

Only one CPU speed atom is allowed in a given reference movie descriptor atom.

## Topics

### Data fields
- [Size](cpu_speed_atom/size.md)
  The number of bytes in this CPU speed atom.
- [Type](cpu_speed_atom/type.md)
  The type of this atom.
- [Flags](cpu_speed_atom/flags.md)
  A 32-bit integer that is always 0.
- [CPU speed](cpu_speed_atom/cpu_speed.md)
  A relative ranking of required computer speed, expressed as a 32-bit integer divisible by 100, with larger numbers indicating higher speed.

## See Also

- [Reference movie atom ('rmra')](reference_movie_atom.md)
  A reference movie atom contains references to one or more movies.
- [Reference movie descriptor atom ('rmda')](reference_movie_descriptor_atom.md)
  An atom that contains other atoms that describe where to find a particular movie, the system requirements to play that movie, and a quality rating.
- [Reference movie data reference atom ('rdrf')](reference_movie_data_reference_atom.md)
  An atom that contains the information necessary to locate a movie, stream or file.
- [Data rate atom ('rmdr')](data_rate_atom.md)
  A data rate atom specifies the minimum data rate required to play a movie.
- [Version check atom ('rmvc')](version_check_atom.md)
  A version check atom specifies a software package, such as QuickTime or QuickTime VR, and the version of that package needed to display a movie.
- [Component detect atom ('rmcd')](component_detect_atom.md)
  A component detect atom specifies a QuickTime component, such as a particular video decompressor, required to play the movie.
- [Movie importer component flags](movie_importer_component_flags.md)
  Flags that adjust the behavior of the movie import component.
- [Quality atom ('rmqu')](quality_atom.md)
  A quality atom describes the relative quality of a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/cpu_speed_atom)*
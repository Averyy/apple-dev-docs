# Type

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit integer that identifies the atom type.

#### Overview

This field must be set to `'tkhd'`.

## See Also

- [Size](track_header_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this track header atom.
- [Version](track_header_atom/version.md)
  A 1-byte specification of the version of this track header.
- [Flags](track_header_atom/flags.md)
  Three bytes that are reserved for the track header flags.
- [Creation time](track_header_atom/creation_time.md)
  A 32-bit integer that indicates the creation calendar date and time for the track header.
- [Modification time](track_header_atom/modification_time.md)
  A 32-bit integer that indicates the last change date for the track header.
- [Track ID](track_header_atom/track_id.md)
  A 32-bit integer that uniquely identifies the track.
- [Reserved](track_header_atom/reserved.md)
  A 32-bit integer that is reserved for use by Apple.
- [Duration](track_header_atom/duration.md)
  A time value that indicates the duration of this track, in the movie’s time coordinate system.
- [Reserved](track_header_atom/reserved_2.md)
  An 8-byte value that is reserved for use by Apple.
- [Layer](track_header_atom/layer.md)
  A 16-bit integer that indicates this track’s spatial priority in its movie.
- [Alternate group](track_header_atom/alternate_group.md)
  A 16-bit integer that identifies a collection of movie tracks that contain alternate data for one another.
- [Volume](track_header_atom/volume.md)
  A 16-bit fixed-point value that indicates how loudly to play this track’s sound.
- [Reserved](track_header_atom/reserved_3.md)
  A 16-bit integer that is reserved for use by Apple.
- [Matrix structure](track_header_atom/matrix_structure.md)
  The matrix structure associated with this track.
- [Track width](track_header_atom/track_width.md)
  A 32-bit fixed-point number that specifies the width of this track in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_header_atom/type)*
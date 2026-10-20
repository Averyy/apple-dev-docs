# Type

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit integer that identifies the atom type.

#### Overview

This field must be set to `'tkhd'`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this track header atom.
- [Version](./version.md)
  A 1-byte specification of the version of this track header.
- [Flags](./flags.md)
  Three bytes that are reserved for the track header flags.
- [Creation time](./creation_time.md)
  A 32-bit integer that indicates the creation calendar date and time for the track header.
- [Modification time](./modification_time.md)
  A 32-bit integer that indicates the last change date for the track header.
- [Track ID](./track_id.md)
  A 32-bit integer that uniquely identifies the track.
- [Reserved](./reserved.md)
  A 32-bit integer that is reserved for use by Apple.
- [Duration](./duration.md)
  A time value that indicates the duration of this track, in the movie’s time coordinate system.
- [Reserved](./reserved_2.md)
  An 8-byte value that is reserved for use by Apple.
- [Layer](./layer.md)
  A 16-bit integer that indicates this track’s spatial priority in its movie.
- [Alternate group](./alternate_group.md)
  A 16-bit integer that identifies a collection of movie tracks that contain alternate data for one another.
- [Volume](./volume.md)
  A 16-bit fixed-point value that indicates how loudly to play this track’s sound.
- [Reserved](./reserved_3.md)
  A 16-bit integer that is reserved for use by Apple.
- [Matrix structure](./matrix_structure.md)
  The matrix structure associated with this track.
- [Track width](./track_width.md)
  A 32-bit fixed-point number that specifies the width of this track in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_header_atom/type)*
# Matrix structure

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

The matrix structure associated with this movie.

#### Overview

A matrix shows how to map points from one coordinate space into another. See [Matrices](../matrices.md) for a discussion of how display matrices are used in QuickTime.

For a matrix in the following format:

![A mathematical matrix with three rows and three columns. The top row contains the values a, b, and u. The middle row contains the values c, d, and v. The bottom row contains the values x, y, and w.](https://developer.apple.com/tutorials/images/com.apple.qtff/matrix-structure@2x.png)

Specify the matrix elements in the following sequence: `a`, `b`, `u`, `c`, `d`, `v`, `x`, `y`, `w`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this movie header atom.
- [Type](./type.md)
  A 32-bit integer that identifies the atom type.
- [Version](./version.md)
  A 1-byte specification of the version of this movie header atom.
- [Flags](./flags.md)
  Three bytes of space for future movie header flags.
- [Creation time](./creation_time.md)
  A 32-bit integer that specifies the creation calendar date and time for the movie atom.
- [Modification time](./modification_time.md)
  A 32-bit integer that specifies the calendar date and time of the last change to the movie atom.
- [Time scale](./time_scale.md)
  A time value that indicates the time scale for this movie.
- [Duration](./duration.md)
  A time value that indicates the duration of the movie in time scale units.
- [Preferred rate](./preferred_rate.md)
  A 32-bit fixed-point number that specifies the rate at which to play this movie.
- [Preferred volume](./preferred_volume.md)
  A 16-bit fixed-point number that specifies how loud to play this movie’s sound.
- [Reserved](./reserved.md)
  Ten bytes reserved for use by Apple.
- [Preview time](./preview_time.md)
  The time value in the movie at which the preview begins.
- [Preview duration](./preview_duration.md)
  The duration of the movie preview in movie time scale units.
- [Poster time](./poster_time.md)
  The time value of the time of the movie poster.
- [Selection time](./selection_time.md)
  The time value for the start time of the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_header_atom/matrix_structure)*
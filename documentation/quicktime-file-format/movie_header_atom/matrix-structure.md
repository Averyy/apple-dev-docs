# Matrix structure

**Framework**: QuickTime File Format  
**Kind**: property

The matrix structure associated with this movie.

#### Overview

A matrix shows how to map points from one coordinate space into another. See [`Matrices`](matrices.md) for a discussion of how display matrices are used in QuickTime.

For a matrix in the following format:

![A mathematical matrix with three rows and three columns. The top row contains the values a, b, and u. The middle row contains the values c, d, and v. The bottom row contains the values x, y, and w.](https://docs-assets.developer.apple.com/published/a592804690d97c48b180e61e28905fa3/matrix-structure%402x.png)

Specify the matrix elements in the following sequence: `a`, `b`, `u`, `c`, `d`, `v`, `x`, `y`, `w`.

## See Also

- [Size](movie_header_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this movie header atom.
- [Type](movie_header_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](movie_header_atom/version.md)
  A 1-byte specification of the version of this movie header atom.
- [Flags](movie_header_atom/flags.md)
  Three bytes of space for future movie header flags.
- [Creation time](movie_header_atom/creation_time.md)
  A 32-bit integer that specifies the creation calendar date and time for the movie atom.
- [Modification time](movie_header_atom/modification_time.md)
  A 32-bit integer that specifies the calendar date and time of the last change to the movie atom.
- [Time scale](movie_header_atom/time_scale.md)
  A time value that indicates the time scale for this movie.
- [Duration](movie_header_atom/duration.md)
  A time value that indicates the duration of the movie in time scale units.
- [Preferred rate](movie_header_atom/preferred_rate.md)
  A 32-bit fixed-point number that specifies the rate at which to play this movie.
- [Preferred volume](movie_header_atom/preferred_volume.md)
  A 16-bit fixed-point number that specifies how loud to play this movie’s sound.
- [Reserved](movie_header_atom/reserved.md)
  Ten bytes reserved for use by Apple.
- [Preview time](movie_header_atom/preview_time.md)
  The time value in the movie at which the preview begins.
- [Preview duration](movie_header_atom/preview_duration.md)
  The duration of the movie preview in movie time scale units.
- [Poster time](movie_header_atom/poster_time.md)
  The time value of the time of the movie poster.
- [Selection time](movie_header_atom/selection_time.md)
  The time value for the start time of the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_header_atom/matrix_structure)*
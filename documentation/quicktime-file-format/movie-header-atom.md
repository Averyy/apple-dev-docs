# Movie header atom ('mvhd')

**Framework**: Quicktime File Format  
**Kind**: class

An atom that specifies the characteristics of an entire QuickTime movie.

#### Overview

You use the movie header atom to specify the characteristics of an entire QuickTime movie. The data contained in this atom defines characteristics of the entire QuickTime movie, such as time scale and duration. It has an atom type value of `'mvhd'`.

The following table shows the layout of the movie header atom. The movie header atom is a leaf atom.

| Data field | Bytes |
| --- | --- |
| [`Size`](movie_header_atom/size.md) | 4 |
| [`Type`](movie_header_atom/type.md) | 4 |
| [`Version`](movie_header_atom/version.md) | 1 |
| [`Flags`](movie_header_atom/flags.md) | 3 |
| [`Creation time`](movie_header_atom/creation_time.md) | 4 |
| [`Modification time`](movie_header_atom/modification_time.md) | 4 |
| [`Time scale`](movie_header_atom/time_scale.md) | 4 |
| [`Duration`](movie_header_atom/duration.md) | 4 |
| [`Preferred rate`](movie_header_atom/preferred_rate.md) | 4 |
| [`Preferred volume`](movie_header_atom/preferred_volume.md) | 2 |
| [`Matrix structure`](movie_header_atom/matrix_structure.md) | 36 |
| [`Preview time`](movie_header_atom/preview_time.md) | 4 |
| [`Preview duration`](movie_header_atom/preview_duration.md) | 4 |
| [`Poster time`](movie_header_atom/poster_time.md) | 4 |
| [`Selection time`](movie_header_atom/selection_time.md) | 4 |
| [`Selection duration`](movie_header_atom/selection_duration.md) | 4 |
| [`Current time`](movie_header_atom/current_time.md) | 4 |
| [`Next track ID`](movie_header_atom/next_track_id.md) | 4 |

> **Note**: Set the creation and modification date with coordinated universal time (UTC). In prior versions of the QuickTime file format, this was not specified, and these fields were commonly set to local time for the time zone where the movie was created.

## Topics

### Data fields
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
- [Matrix structure](movie_header_atom/matrix_structure.md)
  The matrix structure associated with this movie.
- [Preview time](movie_header_atom/preview_time.md)
  The time value in the movie at which the preview begins.
- [Preview duration](movie_header_atom/preview_duration.md)
  The duration of the movie preview in movie time scale units.
- [Poster time](movie_header_atom/poster_time.md)
  The time value of the time of the movie poster.
- [Selection time](movie_header_atom/selection_time.md)
  The time value for the start time of the current selection.
- [Selection duration](movie_header_atom/selection_duration.md)
  The duration of the current selection in movie time scale units.
- [Current time](movie_header_atom/current_time.md)
  The time value for current time position within the movie.
- [Next track ID](movie_header_atom/next_track_id.md)
  A 32-bit integer that indicates a value to use for the track ID number of the next track added to this movie.

## See Also

- [Movie atom ('moov')](movie_atom.md)
  An atom that specifies the information that defines a movie.
- [Color table atom ('ctab')](color_table_atom.md)
  An atom that defines a list of preferred colors for displaying the movie on devices that support only 256 colors.
- [User data atoms](user_data_atoms.md)
  Atoms you use to define and store data associated with a QuickTime object.
- [Interleaving movie data](interleaving_movie_data.md)
  Interleave data in your movie for optimal playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/movie_header_atom)*
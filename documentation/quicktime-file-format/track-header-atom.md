# Track header atom ('tkhd')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies the characteristics of a single track within a movie.

#### Overview

The track header atom specifies the characteristics of a single track within a movie. A track header atom contains a size field that specifies the number of bytes and a type field that indicates the format of the data (defined by the atom type `'tkhd'`).

The layout of a track header atom is as follows.

| Data field | Bytes |
| --- | --- |
| [`Size`](track_header_atom/size.md) | 4 |
| [`Type`](track_header_atom/type.md) | 4 |
| [`Version`](track_header_atom/version.md) | 1 |
| [`Flags`](track_header_atom/flags.md) | 3 |
| [`Creation time`](track_header_atom/creation_time.md) | 4 |
| [`Modification time`](track_header_atom/modification_time.md) | 4 |
| [`Track ID`](track_header_atom/track_id.md) | 4 |
| [`Reserved`](track_header_atom/reserved.md) | 4 |
| [`Duration`](track_header_atom/duration.md) | 4 |
| [`Reserved`](track_header_atom/reserved_2.md) | 8 |
| [`Layer`](track_header_atom/layer.md) | 2 |
| [`Alternate group`](track_header_atom/alternate_group.md) | 2 |
| [`Volume`](track_header_atom/volume.md) | 2 |
| [`Reserved`](track_header_atom/reserved_3.md) | 2 |
| [`Matrix structure`](track_header_atom/matrix_structure.md) | 36 |
| [`Track width`](track_header_atom/track_width.md) | 4 |
| [`Track height`](track_header_atom/track_height.md) | 4 |

The track header atom contains the track characteristics for the track, including temporal, spatial, and volume information.

## Topics

### Data fields
- [Size](track_header_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this track header atom.
- [Type](track_header_atom/type.md)
  A 32-bit integer that identifies the atom type.
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
- [Track height](track_header_atom/track_height.md)
  A 32-bit fixed-point number that indicates the height of this track in pixels.

## See Also

- [Track atom ('trak')](track_atom.md)
  An atom that defines a single track of a movie.
- [Track exclude from autoselection atom ('txas')](track_exclude_from_autoselection_atom.md)
  An atom that indicates not to automatically select this track.
- [Track aperture mode dimension atoms](track_aperture_mode_dimension_atoms.md)
  Atoms that store information for each of the track aperture presentation modes.
- [Clipping atom ('clip')](clipping_atom.md)
  An atom that specifies the clipping regions for movies and for tracks.
- [Clipping region atom ('crgn')](clipping_region_atom.md)
  An atom that specifies the clipping region.
- [Track matte atom ('matt')](track_matte_atom.md)
  An atom you use to visually blend the track’s image when it is displayed.
- [Compressed matte atom ('kmat')](compressed_matte_atom.md)
  An atom that specifies the image description structure and the matte data associated with a particular matte atom.
- [Edit atom ('edts')](edit_atom.md)
  An atom that defines the portions of the media that are to be used to build up a track for a movie.
- [Edit list atom ('elst')](edit_list_atom.md)
  An atom that maps from a time in a movie to a time in a media, and ultimately to media data.
- [Playing with edit lists](playing_with_edit_lists.md)
  Repeat a segment of a movie without copying media with edit lists.
- [Track load settings atom ('load')](track_load_settings_atom.md)
  An atom that indicates how the track is to be used in its movie.
- [Track reference atoms](track_reference_atoms.md)
  Atoms that defines relationships between tracks.
- [Track input map atoms](track_input_map_atoms.md)
  Atoms that define how data being sent to this track from its nonprimary sources is to be interpreted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_header_atom)*
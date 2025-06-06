# Track load settings atom ('load')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that indicates how the track is to be used in its movie.

#### Overview

Track load settings atoms contain information that indicates how the track is to be used in its movie. Applications that read QuickTime files can use this information to process the movie data more efficiently. Track load settings atoms have an atom type value of `'load'`.

The layout of a track load settings atom is as follows.

| Track load settings atom | Bytes |
| --- | --- |
| [`Size`](track_load_settings_atom/size.md) | 4 |
| [`Type`](track_load_settings_atom/type.md) | 4 |
| [`Preload start time`](track_load_settings_atom/preload_start_time.md) | 4 |
| [`Preload duration`](track_load_settings_atom/preload_duration.md) | 4 |
| [`Preload flags`](track_load_settings_atom/preload_flags.md) | 4 |
| [`Default hints`](track_load_settings_atom/default_hints.md) | 4 |

## Topics

### Data fields
- [Size](track_load_settings_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this track load settings atom.
- [Type](track_load_settings_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Preload start time](track_load_settings_atom/preload_start_time.md)
  A 32-bit integer specifying the starting time, in the movie’s time coordinate system, of a segment of the track that is to be preloaded.
- [Preload duration](track_load_settings_atom/preload_duration.md)
  A 32-bit integer specifying the duration, in the movie’s time coordinate system, of a segment of the track that is to be preloaded.
- [Preload flags](track_load_settings_atom/preload_flags.md)
  A 32-bit integer containing flags governing the preload operation.
- [Default hints](track_load_settings_atom/default_hints.md)
  A 32-bit integer containing playback hints.

## See Also

- [Track atom ('trak')](track_atom.md)
  An atom that defines a single track of a movie.
- [Track header atom ('tkhd')](track_header_atom.md)
  An atom that specifies the characteristics of a single track within a movie.
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
- [Track reference atoms](track_reference_atoms.md)
  Atoms that defines relationships between tracks.
- [Track input map atoms](track_input_map_atoms.md)
  Atoms that define how data being sent to this track from its nonprimary sources is to be interpreted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_load_settings_atom)*
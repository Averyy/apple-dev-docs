# Track atom ('trak')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that defines a single track of a movie.

#### Overview

Track atoms have an atom type value of `'trak'`. The track atom requires a track header atom (`'tkhd'`) and a media atom (`'mdia'`). Other child atoms are optional, and may include a track clipping atom (`'clip'`), a track matte atom (`'matt'`), an edit atom (`'edts'`), a track reference atom (`'tref'`), a track load settings atom (`'load'`), a track input map atom (`'imap'`), and a user data atom (`'udta'`).

> **Note**: The track atom layout contains an optional track profile atom `‘prfl’`. Track profile atoms are deprecated in the current version of QuickTime but may be present in existing QuickTime files. The inclusion here documents existing content containing profile atoms, they should not be used for new development.

The track atom layout contains an optional track profile atom `‘prfl’`. Track profile atoms are deprecated in the current version of QuickTime but may be present in existing QuickTime files. The inclusion here documents existing content containing profile atoms, they should not be used for new development.

The layout of a track atom is as follows.

| Data | Type |
| --- | --- |
| [`Size`](track_atom/size.md) | 4 bytes |
| [`Type`](track_atom/type.md) | 4 bytes |
| [`Track profile atom`](track_atom/track_profile_atom.md) | `'prfl'` |
| [`Track header atom`](track_atom/track_header_atom.md) | `'tkhd'` |
| [`Track aperture mode dimensions atom`](track_atom/track_aperture_mode_dimensions_atom.md) | `'tapt'` |
| [`Clipping atom`](track_atom/clipping_atom.md) | `'clip'` |
| [`Track matte atom`](track_atom/track_matte_atom.md) | `'matt'` |
| [`Edit atom`](track_atom/edit_atom.md) | `'edts'` |
| [`Track reference atom`](track_atom/track_reference_atom.md) | `'tref'` |
| [`Track exclude from autoselection atom`](track_atom/track_exclude_from_autoselection_atom.md) | `'txas'` |
| [`Track load settings atom`](track_atom/track_load_settings_atom.md) | `'load'` |
| [`Track input map atom`](track_atom/track_input_map_atom.md) | `'imap'` |
| [`Media atom`](track_atom/media_atom.md) | `'mdia'` |
| [`User-defined data atom`](track_atom/user-defined_data_atom.md) | `'udta'` |

## Topics

### Data fields
- [Size](track_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this track atom.
- [Type](track_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Track profile atom](track_atom/track_profile_atom.md)
  A child atom of movie atoms or track atoms.
- [Track header atom](track_atom/track_header_atom.md)
  An atom that specifies the characteristics of a single track within a movie.
- [Track aperture mode dimensions atom](track_atom/track_aperture_mode_dimensions_atom.md)
  A container atom that stores information for video correction in the form of three required atoms.
- [Clipping atom](track_atom/clipping_atom.md)
  An atom that specifies the clipping regions for movies and for tracks.
- [Track matte atom](track_atom/track_matte_atom.md)
  An atom you use to visually blend the track’s image when it is displayed.
- [Edit atom](track_atom/edit_atom.md)
  An atom that defines the portions of the media that are to be used to build up a track for a movie.
- [Track reference atom](track_atom/track_reference_atom.md)
  An atom that defines relationships between tracks.
- [Track exclude from autoselection atom](track_atom/track_exclude_from_autoselection_atom.md)
  An atom that indicates not to automatically select this track.
- [Track load settings atom](track_atom/track_load_settings_atom.md)
  An atom that indicates how the track is to be used in its movie.
- [Track input map atom](track_atom/track_input_map_atom.md)
  An atom that defines how data being sent to this track from its nonprimary sources is to be interpreted.
- [Media atom](track_atom/media_atom.md)
  An atom that describes and defines a track’s media type and sample data.
- [User-defined data atom](track_atom/user-defined_data_atom.md)
  An atom you use to define and store data associated with a QuickTime object.

## See Also

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
- [Track load settings atom ('load')](track_load_settings_atom.md)
  An atom that indicates how the track is to be used in its movie.
- [Track reference atoms](track_reference_atoms.md)
  Atoms that defines relationships between tracks.
- [Track input map atoms](track_input_map_atoms.md)
  Atoms that define how data being sent to this track from its nonprimary sources is to be interpreted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_atom)*
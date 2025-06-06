# Compressed matte atom ('kmat')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies the image description structure and the matte data associated with a particular matte atom.

#### Overview

The compressed matte atom specifies the image description structure and the matte data associated with a particular matte atom. Compressed matte atoms have an atom type value of `'kmat'`.

The layout of the compressed matte atom is as follows.

| Compressed matte atom | Bytes |
| --- | --- |
| [`Size`](compressed_matte_atom/size.md) | 4 |
| [`Type`](compressed_matte_atom/type.md) | 4 |
| [`Version`](compressed_matte_atom/version.md) | 1 |
| [`Flags`](compressed_matte_atom/flags.md) | 3 |
| [`Matte image description structure`](compressed_matte_atom/matte_image_description_structure.md) | Variable |
| [`Matte data`](compressed_matte_atom/matte_data.md) | Variable |

## Topics

### Data fields
- [Size](compressed_matte_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this compressed matte atom.
- [Type](compressed_matte_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](compressed_matte_atom/version.md)
  A 1-byte specification of the version of this compressed matte atom.
- [Flags](compressed_matte_atom/flags.md)
  Three bytes of space for flags.
- [Matte image description structure](compressed_matte_atom/matte_image_description_structure.md)
  An image description structure associated with this matte data.
- [Matte data](compressed_matte_atom/matte_data.md)
  The compressed matte data, which is of variable length.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/compressed_matte_atom)*
# Edit list atom ('elst')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that maps from a time in a movie to a time in a media, and ultimately to media data.

## Mentions

- [Representing encoder delay explicitly](example_representing_encoder_delay_explicitly.md)
- [Historical solution for implicit encoder delay](historical_solution_implicit_encoder_delay.md)

#### Overview

You use the edit list atom to map from a time in a movie to a time in a media, and ultimately to media data. This information is in the form of entries in an edit list table. Edit list atoms have an atom type value of `'elst'`.

## Topics

### Data fields
- [Size](edit_list_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this edit list atom.
- [Type](edit_list_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](edit_list_atom/version.md)
  A 1-byte specification of the version of this edit list atom.
- [Flags](edit_list_atom/flags.md)
  Three bytes of space for flags.
- [Number of entries](edit_list_atom/number_of_entries.md)
  A 32-bit integer that specifies the number of entries in the edit list atom.
- [Edit list table](edit_list_atom/edit_list_table.md)
  An array of 32-bit values, grouped into entries containing 3 values each.

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
- [Playing with edit lists](playing_with_edit_lists.md)
  Repeat a segment of a movie without copying media with edit lists.
- [Track load settings atom ('load')](track_load_settings_atom.md)
  An atom that indicates how the track is to be used in its movie.
- [Track reference atoms](track_reference_atoms.md)
  Atoms that defines relationships between tracks.
- [Track input map atoms](track_input_map_atoms.md)
  Atoms that define how data being sent to this track from its nonprimary sources is to be interpreted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/edit_list_atom)*
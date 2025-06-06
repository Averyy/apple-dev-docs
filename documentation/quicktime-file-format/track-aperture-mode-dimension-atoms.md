# Track aperture mode dimension atoms

**Framework**: Quicktime File Format

Atoms that store information for each of the track aperture presentation modes.

#### Overview

A video track in a QuickTime Movie can signal clean aperture and pixel aspect ratio information through image description extensions. The clean aperture defines the part of the encoded pixels to be displayed. The pixel aspect ratio is the aspect ratio of the encoded pixels. Conceptually the encoded pixels are decompressed, stretched (or shrunk) based on the pixel aspect ratio, and extra pixels are cropped off according to the clean aperture.

> **Note**: QuickTime tracks define simple dimensions for their content in the track header dimensions. In the absence of a track aperture mode dimensions atom, the dimensions in the track header are used for all modes.

Considering this context, the dimensions recorded in the image description define the dimensions of the encoded pixels (encoded dimensions). What’s actually displayed is a result of applying the pixel aspect ratio and the clean aperture (display dimensions).

Although the result of applying the clean aperture and the pixel aspect ratio is what is intended for final display, there are cases where it is useful to display all the pixels that exist in the content for various different purposes. Readers parsing QuickTime movies require information allowing these different display modes in order to provide this flexibility:

The information for each of these presentation modes are represented in the optional track aperture mode dimensions atoms.

> **Note**: Older applications built prior to QuickTime 7 will continue to use the dimension values stored in the track header.

## Topics

### Track aperture mode dimension atoms
- [Track aperture mode dimensions atom ('tapt')](track_aperture_mode_dimensions_atom.md)
  A container atom that stores information for video correction in the form of three required atoms.
- [Track clean aperture dimensions atom ('clef')](track_clean_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s clean aperture.
- [Track production aperture dimensions atom ('prof')](track_production_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s production aperture.
- [Track encoded pixels dimensions atom ('enof')](track_encoded_pixels_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s encoded pixels.

## See Also

- [Track atom ('trak')](track_atom.md)
  An atom that defines a single track of a movie.
- [Track header atom ('tkhd')](track_header_atom.md)
  An atom that specifies the characteristics of a single track within a movie.
- [Track exclude from autoselection atom ('txas')](track_exclude_from_autoselection_atom.md)
  An atom that indicates not to automatically select this track.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_aperture_mode_dimension_atoms)*
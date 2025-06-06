# Track clean aperture dimensions atom ('clef')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that carries the pixel dimensions of the track’s clean aperture.

#### Overview

The type of the track clean aperture dimensions atom is `‘clef’`.

The layout of a track clean aperture dimensions atom is as follows.

| Data field | Bytes |
| --- | --- |
| [`Size`](track_clean_aperture_dimensions_atom/size.md) | 4 |
| [`Type`](track_clean_aperture_dimensions_atom/type.md) | 4 |
| [`Version`](track_clean_aperture_dimensions_atom/version.md) | 1 |
| [`Flags`](track_clean_aperture_dimensions_atom/flags.md) | 3 |
| [`Width`](track_clean_aperture_dimensions_atom/width.md) | 4 |
| [`Height`](track_clean_aperture_dimensions_atom/height.md) | 4 |

## Topics

### Data fields
- [Size](track_clean_aperture_dimensions_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](track_clean_aperture_dimensions_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](track_clean_aperture_dimensions_atom/version.md)
  A 1-byte specification of the version of this atom.
- [Flags](track_clean_aperture_dimensions_atom/flags.md)
  Three bytes that are reserved for the atom flags.
- [Width](track_clean_aperture_dimensions_atom/width.md)
  A 32-bit fixed-point number that specifies the width of the track clean aperture in pixels.
- [Height](track_clean_aperture_dimensions_atom/height.md)
  A 32-bit fixed-point number that specifies the height of the track clean aperture in pixels.

## See Also

- [Track aperture mode dimensions atom ('tapt')](track_aperture_mode_dimensions_atom.md)
  A container atom that stores information for video correction in the form of three required atoms.
- [Track production aperture dimensions atom ('prof')](track_production_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s production aperture.
- [Track encoded pixels dimensions atom ('enof')](track_encoded_pixels_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s encoded pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_clean_aperture_dimensions_atom)*
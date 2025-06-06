# Track encoded pixels dimensions atom ('enof')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that carries the pixel dimensions of the track’s encoded pixels.

#### Overview

The type of the track encoded pixels dimensions atom is `‘enof’`.

The layout of a track encoded pixels dimensions atom is as follows.

| Data field | Bytes |
| --- | --- |
| [`Size`](track_encoded_pixels_dimensions_atom/size.md) | 4 |
| [`Type`](track_encoded_pixels_dimensions_atom/type.md) | 4 |
| [`Version`](track_encoded_pixels_dimensions_atom/version.md) | 1 |
| [`Flags`](track_encoded_pixels_dimensions_atom/flags.md) | 3 |
| [`Width`](track_encoded_pixels_dimensions_atom/width.md) | 4 |
| [`Height`](track_encoded_pixels_dimensions_atom/height.md) | 4 |

## Topics

### Data fields
- [Size](track_encoded_pixels_dimensions_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](track_encoded_pixels_dimensions_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](track_encoded_pixels_dimensions_atom/version.md)
  A 1-byte specification of the version of this atom.
- [Flags](track_encoded_pixels_dimensions_atom/flags.md)
  Three bytes that are reserved for the atom flags.
- [Width](track_encoded_pixels_dimensions_atom/width.md)
  A 32-bit fixed-point number that specifies the width of the track encoded pixels dimensions in pixels.
- [Height](track_encoded_pixels_dimensions_atom/height.md)
  A 32-bit fixed-point number that specifies the height of the track encoded pixels dimensions in pixels.

## See Also

- [Track aperture mode dimensions atom ('tapt')](track_aperture_mode_dimensions_atom.md)
  A container atom that stores information for video correction in the form of three required atoms.
- [Track clean aperture dimensions atom ('clef')](track_clean_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s clean aperture.
- [Track production aperture dimensions atom ('prof')](track_production_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s production aperture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_encoded_pixels_dimensions_atom)*
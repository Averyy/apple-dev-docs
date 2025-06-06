# Track aperture mode dimensions atom ('tapt')

**Framework**: QuickTime File Format  
**Kind**: class

A container atom that stores information for video correction in the form of three required atoms.

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

This atom is optionally included in the track atom. The type of the track aperture mode dimensions atom is `‘tapt’`.

The layout of a track aperture mode dimensions atom is as follows.

| Data | Type |
| --- | --- |
| [`Size`](track_aperture_mode_dimensions_atom/size.md) | 4 bytes |
| [`Type`](track_aperture_mode_dimensions_atom/type.md) = `'tapt'` | 4 bytes |
| [`Track clean aperture dimensions atom`](track_aperture_mode_dimensions_atom/track_clean_aperture_dimensions_atom.md) | `'clef'` |
| [`Track production aperture dimensions atom`](track_aperture_mode_dimensions_atom/track_production_aperture_dimensions_atom.md) | `'prof'` |
| [`Track encoded pixels dimensions atom`](track_aperture_mode_dimensions_atom/track_encoded_pixels_dimensions_atom.md) | `'enof'` |

## Topics

### Data fields
- [Size](track_aperture_mode_dimensions_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the track aperture mode dimensions atom.
- [Type](track_aperture_mode_dimensions_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Track clean aperture dimensions atom](track_aperture_mode_dimensions_atom/track_clean_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s clean aperture.
- [Track production aperture dimensions atom](track_aperture_mode_dimensions_atom/track_production_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s production aperture.
- [Track encoded pixels dimensions atom](track_aperture_mode_dimensions_atom/track_encoded_pixels_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s encoded pixels.

## See Also

- [Track clean aperture dimensions atom ('clef')](track_clean_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s clean aperture.
- [Track production aperture dimensions atom ('prof')](track_production_aperture_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s production aperture.
- [Track encoded pixels dimensions atom ('enof')](track_encoded_pixels_dimensions_atom.md)
  An atom that carries the pixel dimensions of the track’s encoded pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_aperture_mode_dimensions_atom)*
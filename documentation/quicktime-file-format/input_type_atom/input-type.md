# Input type

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit integer that specifies the type of data that is to be received from the secondary data source.

#### Overview

Valid values for this field are as follows.

| Input identifier | Value | Description |
| --- | --- | --- |
| `kTrackModifierTypeMatrix` | 1 | A 3 × 3 transformation matrix to transform the track’s location, scaling, and so on. |
| `kTrackModifierTypeClip` | 2 | A QuickDraw clipping region to change the track’s shape. |
| `kTrackModifierTypeVolume` | 3 | An 8.8 fixed-point value indicating the relative sound volume. This is used for fading the volume. |
| `kTrackModifierTypeBalance` | 4 | A 16-bit integer indicating the sound balance level. This is used for panning the sound location. |
| `kTrackModifierTypeGraphicsMode` | 5 | A graphics mode record (32-bit integer indicating graphics mode, followed by an RGB color) to modify the track’s graphics mode for visual fades. |
| `kTrackModifierObjectMatrix` | 6 | A 3 × 3 transformation matrix to transform an object within the track’s location, scaling, and so on. |
| `kTrackModifierObjectGraphicsMode` | 7 | A graphics mode record (32-bit integer indicating graphics mode, followed by an RGB color) to modify an object within the track’s graphics mode for visual fades. |
| `kTrackModifierTypeImage` | `'vide’` | Compressed image data for an object within the track. Note that this was `kTrackModifierTypeSpriteImage`. |

## See Also

- [Size](input_type_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this input type atom.
- [Type](input_type_atom/type.md)
  A 32-bit integer that identifies the atom type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/input_type_atom/input_type)*
# kTweenRegionData

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains the data for a QuickDraw region.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

Used only by a `kTweenTypeQDRegion` atom.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenRegionData` or `kTweenPictureData` atom. The ID of this atom is always `1`. The index of this atom is always `1`.

This atom is a leaf atom. The data type of its data is `Region`.

Either a `kTweenPictureData` or `kTweenRegionData` atom is required for a `kTweenTypeQDRegion` tween.

## See Also

- [kTweenPictureData](ktweenpicturedata.md)
  An atom that contains the data for a QuickDraw picture.
- [kTweenSequenceElement](ktweensequenceelement.md)
  An atom that specifies an entry in a tween sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweenregiondata)*
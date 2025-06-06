# kTweenPictureData

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains the data for a QuickDraw picture.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

Used only by a `kTweenTypeQDRegion` atom.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenPictureData` or `kTweenRegionData` atom. The ID of this atom is always `1`. The index of this atom is always `1`.

This atom is a leaf atom. The data type of its data is `Picture`.

Either a `kTweenPictureData` or `kTweenRegionData` atom is required for a `kTweenTypeQDRegion` atom.

## See Also

- [kTweenRegionData](ktweenregiondata.md)
  An atom that contains the data for a QuickDraw region.
- [kTweenSequenceElement](ktweensequenceelement.md)
  An atom that specifies an entry in a tween sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweenpicturedata)*
# kTweenPictureData

**Framework**: QuickTime File Format  
**Kind**: class  
**Role**: Atom

An atom that contains the data for a QuickDraw picture.

> **Deprecated**: Tween media is deprecated in the QuickTime file format. The information that follows documents existing content containing tween media and should not be used for new development.

## Overview

Used only by a `kTweenTypeQDRegion` atom.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenPictureData` or `kTweenRegionData` atom. The ID of this atom is always `1`. The index of this atom is always `1`.

This atom is a leaf atom. The data type of its data is `Picture`.

Either a `kTweenPictureData` or `kTweenRegionData` atom is required for a `kTweenTypeQDRegion` atom.

## See Also

### Region Tween Atoms
- [kTweenRegionData](./ktweenregiondata.md)
  An atom that contains the data for a QuickDraw region.
- [kTweenSequenceElement](./ktweensequenceelement.md)
  An atom that specifies an entry in a tween sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweenpicturedata)*
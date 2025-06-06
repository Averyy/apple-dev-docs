# kTweenSequenceElement

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies an entry in a tween sequence.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

Its parent is the tween QT atom container (which you specify with the constant `kParentAtomIsContainer`).

The ID of a `kTweenSequenceElement` atom must be unique among the `kTweenSequenceElement` atoms in the same QT atom container. The index of a `kTweenSequenceElement` atom specifies its order in the sequence; the first entry in the sequence has the index `1`, the second `2`, and so on.

This atom is a leaf atom. The data type of its data is `TweenSequenceEntryRecord`, a data structure that contains the following fields:

## See Also

- [kTweenPictureData](ktweenpicturedata.md)
  An atom that contains the data for a QuickDraw picture.
- [kTweenRegionData](ktweenregiondata.md)
  An atom that contains the data for a QuickDraw region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweensequenceelement)*
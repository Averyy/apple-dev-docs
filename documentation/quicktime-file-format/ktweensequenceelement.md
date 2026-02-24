# kTweenSequenceElement

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies an entry in a tween sequence.

#### Overview

Its parent is the tween QT atom container (which you specify with the constant `kParentAtomIsContainer`).

The ID of a `kTweenSequenceElement` atom must be unique among the `kTweenSequenceElement` atoms in the same QT atom container. The index of a `kTweenSequenceElement` atom specifies its order in the sequence; the first entry in the sequence has the index `1`, the second `2`, and so on.

This atom is a leaf atom. The data type of its data is `TweenSequenceEntryRecord`, a data structure that contains the following fields:

- **endPercent**: A value of type Fixed that specifies the point in the duration of the tween media sample at which the sequence entry ends. This is expressed as a percentage; for example, if the value is `75.0`, the sequence entry ends after three-quarters of the total duration of the tween media sample have elapsed. The sequence entry begins after the end of the previous sequence entry or, for the first entry in the sequence, at the beginning of the tween media sample.
- **tweenAtomID**: A value of type `QTAtomID` that specifies the `kTweenEntry` atom containing the tween for the sequence element. The `kTweenEntry` atom and the `kTweenSequenceElement` atom must both be a child atoms of the same tween QT atom container.
- **dataAtomID**: A value of type `QTAtomID` that specifies the `kTweenData` atom containing the data for the tween. This atom must be a child atom of the atom specified by the `tweenAtomID` field.

## See Also

- [kTweenPictureData](ktweenpicturedata.md)
  An atom that contains the data for a QuickDraw picture.
- [kTweenRegionData](ktweenregiondata.md)
  An atom that contains the data for a QuickDraw region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweensequenceelement)*
# kTweenStartOffset

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies a time offset from the start of the tween media sample to the start of the tween atom.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

For a tween atom in a tween track of a QuickTime movie, specifies a time offset from the start of the tween media sample to the start of the tween atom. The time units are the units used for the tween track.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenStartOffset` atom. The ID of this atom is always `1`. The index of this atom is always `1`.

This atom is a leaf atom. The data type of its data is `TimeValue`.

This atom is optional. If it is not included, the tween operation begins at the start of the tween media sample.

## See Also

- [kTweenEntry](ktweenentry.md)
  A tween atom, which can be either a single tween atom, a tween atom in a tween sequence, or an interpolation tween atom.
- [kTweenDuration](ktweenduration.md)
  An atom that specifies the duration of a tween operation.
- [kTweenData](ktweendata.md)
  An atom that contains data for a tween atom.
- [kNameAtom](knameatom.md)
  An atom that specifies the name of a tween atom.
- [kTweenType](ktweentype.md)
  An atom that specifies the tween type, which is the data type of the data for the tween operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweenstartoffset)*
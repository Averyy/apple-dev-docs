# kTweenInterpolationID

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies an interpolation tween atom to use for a specified tween data atom.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

Specifies an interpolation tween atom to use for a specified `kTweenData` atom. There can be any number of `kTweenInterpolationID` atoms for a tween atom, one for each `kTweenData` atom to be interpolated.

Its parent atom is a `kTweenEntry` atom.

The index of a `kTweenInterpolationID` atom specifies when it was added to the `kTweenEntry` atom; the first added has the index `1`, the second `2`, and so on. The ID of a `kTweenInterpolationID` atom must match the atom ID of the `kTweenData` atom to be interpolated, and be unique among the `kTweenInterpolationID` atoms contained in the same `kTweenEntry` atom.

This atom is a leaf atom. The data type of its data is `QTAtomID`.

This atom is required for an interpolation tween atom.

## See Also

- [kTweenOutputMax](ktweenoutputmax.md)
  An atom that specifies the maximum output value of an interpolation tween atom.
- [kTweenOutputMin](ktweenoutputmin.md)
  An atom that specifies the minimum output value of an interpolation tween atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweeninterpolationid)*
# kTweenOutputMin

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies the minimum output value of an interpolation tween atom.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

If both `kTweenOutputMin` and `kTweenOutputMax` atoms are included for an interpolation tween atom, output values for the tween atom are scaled to be within the minimum and maximum values. For example, if an interpolation tween atom has values between `0` and `4`, and it has `kTweenOutputMin` and `kTweenOutputMax` atoms with values `1` and `2`, respectively, a value of `0` (the minimum value before scaling) is scaled to `1` (the minimum specified by the `kTweenOutputMin` atom), a value of `4` (the maximum value before scaling) is scaled to `2` (the maximum specified by the `kTweenOutputMax` atom), and a value of `3` (three-quarters of the way between the maximum and minimum values before scaling) is scaled to `1.75` (three-quarters of the way between the values of the `kTweenOutputMin` and `kTweenOutputMax` atoms).

If a `kTweenOutputMin` atom is included but a `kTweenOutputMax` atom is not, QuickTime does not scale interpolation tween values.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenOutputMin` atom. The ID of this atom is always `1`. The index of this atom is always `1`.

This atom is a leaf atom. The data type of its data is `Fixed`.

This atom is optional. If it is not included but a `kTweenOutputMax` atom is, the tween component uses `0` as the minimum value for scaling values of an interpolation tween atom.

## See Also

- [kTweenOutputMax](ktweenoutputmax.md)
  An atom that specifies the maximum output value of an interpolation tween atom.
- [kTweenInterpolationID](ktweeninterpolationid.md)
  An atom that specifies an interpolation tween atom to use for a specified tween data atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweenoutputmin)*
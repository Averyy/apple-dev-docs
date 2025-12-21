# kTweenEntry

**Framework**: QuickTime File Format  
**Kind**: class

A tween atom, which can be either a single tween atom, a tween atom in a tween sequence, or an interpolation tween atom.

#### Overview

Its parent is the tween QT atom container (which you specify with the constant `kParentAtomIsContainer`).

The index of a `kTweenEntry` atom specifies when it was added to the QT atom container; the first added has the index `1`, the second `2`, and so on. The ID of a `kTweenEntry` atom can be any ID that is unique among the `kTweenEntry` atoms contained in the same QuickTime atom container.

This atom is a parent atom. It must contain the following child atoms:

- A `kTweenType` atom that specifies the tween type.
- One or more `kTweenData` atoms that contain the data for the tween atom. Each `kTweenData` atom can contain different data to be processed by the tween component, and a tween component can process data from only one `kTweenData` atom a time. For example, an application can use a list tween to animate sprites. The `kTweenEntry` atom for the tween atom could contain three sets of animation data, one for moving the sprite from left to right, one for moving the sprite from right to left, and one for moving the sprite from top to bottom. In this case, the `kTweenEntry` atom for the tween atom would contain three `kTweenData` atoms, one for each data set. The application specifies the desired data set by specifying the ID of the `kTweenData` atom to use.

A `kTweenEntry` atom can contain any of the following optional child atoms:

- A `kTweenStartOffset` atom that specifies a time interval, beginning at the start of the tween media sample, after which the tween operation begins. If this atom is not included, the tween operation begins at the start of the tween media sample.
- A `kTweenDuration` atom that specifies the duration of the tween operation. If this atom is not included, the duration of the tween operation is the duration of the media sample that contains it.

If a `kTweenEntry` atom specifies a path tween, it can contain the following optional child atom:

- A kTweenFlags atom containing flags that control the tween operation. If this atom is not included, no flags are set. Note that interpolation tween tracks are tween tracks that modify other tween tracks. The output of an interpolation tween track must be a time value, and the time values generated are used in place of the input time values of the tween track being modified.

If a `kTweenEntry` atom specifies an interpolation tween track, it must contain the following child atoms:

- A `kTweenInterpolationID` atom for each `kTweenData` atom to be interpolated. The ID of each `kTweenInterpolationID` atom must match the ID of the `kTweenData` atom to be interpolated. The data for a `kTweenInterpolationID` atom specifies a `kTweenEntry` atom that contains the interpolation tween track to use for the `kTweenData` atom.

If this atom specifies an interpolation tween track, it can contain either of the following optional child atoms:

- A `kTweenOutputMin` atom that specifies the minimum output value of the interpolation tween atom. The value of this atom is used only if there is also a `kTweenOutputMax` atom with the same parent. If this atom is not included and there is a `kTweenOutputMax` atom with the same parent, the tween component uses 0 as the minimum value when scaling output values of the interpolation tween track.
- A `kTweenOutputMax` atom that specifies the maximum output value of the interpolation tween atom. If this atom is not included, the tween component does not scale the output values of the interpolation tween track.

## See Also

- [kTweenStartOffset](ktweenstartoffset.md)
  An atom that specifies a time offset from the start of the tween media sample to the start of the tween atom.
- [kTweenDuration](ktweenduration.md)
  An atom that specifies the duration of a tween operation.
- [kTweenData](ktweendata.md)
  An atom that contains data for a tween atom.
- [kNameAtom](knameatom.md)
  An atom that specifies the name of a tween atom.
- [kTweenType](ktweentype.md)
  An atom that specifies the tween type, which is the data type of the data for the tween operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweenentry)*
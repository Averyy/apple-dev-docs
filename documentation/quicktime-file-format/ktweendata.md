# kTweenData

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains data for a tween atom.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain any number of `kTweenData` atoms.

The index of a `kTweenData` atom specifies when it was added to the `kTweenEntry` atom; the first added has the index `1`, the second `2`, and so on. The ID of a `kTweenData` atom can be any ID that is unique among the `kTweenData` atoms contained in the same `kTweenEntry` atom.

At least one `kTweenData` atom is required in a `kTweenEntry` atom.

For single tween atoms, a `kTweenData` atom is a leaf atom. It can contain data of any type.

For polygon tween atoms, a `kTweenData` atom is a leaf atom. The data type of its data is `Fixed[27]`, which specifies three polygons.

For path tweens, a `kTweenData` atom is a leaf atom. The data type of its data is `Handle`, which contains a QuickTime vector.

In interpolation tween atoms, a `kTweenData` atom is a leaf atom. It can contain data of any type. An interpolation tween atom can be any tween atoms other than a list tween atom that returns a time value.

In list tween atoms, a `kTweenData` atom is a parent atom that must contain the following child atoms:

- A kListElementType atom that specifies the atom type of the elements of the tween atom.
- One or more leaf atoms of the type specified by the `kListElementType` atom. The data for each atom is the result of a list tween operation.

## See Also

- [kTweenEntry](ktweenentry.md)
  A tween atom, which can be either a single tween atom, a tween atom in a tween sequence, or an interpolation tween atom.
- [kTweenStartOffset](ktweenstartoffset.md)
  An atom that specifies a time offset from the start of the tween media sample to the start of the tween atom.
- [kTweenDuration](ktweenduration.md)
  An atom that specifies the duration of a tween operation.
- [kNameAtom](knameatom.md)
  An atom that specifies the name of a tween atom.
- [kTweenType](ktweentype.md)
  An atom that specifies the tween type, which is the data type of the data for the tween operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktweendata)*
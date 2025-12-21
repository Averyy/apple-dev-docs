# kInitialRotationAtom

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies an initial angle of rotation for a path tween atom.

#### Overview

Specifies an initial angle of rotation for a path tween atom of type `kTweenTypePathToMatrixRotation`, `kTweenTypePathToMatrixTranslation`, or `kTweenTypePathToMatrixTranslationAndRotation`.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kInitialRotationAtom` atom. The ID of this atom is always `1`. The index of this atom is always `1`.

This atom is a leaf atom. Its data type is `Fixed`.

This atom is optional. If it is not included, no initial rotation of the tween atom is performed.

## See Also

- [kTweenFlags](ktweenflags.md)
  An atom that contains flags that control the tween operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/kinitialrotationatom)*
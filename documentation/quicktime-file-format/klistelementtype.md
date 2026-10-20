# kListElementType

**Framework**: QuickTime File Format  
**Kind**: class  
**Role**: Atom

An element that specifies the atom type of the elements in a list tween atom.

> **Deprecated**: Tween media is deprecated in the QuickTime file format. The information that follows documents existing content containing tween media and should not be used for new development.

#### Overview

Its parent atom is a `kTweenData` atom.

A `kTweenEntry` atom can contain only one `kListElementType` atom. The ID of this atom is always `1`. The index of this atom is always `1`.

This atom is a leaf atom. Its data type is `QTAtomType`.

This atom is required in the `kTweenData` atom for a list tween atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/klistelementtype)*
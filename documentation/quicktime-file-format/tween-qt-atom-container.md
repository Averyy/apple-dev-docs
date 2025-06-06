# Tween QT atom container

**Framework**: QuickTime File Format

Specify the characteristics of a tween with atoms in a tween QT atom container.

#### Overview

A tween QT atom container can contain the atoms described in the following sections.

## Topics

### General tween atoms
- [kTweenEntry](ktweenentry.md)
  A tween atom, which can be either a single tween atom, a tween atom in a tween sequence, or an interpolation tween atom.
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
### Path Tween Atoms
- [kTweenFlags](ktweenflags.md)
  An atom that contains flags that control the tween operation.
- [kInitialRotationAtom](kinitialrotationatom.md)
  An atom that specifies an initial angle of rotation for a path tween atom.
### List Tween Atoms
- [kListElementType](klistelementtype.md)
  An element that specifies the atom type of the elements in a list tween atom.
### 3D Tween Atoms
- [kTween3dInitialCondition](ktween3dinitialcondition.md)
  An atom that specifies an initial transform for a 3D tween atom.
### Interpolation Tween Atoms
- [kTweenOutputMax](ktweenoutputmax.md)
  An atom that specifies the maximum output value of an interpolation tween atom.
- [kTweenOutputMin](ktweenoutputmin.md)
  An atom that specifies the minimum output value of an interpolation tween atom.
- [kTweenInterpolationID](ktweeninterpolationid.md)
  An atom that specifies an interpolation tween atom to use for a specified tween data atom.
### Region Tween Atoms
- [kTweenPictureData](ktweenpicturedata.md)
  An atom that contains the data for a QuickDraw picture.
- [kTweenRegionData](ktweenregiondata.md)
  An atom that contains the data for a QuickDraw region.
- [kTweenSequenceElement](ktweensequenceelement.md)
  An atom that specifies an entry in a tween sequence.

## See Also

- [Tween sample description](tween_sample_description.md)
  An atom that contains information for converting from media time to sample number to sample location for tweens.
- [Tween sample data](tween_sample_data.md)
- [Tween type categories](tween_type_categories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/tween_qt_atom_container)*
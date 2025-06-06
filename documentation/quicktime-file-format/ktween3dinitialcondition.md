# kTween3dInitialCondition

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies an initial transform for a 3D tween atom.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

Specifies an initial transform for a 3D tween atom whose tween type is one of the following: `kTweenType3dCameraData`, `kTweenType3dMatrix`, `kTweenType3dQuaternion`, `kTweenType3dRotate`, `kTweenType3dRotateAboutAxis`, `kTweenType3dRotateAboutAxis`, `kTweenType3dRotateAboutPoint`, `kTweenType3dRotateAboutVector`, `kTweenType3dScale`, or `kTweenType3dTranslate`.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTween3dInitialCondition` atom. The ID of this atom is always `1`. The index of this atom is always `1`.

This atom is a leaf atom. The data type of its data is one of the values listed in the following table.

| Tween type | Data type |
| --- | --- |
| `kTweenType3dCameraData` | `TQ3CameraData` |
| `kTweenType3dMatrix` | `TQ3Matrix4x4` |
| `kTweenType3dQuaternion` | `TQ3Quaternion` |
| `kTweenType3dRotate` | `TQ3RotateTransformData` |
| `kTweenType3dRotateAboutAxis` | `TQ3RotateAboutAxisTransformData` |
| `kTweenType3dRotateAboutPoint` | `TQ3RotateAboutPointTransformData` |
| `kTweenType3dRotateAboutVector` | `TQ3PlaneEquation` |
| `kTweenType3dScale` | `TQ3Vector3D` |
| `kTweenType3dTranslate` | `TQ3Vector3D` |

This atom is optional. For each tween type, the default value is the data structure that specifies an identity transform, that is, a transform that does not alter the 3D data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/ktween3dinitialcondition)*
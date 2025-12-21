# kVTCompressionPropertyCameraCalibrationKey_LensAlgorithmKind

**Framework**: Video Toolbox  
**Kind**: var

The following keys are required in each kVTCompressionPropertyKey_CameraCalibrationDataLensCollection dictionary.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTCompressionPropertyCameraCalibrationKey_LensAlgorithmKind: CFString
```

#### Discussion

Specifies the camera calibration methodology.

If the algorithm kind is ParametricLens, the camera lens collection requires camera intrinsic and extrinsic parameters.

Specifies the kind of lens (e.g., color).

Specifies a unique number associated with a lens.

Specifies the particular use of the lens in the camera system (e.g., left or right for a stereo system).

For a stereoscopic camera system, one lens should have the left role and another should have the right role.

Specifies the first and second radial distortion coefficients(k1 and k2) used to correct the distortion that appeared as curved lines for straight lines and the first and second tangential distortion coefficients(p1 and p2) used to correct the distortion caused by a lens’s improper alignment of physical elements.

The values are in a CFArray of four CFNumbers in k1, k2, p1 and p2 order.

Specifies a three element polynomial for mapping x axis UV parameters with an adjustment using the equation `x' = polynomialX[0] + polynomialX[1]*x + polynomialX[2]*x^3`.

The values are in a CFArray of three CFNumbers(float) in the order polynomialX[0], polynomialX[1] & polynomialX[2]. The polynomial transform origin is at the center of the frame. The default values of elements of polynomialX[] are [0.0, 1.0, 0.0].

Specifies a three element polynomial for mapping y axis UV parameters with an adjustment using the equation `y' = polynomialY[0] + polynomialY[1]*y + polynomialY[2]*y^3`.

The values are in a CFArray of three CFNumbers(float) in the order polynomialY[0], polynomialY[1] & polynomialY[2]. The polynomial transform origin is at the center of the frame. The default values of elements of polynomialY[] are [0.0, 1.0, 0.0].

Specifies the outer limit of the calibration validity in degrees of angle eccentric from the optical axis.

The value is linked to radial distortion corrections with k1 and k2.

Specifies the 3x3 camera intrinsic matrix for camera calibration.

Camera intrinsic matrix is a CFData containing a matrix_float3x3, which is column-major. Each element is in IEEE754 native-endian 32-bit floating point. It has the following contents: fx	s	cx 0	fy	cy 0	0	1 fx and fy are the focal length in pixels. For square pixels, they will have the same value. cx and cy are the coordinates of the principal point. The origin is the upper left of the frame. s is an optional skew factor.

Specifies the offset of the point of perspective relative to the rectilinear projection.

Specifies the image dimensions to which the camera’s intrinsic matrix values are relative.

Values are width and height in a CFDictionary. Dictionary keys are compatible with CGSize dictionary, namely “Width” and “Height”.

Identifies how the origin of the camera system’s extrinsics are determined.

The ‘blin’ value indicates the center of transform is determined by the point mid way along the dimensions indicated by the StereoCameraSystemBaselineBox held in the StereoCameraSystemBox. Each left and right lens within a stereoscopic camera system is equidistant from this point, so the ‘blin’ value is halved when associated with the respective left and right lenses.

Specifies a camera’s orientation to a world or scene coordinate system. The orientation value is a unit quaternion(ix, iy, and iz) instead of the classical 3x3 matrix.

The values are in a CFArray of three CFNumbers in ix, iy, and iz order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertycameracalibrationkey_lensalgorithmkind)*
# kVTCompressionPropertyCameraCalibrationKey_LensAlgorithmKind

**Framework**: Video Toolbox  
**Kind**: var

The following keys are required in each kVTCompressionPropertyKey_CameraCalibrationDataLensCollection dictionary.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let kVTCompressionPropertyCameraCalibrationKey_LensAlgorithmKind: CFString
```

#### Discussion

If the algorithm kind is ParametricLens, the camera lens collection requires camera intrinsic and extrinsic parameters.

For a stereoscopic camera system, one lens should have the left role and another should have the right role.

The values are in a CFArray of four CFNumbers in k1, k2, p1 and p2 order.

The values are in a CFArray of three CFNumbers(float) in the order polynomialX[0], polynomialX[1] & polynomialX[2]. The polynomial transform origin is at the center of the frame. The default values of elements of polynomialX[] are [0.0, 1.0, 0.0].

The values are in a CFArray of three CFNumbers(float) in the order polynomialY[0], polynomialY[1] & polynomialY[2]. The polynomial transform origin is at the center of the frame. The default values of elements of polynomialY[] are [0.0, 1.0, 0.0].

The value is linked to radial distortion corrections with k1 and k2.

Camera intrinsic matrix is a CFData containing a matrix_float3x3, which is column-major. Each element is in IEEE754 native-endian 32-bit floating point. It has the following contents: fx	s	cx 0	fy	cy 0	0	1 fx and fy are the focal length in pixels. For square pixels, they will have the same value. cx and cy are the coordinates of the principal point. The origin is the upper left of the frame. s is an optional skew factor.

Values are width and height in a CFDictionary. Dictionary keys are compatible with CGSize dictionary, namely “Width” and “Height”.

The ‘blin’ value indicates the center of transform is determined by the point mid way along the dimensions indicated by the StereoCameraSystemBaselineBox held in the StereoCameraSystemBox. Each left and right lens within a stereoscopic camera system is equidistant from this point, so the ‘blin’ value is halved when associated with the respective left and right lenses.

The values are in a CFArray of three CFNumbers in ix, iy, and iz order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertycameracalibrationkey_lensalgorithmkind)*
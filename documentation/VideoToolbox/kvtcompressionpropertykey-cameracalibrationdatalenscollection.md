# kVTCompressionPropertyKey_CameraCalibrationDataLensCollection

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTCompressionPropertyKey_CameraCalibrationDataLensCollection: CFString
```

#### Discussion

Specifies intrinsic and extrinsic parameters for single or multiple lenses.

The property value is an array of dictionaries describing the camera calibration data for each lens. The camera calibration data includes intrinsics and extrinics with other parameters. For a stereoscopic camera system, the left and right lens signaling can be done with the kVTCompressionPropertyCameraCalibrationKey_LensRole key and its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_cameracalibrationdatalenscollection)*
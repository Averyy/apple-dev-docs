# kVTCompressionPropertyKey_CameraCalibrationDataLensCollection

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let kVTCompressionPropertyKey_CameraCalibrationDataLensCollection: CFString
```

#### Discussion

The property value is an array of dictionaries describing the camera calibration data for each lens. The camera calibration data includes intrinsics and extrinics with other parameters. For a stereoscopic camera system, the left and right lens signaling can be done with the kVTCompressionPropertyCameraCalibrationKey_LensRole key and its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_cameracalibrationdatalenscollection)*
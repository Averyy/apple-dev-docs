# CIDetectorTypeFace

**Framework**: Core Image  
**Kind**: data

A detector that searches for faces in a still image or video, returning [`CIFaceFeature`](cifacefeature.md) objects that provide information about detected faces.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorTypeFace: String
```

#### Discussion

For better accuracy and performance in face detection, use the [`CIDetectorImageOrientation`](cidetectorimageorientation.md) key to specify the image orientation when using the [`features(in:options:)`](cidetector/1438189-features.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectortypeface)*
# CIFaceFeature

**Framework**: Core Image  
**Kind**: class

Information about a face detected in a still or video image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIFaceFeature
```

#### Overview

> **Note**:  In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/Vision) framework replaces these classes for identifying and analyzing image features. See [`VNDetectFaceRectanglesRequest`](https://developer.apple.com/documentation/Vision/VNDetectFaceRectanglesRequest).

The properties of a `CIFaceFeature` object provide information about the face’s eyes and mouth. A face object in a video can also have properties that track its location over time, tracking ID and frame count.

## Topics

### Locating Faces
- [var bounds: CGRect](cifacefeature/bounds-swift.property.md)
  A rectangle indicating the position and dimensions of the face in image coordinates.
- [var hasFaceAngle: Bool](cifacefeature/hasfaceangle-swift.property.md)
  A Boolean value that indicates whether information about face rotation is available.
- [var faceAngle: Float](cifacefeature/faceangle-swift.property.md)
  The rotation of the face.
### Identifying Facial Features
- [var hasLeftEyePosition: Bool](cifacefeature/haslefteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s left eye.
- [var hasRightEyePosition: Bool](cifacefeature/hasrighteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s right eye.
- [var hasMouthPosition: Bool](cifacefeature/hasmouthposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s mouth.
- [var leftEyePosition: CGPoint](cifacefeature/lefteyeposition-swift.property.md)
  The coordinates of the left eye, in image coordinates.
- [var rightEyePosition: CGPoint](cifacefeature/righteyeposition-swift.property.md)
  The coordinates of the right eye, in image coordinates
- [var mouthPosition: CGPoint](cifacefeature/mouthposition-swift.property.md)
  The coordinates of the mouth, in image coordinates
- [var hasSmile: Bool](cifacefeature/hassmile-swift.property.md)
  A Boolean value that indicates whether a smile is detected in the face.
- [var leftEyeClosed: Bool](cifacefeature/lefteyeclosed-swift.property.md)
  A Boolean value that indicates whether a closed left eye is detected in the face.
- [var rightEyeClosed: Bool](cifacefeature/righteyeclosed-swift.property.md)
  A Boolean value that indicates whether a closed right eye is detected in the face.
### Tracking Distinct Faces in Video
- [var hasTrackingID: Bool](cifacefeature/hastrackingid-swift.property.md)
  A Boolean value that indicates whether the face object has a tracking ID.
- [var trackingID: Int32](cifacefeature/trackingid-swift.property.md)
  The tracking identifier of the face object.
- [var hasTrackingFrameCount: Bool](cifacefeature/hastrackingframecount-swift.property.md)
  A Boolean value that indicates the face object has a tracking frame count.
- [var trackingFrameCount: Int32](cifacefeature/trackingframecount-swift.property.md)
  The tracking frame count of the face.

## Relationships

### Inherits From
- [CIFeature](cifeature.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CIDetector](cidetector.md)
  An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a region likely to contain text detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifacefeature)*
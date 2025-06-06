# CIFaceFeature

**Framework**: Coreimage  
**Kind**: cl

Information about a face detected in a still or video image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIFaceFeature : CIFeature
```

#### Overview

> **Note**: In macOS 10.13, iOS 11, and tvOS 11 or later, the [`Vision`](https://developer.apple.com/documentation/vision) framework replaces these classes for identifying and analyzing image features. See [`VNDetectFaceRectanglesRequest`](https://developer.apple.com/documentation/vision/vndetectfacerectanglesrequest).

The properties of a [`CIFaceFeature`](cifacefeature.md) object provide information about the face’s eyes and mouth. A face object in a video can also have properties that track its location over time, tracking ID and frame count.

## Topics

### Locating Faces
- [var bounds: CGRect](cifacefeature/1438068-bounds.md)
  A rectangle indicating the position and dimensions of the face in image coordinates.
- [var hasFaceAngle: Bool](cifacefeature/1438165-hasfaceangle.md)
  A Boolean value that indicates whether information about face rotation is available.
- [var faceAngle: Float](cifacefeature/1437689-faceangle.md)
  The rotation of the face.
### Identifying Facial Features
- [var hasLeftEyePosition: Bool](cifacefeature/1437900-haslefteyeposition.md)
  A Boolean value that indicates whether the detector found the face’s left eye.
- [var hasRightEyePosition: Bool](cifacefeature/1438076-hasrighteyeposition.md)
  A Boolean value that indicates whether the detector found the face’s right eye.
- [var hasMouthPosition: Bool](cifacefeature/1437976-hasmouthposition.md)
  A Boolean value that indicates whether the detector found the face’s mouth.
- [var leftEyePosition: CGPoint](cifacefeature/1437923-lefteyeposition.md)
  The coordinates of the left eye, in image coordinates.
- [var rightEyePosition: CGPoint](cifacefeature/1438213-righteyeposition.md)
  The coordinates of the right eye, in image coordinates
- [var mouthPosition: CGPoint](cifacefeature/1438020-mouthposition.md)
  The coordinates of the mouth, in image coordinates
- [var hasSmile: Bool](cifacefeature/1437882-hassmile.md)
  A Boolean value that indicates whether a smile is detected in the face.
- [var leftEyeClosed: Bool](cifacefeature/1437630-lefteyeclosed.md)
  A Boolean value that indicates whether a closed left eye is detected in the face.
- [var rightEyeClosed: Bool](cifacefeature/1437615-righteyeclosed.md)
  A Boolean value that indicates whether a closed right eye is detected in the face.
### Tracking Distinct Faces in Video
- [var hasTrackingID: Bool](cifacefeature/1437683-hastrackingid.md)
  A Boolean value that indicates whether the face object has a tracking ID.
- [var trackingID: Int32](cifacefeature/1437709-trackingid.md)
  The tracking identifier of the face object.
- [var hasTrackingFrameCount: Bool](cifacefeature/1437731-hastrackingframecount.md)
  A Boolean value that indicates the face object has a tracking frame count.
- [var trackingFrameCount: Int32](cifacefeature/1437953-trackingframecount.md)
  The tracking frame count of the face.

## Relationships

### Inherits From
- [CIFeature](cifeature.md)

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
# FaceObservation

**Framework**: Vision  
**Kind**: struct

An image-analysis request that identifies facial features in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct FaceObservation
```

## Topics

### Creating an observation
- [init(VNFaceObservation)](faceobservation/init(_:).md)
  Creates a face observation.
- [init(boundingBox: NormalizedRect, revision: DetectFaceRectanglesRequest.Revision?)](faceobservation/init(boundingbox:revision:).md)
  Creates a face observation from its bounding box.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [FaceObservation.Landmarks2D](faceobservation/landmarks2d.md)
  A collection of facial features that a request detects.
- [var landmarks: FaceObservation.Landmarks2D?](faceobservation/landmarks.md)
  The facial features of the detected face.
- [let pitch: Measurement<UnitAngle>](faceobservation/pitch.md)
  The pitch angle of a face.
- [let roll: Measurement<UnitAngle>](faceobservation/roll.md)
  The roll angle of a face.
- [let yaw: Measurement<UnitAngle>](faceobservation/yaw.md)
  The yaw angle of a face.
### Getting the capture quality
- [var captureQuality: FaceObservation.CaptureQuality?](faceobservation/capturequality-swift.property.md)
  The quality of the face capture.
- [FaceObservation.CaptureQuality](faceobservation/capturequality-swift.struct.md)
  An indicator of the quality of a face capture.

## Relationships

### Conforms To
- [BoundingBoxProviding](boundingboxproviding.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation)*
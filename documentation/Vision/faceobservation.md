# FaceObservation

**Framework**: Vision  
**Kind**: struct

An image-analysis request that identifies facial features in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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
### Structures
- [FaceObservation.CaptureQuality](faceobservation/capturequality-swift.struct.md)
  An indicator of the quality of a face capture.
### Instance Properties
- [var captureQuality: FaceObservation.CaptureQuality?](faceobservation/capturequality-swift.property.md)
  The quality of the face capture.

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

## See Also

- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation)*
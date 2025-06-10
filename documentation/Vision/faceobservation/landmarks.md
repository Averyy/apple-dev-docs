# landmarks

**Framework**: Vision  
**Kind**: property

The facial features of the detected face.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var landmarks: FaceObservation.Landmarks2D? { get }
```

#### Discussion

This value is `nil` for face observations produced by a [`DetectFaceRectanglesRequest`](detectfacerectanglesrequest.md) analysis. Use the [`DetectFaceLandmarksRequest`](detectfacelandmarksrequest.md) object to find facial features.

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [FaceObservation.Landmarks2D](faceobservation/landmarks2d.md)
  A collection of facial features that a request detects.
- [let pitch: Measurement<UnitAngle>](faceobservation/pitch.md)
  The pitch angle of a face.
- [let roll: Measurement<UnitAngle>](faceobservation/roll.md)
  The roll angle of a face.
- [let yaw: Measurement<UnitAngle>](faceobservation/yaw.md)
  The yaw angle of a face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/landmarks)*
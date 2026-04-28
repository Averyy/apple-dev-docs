# HumanBodyPose3DObservation.EstimationTechnique

**Framework**: Vision  
**Kind**: enum

Constants that identify body height estimation techniques.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum EstimationTechnique
```

## Topics

### Getting estimation techniques
- [HumanBodyPose3DObservation.EstimationTechnique.measured](humanbodypose3dobservation/estimationtechnique/measured.md)
  A technique that uses LiDAR depth data to measure body height, in meters.
- [HumanBodyPose3DObservation.EstimationTechnique.reference](humanbodypose3dobservation/estimationtechnique/reference.md)
  A technique that uses a reference height.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let bodyHeight: Measurement<UnitLength>](humanbodypose3dobservation/bodyheight.md)
  The estimated human body height, in meters.
- [let cameraOriginMatrix: simd_float4x4](humanbodypose3dobservation/cameraoriginmatrix.md)
  A transform from the skeleton hip to the camera.
- [let heightEstimationTechnique: HumanBodyPose3DObservation.EstimationTechnique](humanbodypose3dobservation/heightestimationtechnique.md)
  The technique the framework uses to estimate body height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/estimationtechnique)*
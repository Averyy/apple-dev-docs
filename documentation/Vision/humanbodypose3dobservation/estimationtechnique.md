# HumanBodyPose3DObservation.EstimationTechnique

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

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
- [HumanBodyPose3DObservation.EstimationTechnique.measured](./estimationtechnique/measured.md)
  A technique that uses LiDAR depth data to measure body height, in meters.
- [HumanBodyPose3DObservation.EstimationTechnique.reference](./estimationtechnique/reference.md)
  A technique that uses a reference height.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting an observation
- [enum RequestDescriptor](../requestdescriptor.md)
  A type that describes the request and revision combination.
- [let bodyHeight: Measurement<UnitLength>](./bodyheight.md)
  The estimated human body height, in meters.
- [let cameraOriginMatrix: simd_float4x4](./cameraoriginmatrix.md)
  A transform from the skeleton hip to the camera.
- [let heightEstimationTechnique: HumanBodyPose3DObservation.EstimationTechnique](./heightestimationtechnique.md)
  The technique the framework uses to estimate body height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/estimationtechnique)*
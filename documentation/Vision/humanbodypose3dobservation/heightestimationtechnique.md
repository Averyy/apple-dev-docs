# heightEstimationTechnique

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The technique the framework uses to estimate body height.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let heightEstimationTechnique: HumanBodyPose3DObservation.EstimationTechnique
```

## See Also

### Inspecting an observation
- [enum RequestDescriptor](../requestdescriptor.md)
  A type that describes the request and revision combination.
- [let bodyHeight: Measurement<UnitLength>](./bodyheight.md)
  The estimated human body height, in meters.
- [let cameraOriginMatrix: simd_float4x4](./cameraoriginmatrix.md)
  A transform from the skeleton hip to the camera.
- [HumanBodyPose3DObservation.EstimationTechnique](./estimationtechnique.md)
  Constants that identify body height estimation techniques.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/heightestimationtechnique)*
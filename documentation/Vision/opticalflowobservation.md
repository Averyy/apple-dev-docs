# OpticalFlowObservation

**Framework**: Vision  
**Kind**: struct

An object that represents an optical flow that an image-analysis request produces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct OpticalFlowObservation
```

#### Overview

The optical flow is a 2D image, with each pixel representing the directional change from a previous to current image.

## Topics

### Creating an observation
- [init?(VNPixelBufferObservation)](opticalflowobservation/init(_:).md)
  Creates an optical flow observation.
### Inspecting an observation
- [var pixelFormat: OSType](opticalflowobservation/pixelformat.md)
  The four-character code that identifies the pixel format.
- [var size: CGSize](opticalflowobservation/size.md)
  The size of the observation image.
### Getting the optical flow
- [func flow(at: NormalizedPoint) -> (Float, Float)](opticalflowobservation/flow(at:).md)
  Returns the optical flow for the specified location in the observation image.
### Accessing the memory
- [func withUnsafePointer<R>((UnsafeRawPointer) -> R) -> R](opticalflowobservation/withunsafepointer(_:).md)
  Invokes the given closure with a pointer to the given argument.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/opticalflowobservation)*
# OpticalFlowObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An object that represents an optical flow that an image-analysis request produces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct OpticalFlowObservation
```

## Overview

The optical flow is a 2D image, with each pixel representing the directional change from a previous to current image.

## Topics

### Creating an observation
- [init?(VNPixelBufferObservation)](./opticalflowobservation/init%28_%29.md)
  Creates an optical flow observation.
### Inspecting an observation
- [var pixelFormat: OSType](./opticalflowobservation/pixelformat.md)
  The four-character code that identifies the pixel format.
- [var pixelBuffer: CVReadOnlyPixelBuffer](./opticalflowobservation/pixelbuffer.md)
- [var size: CGSize](./opticalflowobservation/size.md)
  The size of the observation image.
### Getting the optical flow
- [func flow(at: NormalizedPoint) -> (Float, Float)](./opticalflowobservation/flow%28at%29.md)
  Returns the optical flow for the specified location in the observation image.
### Accessing the memory
- [func withUnsafePointer<R>((UnsafeRawPointer) -> R) -> R](./opticalflowobservation/withunsafepointer%28_%29.md)
  Invokes the given closure with a pointer to the given argument.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VisionObservation](./visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/opticalflowobservation)*
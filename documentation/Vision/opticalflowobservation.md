# OpticalFlowObservation

**Framework**: Vision  
**Kind**: struct

An object that represents an optical flow that an image-analysis request produces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/opticalflowobservation)*
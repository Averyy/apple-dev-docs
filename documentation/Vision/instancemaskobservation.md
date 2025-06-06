# InstanceMaskObservation

**Framework**: Vision  
**Kind**: struct

An observation that contains an instance mask that labels instances in the mask.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct InstanceMaskObservation
```

## Topics

### Creating an observation
- [init?(VNInstanceMaskObservation)](instancemaskobservation/init(_:).md)
  Creates an instance mask observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
### Generating a mask
- [func generateMask(for: IndexSet) throws -> CVPixelBuffer](instancemaskobservation/generatemask(for:).md)
  Creates a low-resolution mask from the instances you specify.
- [func generateMaskedImage(for: IndexSet, imageFrom: ImageRequestHandler, croppedToInstancesExtent: Bool) throws -> CVPixelBuffer](instancemaskobservation/generatemaskedimage(for:imagefrom:croppedtoinstancesextent:).md)
  Creates a high-resolution image with everything except for the instances you specify masked out.
- [func generateScaledMask(for: IndexSet, scaledToImageFrom: ImageRequestHandler) throws -> CVPixelBuffer](instancemaskobservation/generatescaledmask(for:scaledtoimagefrom:).md)
  Creates a high-resolution mask representing a combination of the instances you specify.
### Getting instances
- [func instanceAtPoint(NormalizedPoint) -> IndexSet](instancemaskobservation/instanceatpoint(_:).md)
  Returns an instance at the point you specify.
- [let allInstances: IndexSet](instancemaskobservation/allinstances.md)
  The collection that contains all instances, excluding the background.
- [let allInstancesMask: PixelBufferObservation](instancemaskobservation/allinstancesmask.md)
  The resulting mask that represents all instances.
- [struct PixelBufferObservation](pixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/vision/instancemaskobservation)*
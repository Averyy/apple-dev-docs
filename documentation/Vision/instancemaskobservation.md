# InstanceMaskObservation

**Framework**: Vision  
**Kind**: struct

An observation that contains an instance mask that labels instances in the mask.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/instancemaskobservation)*
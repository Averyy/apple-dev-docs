# PixelBufferObservation

**Framework**: Vision  
**Kind**: struct

An object that represents an image that an image-analysis request produces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct PixelBufferObservation
```

## Topics

### Creating an observation
- [init?(VNPixelBufferObservation)](pixelbufferobservation/init(_:).md)
  Creates a pixel buffer observation.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [var cgImage: CGImage](pixelbufferobservation/cgimage.md)
  A Core Graphics image created from the pixel buffer observation.
- [var pixelFormat: OSType](pixelbufferobservation/pixelformat.md)
  The four-character code that identifies the pixel format.
- [var size: CGSize](pixelbufferobservation/size.md)
  The size of the image.
### Getting pixel data
- [func pixel(at: NormalizedPoint) -> Float](pixelbufferobservation/pixel(at:).md)
  Returns the pixel data for the specified location in the image.
### Accessing the memory
- [func withUnsafePointer<R>((UnsafeRawPointer) -> R) -> R](pixelbufferobservation/withunsafepointer(_:).md)
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

- [struct ClassificationObservation](classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [struct CoreMLFeatureValueObservation](coremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/pixelbufferobservation)*
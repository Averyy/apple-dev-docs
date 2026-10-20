# PixelBufferObservation

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An object that represents an image that an image-analysis request produces.

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
struct PixelBufferObservation
```

## Mentions

- [Isolating an object from a tap, box, or scribble](./segmenting-objects-with-iterative-refinement.md)

## Topics

### Creating an observation
- [init?(VNPixelBufferObservation)](./pixelbufferobservation/init%28_%29.md)
  Creates a pixel buffer observation.
### Inspecting an observation
- [enum RequestDescriptor](./requestdescriptor.md)
  A type that describes the request and revision combination.
- [var cgImage: CGImage](./pixelbufferobservation/cgimage.md)
  A Core Graphics image created from the pixel buffer observation.
- [var pixelFormat: OSType](./pixelbufferobservation/pixelformat.md)
  The four-character code that identifies the pixel format.
- [var pixelBuffer: CVReadOnlyPixelBuffer](./pixelbufferobservation/pixelbuffer.md)
- [var size: CGSize](./pixelbufferobservation/size.md)
  The size of the image.
### Getting pixel data
- [func pixel(at: NormalizedPoint) -> Float](./pixelbufferobservation/pixel%28at%29.md)
  Returns the pixel data for the specified location in the image.
### Accessing the memory
- [func withUnsafePointer<R>((UnsafeRawPointer) -> R) -> R](./pixelbufferobservation/withunsafepointer%28_%29.md)
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

## See Also

### Understanding the result
- [struct ClassificationObservation](./classificationobservation.md)
  An object that represents classification information that an image-analysis request produces.
- [struct CoreMLFeatureValueObservation](./coremlfeaturevalueobservation.md)
  An object that represents a collection of key-value information that a Core ML image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/pixelbufferobservation)*
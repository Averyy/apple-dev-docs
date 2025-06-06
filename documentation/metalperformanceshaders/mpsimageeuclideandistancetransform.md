# MPSImageEuclideanDistanceTransform

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that performs a Euclidean distance transform on an image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSImageEuclideanDistanceTransform : MPSUnaryImageKernel
```

## Topics

### Creating a Euclidean distance transform
- [init(device: any MTLDevice)](mpsimageeuclideandistancetransform/2953973-init.md)
  Creates a Euclidean distance transform that runs on a specified device.
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageeuclideandistancetransform/2953972-init.md)
  Creates a Euclidean distance transform that uses a specified decoder for your data and runs on a specified device.
### Limiting the search for nonzero pixels
- [var searchLimitRadius: Float](mpsimageeuclideandistancetransform/3547977-searchlimitradius.md)
  Limits the search in an image from a pixel to the closest nonzero pixel within a specified radius.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageeuclideandistancetransform)*
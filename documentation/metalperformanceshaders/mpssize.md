# MPSSize

**Framework**: Metal Performance Shaders  
**Kind**: struct

A size of a region in an image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSSize
```

#### Overview

The depth of a region is usually `1.0`.

The `double` data type is used because some kernel operations require fractional precision—for example, the [`MPSImageLanczosScale`](mpsimagelanczosscale.md) filter.

## Topics

### Fields
- [var width: Double](mpssize/width.md)
  The width of the region, in pixels.
- [var height: Double](mpssize/height.md)
  The height of the region, in pixels.
- [var depth: Double](mpssize/depth.md)
  The depth of the region, in pixels.
### Initializers
- [init()](mpssize/init.md)
- [init(width: Double, height: Double, depth: Double)](mpssize/init(width:height:depth:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssize)*
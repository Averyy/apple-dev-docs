# MPSSize

**Framework**: Metal Performance Shaders  
**Kind**: struct

A size of a region in an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSSize
```

#### Overview

The depth of a region is usually `1.0`.

The `double` data type is used because some kernel operations require fractional precision—for example, the [`MPSImageLanczosScale`](mpsimagelanczosscale.md) filter.

## Topics

### Initializers
- [init()](mpssize/1618801-init.md)
- [init(width: Double, height: Double, depth: Double)](mpssize/1618905-init.md)
### Instance Properties
- [var depth: Double](mpssize/1618886-depth.md)
  The depth of the region, in pixels.
- [var height: Double](mpssize/1618874-height.md)
  The height of the region, in pixels.
- [var width: Double](mpssize/1618898-width.md)
  The width of the region, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssize)*
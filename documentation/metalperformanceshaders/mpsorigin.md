# MPSOrigin

**Framework**: Metal Performance Shaders  
**Kind**: struct

A position in an image used as the source origin.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSOrigin
```

#### Overview

The `double` data type is used because some kernel operations require fractional precision—for example, the [`MPSImageLanczosScale`](mpsimagelanczosscale.md) filter.

## Topics

### Initializers
- [init()](mpsorigin/1618866-init.md)
- [init(x: Double, y: Double, z: Double)](mpsorigin/1618888-init.md)
### Instance Properties
- [var x: Double](mpsorigin/1618870-x.md)
  The x coordinate of the position, in pixels.
- [var y: Double](mpsorigin/1618793-y.md)
  The y coordinate of the position, in pixels.
- [var z: Double](mpsorigin/1618833-z.md)
  The z coordinate of the position, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsorigin)*
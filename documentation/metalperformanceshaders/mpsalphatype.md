# MPSAlphaType

**Framework**: Metal Performance Shaders  
**Kind**: enum

Premultiplication description for the color channels of an image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSAlphaType : UInt, @unchecked Sendable
```

#### Overview

Some image data is premultiplied. That is to say that the color channels are stored instead as `color*alpha`. This is an optimization for image compositing (alpha blending), but it can get in the way of most other image filters, especially those that apply non-linear effects like the color conversion filters and functions like convolution or resampling filters that look at adjacent pixels, where the alpha may not be the same. The following are some basic conversion cases:

| Source | Destination | Operation |
| --- | --- | --- |
| `NonPremultiplied` | `NonPremultiplied` | None. |
| `NonPremultiplied` | `AlphaIsOne` | Composite with opaque background color. |
| `NonPremultiplied` | `Premultiplied` | Multiply color channels by alpha. |
| `AlphaIsOne` | `NonPremultiplied` | Set alpha to 1. |
| `AlphaIsOne` | `AlphaIsOne` | Set alpha to 1. |
| `AlphaIsOne` | `Premultiplied` | Set alpha to 1. |
| `Premultiplied` | `NonPremultiplied` | Divide color channels by alpha. |
| `Premultiplied` | `AlphaIsOne` | Composite with opaque background color. |
| `Premultiplied` | `Premultiplied` | None. |

Most [`MPSKernel`](mpskernel.md) objects require non-premultiplied or completely opaque colors to work correctly. They implictly assume that alpha is equal to 1 and do not provide functions for the user to specify alpha channel types. Currently, the only filters that can handle premultiplied data are the color conversion filters provided by [`MPSImageConversion`](mpsimageconversion.md) kernels and they insert extra operations to ensure a correct conversion. Fully opaque images should use `MPSAlphaTypeAlphaIsOne`

## Topics

### Constants
- [MPSAlphaType.nonPremultiplied](mpsalphatype/nonpremultiplied.md)
  The image is not premultiplied by alpha. Alpha is not guaranteed to be 1. ([`CGImageAlphaInfo.first`](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/first)`/`[`CGImageAlphaInfo.last`](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/last))
- [MPSAlphaType.alphaIsOne](mpsalphatype/alphaisone.md)
  Alpha is guaranteed to be 1, even if it is not encoded as 1 or not encoded at all. ([`CGImageAlphaInfo.noneSkipFirst`](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/noneskipfirst)`/`[`CGImageAlphaInfo.noneSkipLast`](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/noneskiplast)`, `[`CGImageAlphaInfo.none`](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/none))
- [MPSAlphaType.premultiplied](mpsalphatype/premultiplied.md)
  The image is premultiplied by alpha. Alpha is not guaranteed to be 1. ([`CGImageAlphaInfo.premultipliedFirst`](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/premultipliedfirst)`/`[`CGImageAlphaInfo.premultipliedLast`](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/premultipliedlast))

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)

## See Also

- [init(device: any MTLDevice, srcAlpha: MPSAlphaType, destAlpha: MPSAlphaType, backgroundColor: UnsafeMutablePointer<CGFloat>?, conversionInfo: CGColorConversionInfo?)](mpsimageconversion/2206722-init.md)
  Initializes a filter that can convert texture color space, alpha, and pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsalphatype)*
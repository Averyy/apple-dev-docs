# kCISamplerColorSpace

**Framework**: Core Image  
**Kind**: var

The key for the color space to use when sampling the image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCISamplerColorSpace: String
```

#### Discussion

The associated value must be an RGB [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) object. Using this option specifies that samples should be converted to this color space before being passed to a kernel. If not specified, samples will be passed to the kernel in the working color space of the Core Image context used to render the image.

## See Also

- [let kCISamplerAffineMatrix: String](kcisampleraffinematrix.md)
  The key for an affine matrix. The associated value is an `NSArray` object ([]) that defines the transformation to apply to the sampler.
- [let kCISamplerWrapMode: String](kcisamplerwrapmode.md)
  The key for the sampler wrap mode. The wrap mode specifies how Core Image produces pixels that are outside the extent of the sample. Possible values are [`kCISamplerWrapBlack`](kcisamplerwrapblack.md) and [`kCISamplerWrapClamp`](kcisamplerwrapclamp.md).
- [let kCISamplerFilterMode: String](kcisamplerfiltermode.md)
  The key for the filtering to use when sampling the image. Possible values are [`kCISamplerFilterNearest`](kcisamplerfilternearest.md) and [`kCISamplerFilterLinear`](kcisamplerfilterlinear.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/kcisamplercolorspace)*
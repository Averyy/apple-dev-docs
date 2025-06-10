# kCISamplerAffineMatrix

**Framework**: Core Image  
**Kind**: var

The key for an affine matrix. The associated value is an `NSArray` object ([]) that defines the transformation to apply to the sampler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCISamplerAffineMatrix: String
```

## See Also

- [let kCISamplerWrapMode: String](kcisamplerwrapmode.md)
  The key for the sampler wrap mode. The wrap mode specifies how Core Image produces pixels that are outside the extent of the sample. Possible values are [`kCISamplerWrapBlack`](kcisamplerwrapblack.md) and [`kCISamplerWrapClamp`](kcisamplerwrapclamp.md).
- [let kCISamplerFilterMode: String](kcisamplerfiltermode.md)
  The key for the filtering to use when sampling the image. Possible values are [`kCISamplerFilterNearest`](kcisamplerfilternearest.md) and [`kCISamplerFilterLinear`](kcisamplerfilterlinear.md).
- [let kCISamplerColorSpace: String](kcisamplercolorspace.md)
  The key for the color space to use when sampling the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/kcisampleraffinematrix)*
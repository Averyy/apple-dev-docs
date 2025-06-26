# MPSAlphaType.alphaIsOne

**Framework**: Metal Performance Shaders  
**Kind**: case

Alpha is guaranteed to be 1.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case alphaIsOne
```

#### Overview

The alpha value is guaranteed to be `1` even if it is not encoded as `1` or even not encoded at all.

## See Also

- [MPSAlphaType.nonPremultiplied](mpsalphatype/nonpremultiplied.md)
  The image is not premultiplied by alpha.
- [MPSAlphaType.premultiplied](mpsalphatype/premultiplied.md)
  The image is premultiplied by alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsalphatype/alphaisone)*
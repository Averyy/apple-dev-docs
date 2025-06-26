# destinationAlpha

**Framework**: Metal Performance Shaders  
**Kind**: property

Premultiplication description for the destination texture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var destinationAlpha: MPSAlphaType { get }
```

#### Discussion

Color space conversion operations produce non-premultiplied data. Use this property to tag cases where premultiplied results are required. If the [`MPSAlphaType.alphaIsOne`](mpsalphatype/alphaisone.md) value is used, the alpha channel will be set to 1. The default value is [`MPSAlphaType.alphaIsOne`](mpsalphatype/alphaisone.md).

## See Also

- [var sourceAlpha: MPSAlphaType](mpsimageconversion/sourcealpha.md)
  Premultiplication description for the source texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconversion/destinationalpha)*
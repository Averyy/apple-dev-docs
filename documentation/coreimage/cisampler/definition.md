# definition

**Framework**: Core Image  
**Kind**: property

The domain of definition (DOD) of the sampler

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var definition: CIFilterShape { get }
```

#### Discussion

The DOD contains all nontransparent pixels produced by referencing the sampler.

## See Also

- [var extent: CGRect](cisampler/extent.md)
  The rectangle that specifies the extent of the sampler


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler/definition)*
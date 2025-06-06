# MPSRNNBidirectionalCombineMode

**Framework**: Metal Performance Shaders  
**Kind**: enum

Modes that define how two images or matrices are combined. 

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSRNNBidirectionalCombineMode : UInt, @unchecked Sendable
```

## Topics

### Enumeration Cases
- [MPSRNNBidirectionalCombineMode.add](mpsrnnbidirectionalcombinemode/add.md)
  A mode in which two sequences are summed to form a single output.
- [MPSRNNBidirectionalCombineMode.concatenate](mpsrnnbidirectionalcombinemode/concatenate.md)
  A mode in which two sequences are concatenated along the feature channels to form a single output.
- [MPSRNNBidirectionalCombineMode.none](mpsrnnbidirectionalcombinemode/none.md)
  A mode in which two sequences are kept separate.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnbidirectionalcombinemode)*
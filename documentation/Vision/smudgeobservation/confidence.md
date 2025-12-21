# confidence

**Framework**: Vision  
**Kind**: property

The level of confidence in the observation’s accuracy of smudge detection on a lens.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let confidence: Float
```

#### Discussion

The framework normalizes this value to `[0, 1]`, where `1` represents the most confident. When results come from a [`CoreMLRequest`](coremlrequest.md), the relevant [`Core ML`](https://developer.apple.com/documentation/CoreML) models forward the confidence values.

## See Also

- [var description: String](smudgeobservation/description.md)
  A textual representation of this instance.
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/smudgeobservation/confidence)*
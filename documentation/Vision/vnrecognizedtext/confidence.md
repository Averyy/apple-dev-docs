# confidence

**Framework**: Vision  
**Kind**: property

A normalized confidence score for the text recognition result.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var confidence: VNConfidence { get }
```

#### Discussion

The confidence level is a normalized value between `0.0` and `1.0`, where `1.0` represents the highest confidence.

## See Also

- [var string: String](vnrecognizedtext/string.md)
  The top candidate for recognized text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedtext/confidence)*
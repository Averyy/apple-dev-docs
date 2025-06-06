# UITextAlternativeStyle

**Framework**: UIKit  
**Kind**: enum

A constant that determines if the system highlights alternative phrases during text input.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum UITextAlternativeStyle
```

## Topics

### Constants
- [UITextAlternativeStyle.lowConfidence](uitextalternativestyle/lowconfidence.md)
  A constant that indicates that the text input should highlight alternatives because the input text may be incorrect.
- [UITextAlternativeStyle.none](uitextalternativestyle/none.md)
  A constant that indicates that the text input shouldn’t highlight alternatives because the input text is expected to be correct.
### Initializers
- [init?(rawValue: Int)](uitextalternativestyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func insertText(String, alternatives: [String], style: UITextAlternativeStyle)](uitextinput/inserttext(_:alternatives:style:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextalternativestyle)*
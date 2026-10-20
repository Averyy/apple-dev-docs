# UITextAlternativeStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A constant that determines if the system highlights alternative phrases during text input.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum UITextAlternativeStyle
```

```c
enum UITextAlternativeStyle : NSInteger;
```

## Topics

### Constants
- [UITextAlternativeStyle.lowConfidence](./uitextalternativestyle/lowconfidence.md)
  A constant that indicates that the text input should highlight alternatives because the input text may be incorrect.
- [UITextAlternativeStyle.none](./uitextalternativestyle/none.md)
  A constant that indicates that the text input shouldn’t highlight alternatives because the input text is expected to be correct.
### Initializers
- [init?(rawValue: Int)](./uitextalternativestyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting text-phrase alternatives
- [func insertText(String, alternatives: [String], style: UITextAlternativeStyle)](./uitextinput/inserttext%28_,alternatives,style%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextalternativestyle)*
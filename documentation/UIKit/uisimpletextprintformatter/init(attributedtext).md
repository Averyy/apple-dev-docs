# init(attributedText:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns a simple-text print formatter initialized with attributed text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(attributedText: NSAttributedString)
```

```objc
- (instancetype) initWithAttributedText:(NSAttributedString *) attributedText;
```

#### Return Value

An initialized instance of `UISimpleTextPrintFormatter` or `nil` if the object could not be created.

## Parameters

- `attributedText`: A string of attributed text or `nil` if you intend to assign the text later.

## See Also

### Related Documentation
- [var attributedText: NSAttributedString?](./attributedtext.md)
  A string of attributed text.
### Creating a simple-text print formatter
- [init(text: String)](./init%28text%29.md)
  Returns a simple-text print formatter initialized with plain text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/init(attributedtext:))*
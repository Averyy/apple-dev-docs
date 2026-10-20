# init(text:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns a simple-text print formatter initialized with plain text.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(text: String)
```

```objc
- (instancetype) initWithText:(NSString *) text;
```

#### Return Value

An initialized instance of `UISimpleTextPrintFormatter` or `nil` if the object could not be created.

## Parameters

- `text`: A string of plain text or `nil` if you intend to assign the text later.

## See Also

### Related Documentation
- [var text: String?](./text.md)
  A string of plain text.
### Creating a simple-text print formatter
- [init(attributedText: NSAttributedString)](./init%28attributedtext%29.md)
  Returns a simple-text print formatter initialized with attributed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/init(text:))*
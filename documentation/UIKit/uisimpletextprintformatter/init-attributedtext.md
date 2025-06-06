# init(attributedText:)

**Framework**: UIKit  
**Kind**: init

Returns a simple-text print formatter initialized with attributed text.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(attributedText: NSAttributedString)
```

#### Return Value

An initialized instance of `UISimpleTextPrintFormatter` or `nil` if the object could not be created.

## Parameters

- `attributedText`: A string of attributed text or   if you intend to assign the text later.

## See Also

- [var attributedText: NSAttributedString?](uisimpletextprintformatter/attributedtext.md)
  A string of attributed text.
- [init(text: String)](uisimpletextprintformatter/init(text:).md)
  Returns a simple-text print formatter initialized with plain text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisimpletextprintformatter/init(attributedtext:))*
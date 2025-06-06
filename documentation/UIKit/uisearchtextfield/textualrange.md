# textualRange

**Framework**: UIKit  
**Kind**: property

The range of the field’s text content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textualRange: UITextRange { get }
```

#### Discussion

Both tokens and text are included in the range from [`beginningOfDocument`](uitextinput/beginningofdocument.md) to [`endOfDocument`](uitextinput/endofdocument.md). This property provides convenient access to just the text.

## See Also

- [func replaceTextualPortion(of: UITextRange, with: UISearchToken, at: Int)](uisearchtextfield/replacetextualportion(of:with:at:).md)
  Converts text in a search field into a search token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/textualrange)*
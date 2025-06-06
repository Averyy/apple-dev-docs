# setMarkedText(_:selectedRange:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Inserts the provided text and marks it to indicate that it’s part of an active input session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setMarkedText(_ markedText: String, selectedRange: NSRange)
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)

#### Discussion

Setting marked text either replaces the existing marked text or, if none is present, inserts it in place of the current selection.

## See Also

- [func unmarkText()](uitextdocumentproxy/unmarktext.md)
  Unmarks the currently marked text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdocumentproxy/setmarkedtext(_:selectedrange:))*
# layoutManager

**Framework**: UIKit  
**Kind**: property

The layout manager that lays out text for the text view’s text container.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var layoutManager: NSLayoutManager { get }
```

#### Discussion

This property is a convenience accessor that provides access through the text container.

## See Also

- [var textLayoutManager: NSTextLayoutManager?](uitextview/textlayoutmanager.md)
  The text layout manager that lays out text for the text view’s text container.
- [var textContainer: NSTextContainer](uitextview/textcontainer.md)
  The text container object that defines the area where text displays in the text view.
- [var textStorage: NSTextStorage](uitextview/textstorage.md)
  The text storage object holding the text that displays in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/layoutmanager)*
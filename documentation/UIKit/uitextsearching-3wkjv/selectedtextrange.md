# selectedTextRange

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The range of selected text in a document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var selectedTextRange: UITextRange? { get }
```

#### Discussion

If the text range has a length, it indicates the currently selected text. If it has zero length, it indicates the caret (insertion point). If the text-range object is `nil`, it indicates that there’s no current selection.

## See Also

- [var selectedTextSearchDocument: Self.DocumentIdentifier?](uitextsearching-3wkjv/selectedtextsearchdocument.md)
  The object that uniquely identifies the specific document with selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/selectedtextrange)*
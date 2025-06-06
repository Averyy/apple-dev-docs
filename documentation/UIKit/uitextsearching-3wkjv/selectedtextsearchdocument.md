# selectedTextSearchDocument

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The object that uniquely identifies the specific document with selected text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var selectedTextSearchDocument: Self.DocumentIdentifier? { get }
```

#### Discussion

When performing a search across multiple documents, this object returns the identifier for the document with the selected text. When performing a search on a single document, it returns `nil`.

## See Also

- [var selectedTextRange: UITextRange?](uitextsearching-3wkjv/selectedtextrange.md)
  The range of selected text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/selectedtextsearchdocument)*
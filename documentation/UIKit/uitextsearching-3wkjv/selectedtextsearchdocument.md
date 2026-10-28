# selectedTextSearchDocument

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The object that uniquely identifies the specific document with selected text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
var selectedTextSearchDocument: Self.DocumentIdentifier? { get }
```

## Discussion

When performing a search across multiple documents, this object returns the identifier for the document with the selected text. When performing a search on a single document, it returns `nil`.

## Default Implementations

### UITextSearching Implementations
- [var selectedTextSearchDocument: Self.DocumentIdentifier?](./selectedtextsearchdocument-72uzm.md)

## See Also

### Identifying selected text
- [var selectedTextRange: UITextRange?](./selectedtextrange.md)
  The range of selected text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/selectedtextsearchdocument)*
# selectedTextSearchDocument

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that uniquely identifies the specific document with selected text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (readonly, nullable) UITextSearchDocumentIdentifier selectedTextSearchDocument;
```

## Discussion

When performing a search across multiple documents, this object returns the identifier for the document with the selected text. When performing a search on a single document, it returns `nil`.

## See Also

### Identifying selected text
- [selectedTextRange](./selectedtextrange.md)
  The range of selected text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/selectedtextsearchdocument)*
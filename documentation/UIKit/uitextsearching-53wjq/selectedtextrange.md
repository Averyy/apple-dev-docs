# selectedTextRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The range of selected text in a document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (readonly, nullable) UITextRange * selectedTextRange;
```

## Discussion

If the text range has a length, it indicates the currently selected text. If it has zero length, it indicates the caret (insertion point). If the text-range object is `nil`, it indicates that there’s no current selection.

## See Also

### Identifying selected text
- [selectedTextSearchDocument](./selectedtextsearchdocument.md)
  The object that uniquely identifies the specific document with selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/selectedtextrange)*
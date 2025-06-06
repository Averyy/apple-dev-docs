# willHighlight(foundTextRange:document:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Informs the searchable object when the highlighted search result is about to change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func willHighlight(foundTextRange: UITextRange, document: Self.DocumentIdentifier?)
```

## Parameters

- `foundTextRange`: The text range to highlight.
- `document`: A string that uniquely identifies the document containing the text range.   when searching a single document.

## See Also

- [func decorate(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, usingStyle: UITextSearchFoundTextStyle)](uitextsearching-3wkjv/decorate(foundtextrange:document:usingstyle:).md)
  Applies the style to a specific text range to indicate found and highlighted results.
- [func clearAllDecoratedFoundText()](uitextsearching-3wkjv/clearalldecoratedfoundtext.md)
  Clears the style from all found and highlighted results.
- [func scrollRangeToVisible(UITextRange, inDocument: Self.DocumentIdentifier?)](uitextsearching-3wkjv/scrollrangetovisible(_:indocument:).md)
  Scrolls to the containing view to make the text range visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/willhighlight(foundtextrange:document:))*
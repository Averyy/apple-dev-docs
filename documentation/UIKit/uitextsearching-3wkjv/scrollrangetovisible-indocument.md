# scrollRangeToVisible(_:inDocument:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Scrolls to the containing view to make the text range visible.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func scrollRangeToVisible(_ range: UITextRange, inDocument: Self.DocumentIdentifier?)
```

#### Discussion

If the seachable object supports scrolling, use this method to implement scrolling your view to make the highlighted text range visible.

## Parameters

- `range`: The text range to scroll to.
- `inDocument`: A string that uniquely identifies the document containing the text range.   when searching a single document.

## See Also

- [func decorate(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, usingStyle: UITextSearchFoundTextStyle)](uitextsearching-3wkjv/decorate(foundtextrange:document:usingstyle:).md)
  Applies the style to a specific text range to indicate found and highlighted results.
- [func clearAllDecoratedFoundText()](uitextsearching-3wkjv/clearalldecoratedfoundtext.md)
  Clears the style from all found and highlighted results.
- [func willHighlight(foundTextRange: UITextRange, document: Self.DocumentIdentifier?)](uitextsearching-3wkjv/willhighlight(foundtextrange:document:).md)
  Informs the searchable object when the highlighted search result is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/scrollrangetovisible(_:indocument:))*
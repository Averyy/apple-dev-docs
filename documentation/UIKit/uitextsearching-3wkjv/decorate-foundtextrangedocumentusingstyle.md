# decorate(foundTextRange:document:usingStyle:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Applies the style to a specific text range to indicate found and highlighted results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func decorate(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, usingStyle: UITextSearchFoundTextStyle)
```

#### Discussion

The system calls this method during a find session to display the results of a search in your custom view. Your implenentation should decorate matching text ranges for the given style to indicate the found and highlighted result.

## Parameters

- `foundTextRange`: The text range to decorate.
- `document`: A string that uniquely identifies the document containing the text range.   when searching a single document.
- `usingStyle`: The style to decorate the text: highlighted, found, or normal.

## See Also

- [func clearAllDecoratedFoundText()](uitextsearching-3wkjv/clearalldecoratedfoundtext.md)
  Clears the style from all found and highlighted results.
- [func willHighlight(foundTextRange: UITextRange, document: Self.DocumentIdentifier?)](uitextsearching-3wkjv/willhighlight(foundtextrange:document:).md)
  Informs the searchable object when the highlighted search result is about to change.
- [func scrollRangeToVisible(UITextRange, inDocument: Self.DocumentIdentifier?)](uitextsearching-3wkjv/scrollrangetovisible(_:indocument:).md)
  Scrolls to the containing view to make the text range visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/decorate(foundtextrange:document:usingstyle:))*
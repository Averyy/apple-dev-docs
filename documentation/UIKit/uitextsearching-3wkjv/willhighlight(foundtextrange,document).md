# willHighlight(foundTextRange:document:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the searchable object when the highlighted search result is about to change.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
func willHighlight(foundTextRange: UITextRange, document: Self.DocumentIdentifier?)
```

## Parameters

- `foundTextRange`: The text range to highlight.
- `document`: A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Default Implementations

### UITextSearching Implementations
- [func willHighlight(foundTextRange: UITextRange, document: Self.DocumentIdentifier?)](./willhighlight%28foundtextrange,document%29-55xf1.md)

## See Also

### Displaying results
- [func decorate(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, usingStyle: UITextSearchFoundTextStyle)](./decorate%28foundtextrange,document,usingstyle%29.md)
  Applies the style to a specific text range to indicate found and highlighted results.
- [func clearAllDecoratedFoundText()](./clearalldecoratedfoundtext%28%29.md)
  Clears the style from all found and highlighted results.
- [func scrollRangeToVisible(UITextRange, inDocument: Self.DocumentIdentifier?)](./scrollrangetovisible%28_,indocument%29.md)
  Scrolls to the containing view to make the text range visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/willhighlight(foundtextrange:document:))*
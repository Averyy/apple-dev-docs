# scrollRangeToVisible(_:inDocument:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Scrolls to the containing view to make the text range visible.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
func scrollRangeToVisible(_ range: UITextRange, inDocument: Self.DocumentIdentifier?)
```

## Discussion

If the seachable object supports scrolling, use this method to implement scrolling your view to make the highlighted text range visible.

## Parameters

- `range`: The text range to scroll to.
- `inDocument`: A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Default Implementations

### UITextSearching Implementations
- [func scrollRangeToVisible(UITextRange, inDocument: Self.DocumentIdentifier?)](./scrollrangetovisible%28_,indocument%29-8v4iu.md)

## See Also

### Displaying results
- [func decorate(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, usingStyle: UITextSearchFoundTextStyle)](./decorate%28foundtextrange,document,usingstyle%29.md)
  Applies the style to a specific text range to indicate found and highlighted results.
- [func clearAllDecoratedFoundText()](./clearalldecoratedfoundtext%28%29.md)
  Clears the style from all found and highlighted results.
- [func willHighlight(foundTextRange: UITextRange, document: Self.DocumentIdentifier?)](./willhighlight%28foundtextrange,document%29.md)
  Informs the searchable object when the highlighted search result is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/scrollrangetovisible(_:indocument:))*
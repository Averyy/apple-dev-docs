# decorateFoundTextRange:inDocument:usingStyle:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Applies the style to a specific text range to indicate found and highlighted results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) decorateFoundTextRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document usingStyle:(UITextSearchFoundTextStyle) style;
```

## Discussion

The system calls this method during a find session to display the results of a search in your custom view. Your implenentation should decorate matching text ranges for the given style to indicate the found and highlighted result.

## Parameters

- `range`: The text range to decorate.
- `document`: A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.
- `style`: The style to decorate the text: highlighted, found, or normal.

## See Also

### Displaying results
- [- clearAllDecoratedFoundText](./clearalldecoratedfoundtext.md)
  Clears the style from all found and highlighted results.
- [- willHighlightFoundTextRange:inDocument:](./willhighlightfoundtextrange_indocument_.md)
  Informs the searchable object when the highlighted search result is about to change.
- [- scrollRangeToVisible:inDocument:](./scrollrangetovisible_indocument_.md)
  Scrolls to the containing view to make the text range visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/decoratefoundtextrange:indocument:usingstyle:)*
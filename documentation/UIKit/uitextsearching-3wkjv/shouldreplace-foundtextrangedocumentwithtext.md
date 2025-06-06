# shouldReplace(foundTextRange:document:withText:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Determines whether the searchable object allows replacement of the text range you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func shouldReplace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String) -> Bool
```

#### Return Value

Return `No` to prevent the replacement of a particular text range.

#### Discussion

Returning `NO` from this method disables the “replace” button in the find panel. If you don’t implement this method, the system assumes all results are replacable.

## Parameters

- `foundTextRange`: The range of characters in a text container to consider a replacement for.
- `document`: A string that uniquely identifies the document containing the text range.
- `withText`: The string to replace the text with.

## See Also

- [var supportsTextReplacement: Bool](uitextsearching-3wkjv/supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)](uitextsearching-3wkjv/replace(foundtextrange:document:withtext:).md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)](uitextsearching-3wkjv/replaceall(querystring:options:withtext:).md)
  Informs the searchable object to replace all matching text across all searchable documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/shouldreplace(foundtextrange:document:withtext:))*
# replaceAll(queryString:options:withText:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Informs the searchable object to replace all matching text across all searchable documents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)
```

#### Discussion

When [`supportsTextReplacement`](uitextsearching-3wkjv/supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request the replacement of all text matching the query string.

## Parameters

- `queryString`: The string to search for and replace.
- `options`: The configurable options to use for matching words and comparing strings.
- `withText`: The string to replace the text with.

## See Also

- [var supportsTextReplacement: Bool](uitextsearching-3wkjv/supportstextreplacement.md)
  A Boolean value that indicates whether the searchable object supports replacing text.
- [func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)](uitextsearching-3wkjv/replace(foundtextrange:document:withtext:).md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [func shouldReplace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String) -> Bool](uitextsearching-3wkjv/shouldreplace(foundtextrange:document:withtext:).md)
  Determines whether the searchable object allows replacement of the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/replaceall(querystring:options:withtext:))*
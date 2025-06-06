# supportsTextReplacement

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the searchable object supports replacing text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var supportsTextReplacement: Bool { get }
```

## See Also

- [func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)](uitextsearching-3wkjv/replace(foundtextrange:document:withtext:).md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)](uitextsearching-3wkjv/replaceall(querystring:options:withtext:).md)
  Informs the searchable object to replace all matching text across all searchable documents.
- [func shouldReplace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String) -> Bool](uitextsearching-3wkjv/shouldreplace(foundtextrange:document:withtext:).md)
  Determines whether the searchable object allows replacement of the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/supportstextreplacement)*
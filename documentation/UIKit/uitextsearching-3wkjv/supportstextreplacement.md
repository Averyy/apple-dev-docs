# supportsTextReplacement

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the searchable object supports replacing text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
var supportsTextReplacement: Bool { get }
```

## Default Implementations

### UITextSearching Implementations
- [var supportsTextReplacement: Bool](./supportstextreplacement-68rh6.md)

## See Also

### Handling replacements
- [func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)](./replace%28foundtextrange,document,withtext%29.md)
  Informs the searchable object to replace the text range for the highlighted search result.
- [func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)](./replaceall%28querystring,options,withtext%29.md)
  Informs the searchable object to replace all matching text across all searchable documents.
- [func shouldReplace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String) -> Bool](./shouldreplace%28foundtextrange,document,withtext%29.md)
  Determines whether the searchable object allows replacement of the text range you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/supportstextreplacement)*
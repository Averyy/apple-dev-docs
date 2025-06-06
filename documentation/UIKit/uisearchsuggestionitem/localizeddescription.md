# localizedDescription

**Framework**: UIKit  
**Kind**: property

A description of the suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var localizedDescription: String? { get }
```

#### Discussion

The system uses this description for accessibility.

## See Also

- [var localizedSuggestion: String?](uisearchsuggestionitem/localizedsuggestion.md)
  A label for the suggestion, usually the search term the suggestion represents.
- [var localizedAttributedSuggestion: NSAttributedString?](uisearchsuggestionitem/localizedattributedsuggestion.md)
  An attributed label for the suggestion, usually the search term the suggestion represents.
- [var iconImage: UIImage?](uisearchsuggestionitem/iconimage.md)
  An image for display on the suggestion.
- [var representedObject: Any?](uisearchsuggestionitem/representedobject.md)
  An object for tracking supplementary information about the search suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/localizeddescription)*
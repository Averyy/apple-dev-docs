# representedObject

**Framework**: UIKit  
**Kind**: property

An object for tracking supplementary information about the search suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var representedObject: Any? { get set }
```

#### Discussion

Use this property to associate the search suggestion with a corresponding object.

## See Also

- [var localizedSuggestion: String?](uisearchsuggestionitem/localizedsuggestion.md)
  A label for the suggestion, usually the search term the suggestion represents.
- [var localizedAttributedSuggestion: NSAttributedString?](uisearchsuggestionitem/localizedattributedsuggestion.md)
  An attributed label for the suggestion, usually the search term the suggestion represents.
- [var localizedDescription: String?](uisearchsuggestionitem/localizeddescription.md)
  A description of the suggestion.
- [var iconImage: UIImage?](uisearchsuggestionitem/iconimage.md)
  An image for display on the suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/representedobject)*
# init(localizedAttributedSuggestion:)

**Framework**: UIKit  
**Kind**: init

Creates a search suggestion with the specified attributed label.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(localizedAttributedSuggestion suggestion: NSAttributedString)
```

## Parameters

- `suggestion`: An attributed label for the suggestion, usually the search term the suggestion represents.

## See Also

- [init(localizedSuggestion: String, localizedDescription: String?, iconImage: UIImage?)](uisearchsuggestionitem/init(localizedsuggestion:localizeddescription:iconimage:).md)
  Creates a search suggestion with the specified text and image attributes.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?, iconImage: UIImage?)](uisearchsuggestionitem/init(localizedattributedsuggestion:localizeddescription:iconimage:).md)
  Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [init(localizedSuggestion: String, localizedDescription: String?)](uisearchsuggestionitem/init(localizedsuggestion:localizeddescription:).md)
  Creates a search suggestion with the specified label and accessibility description.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?)](uisearchsuggestionitem/init(localizedattributedsuggestion:localizeddescription:).md)
  Creates a search suggestion with the specified attributed label and accessibility description.
- [init(localizedSuggestion: String)](uisearchsuggestionitem/init(localizedsuggestion:).md)
  Creates a search suggestion with the specified label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/init(localizedattributedsuggestion:))*
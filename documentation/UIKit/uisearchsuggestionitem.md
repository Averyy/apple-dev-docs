# UISearchSuggestionItem

**Framework**: UIKit  
**Kind**: class

A selectable search parameter.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISearchSuggestionItem
```

#### Overview

This class provides a basic implementation of the [`UISearchSuggestion`](uisearchsuggestion.md) protocol.

## Topics

### Creating a search suggestion
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
- [init(localizedAttributedSuggestion: NSAttributedString)](uisearchsuggestionitem/init(localizedattributedsuggestion:).md)
  Creates a search suggestion with the specified attributed label.
### Describing a search suggestion
- [var localizedSuggestion: String?](uisearchsuggestionitem/localizedsuggestion.md)
  A label for the suggestion, usually the search term the suggestion represents.
- [var localizedAttributedSuggestion: NSAttributedString?](uisearchsuggestionitem/localizedattributedsuggestion.md)
  An attributed label for the suggestion, usually the search term the suggestion represents.
- [var localizedDescription: String?](uisearchsuggestionitem/localizeddescription.md)
  A description of the suggestion.
- [var iconImage: UIImage?](uisearchsuggestionitem/iconimage.md)
  An image for display on the suggestion.
- [var representedObject: Any?](uisearchsuggestionitem/representedobject.md)
  An object for tracking supplementary information about the search suggestion.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UISearchSuggestion](uisearchsuggestion.md)

## See Also

- [var searchSuggestions: [any UISearchSuggestion]?](uisearchcontroller/searchsuggestions.md)
  A list of suggestions to offer as shortcuts below the search field.
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [protocol UISearchSuggestion](uisearchsuggestion.md)
  A set of attributes that a selectable search suggestion must provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem)*
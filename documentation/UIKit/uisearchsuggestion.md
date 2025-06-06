# UISearchSuggestion

**Framework**: UIKit  
**Kind**: protocol

A set of attributes that a selectable search suggestion must provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UISearchSuggestion : NSObjectProtocol
```

#### Overview

Provide common or predicted search queries to save the user the time of typing their entire query in a [`UISearchController`](uisearchcontroller.md) field. [`UISearchSuggestionItem`](uisearchsuggestionitem.md) provides a simple implementation of this protocol. You may also define and use your own type that conforms to [`UISearchSuggestion`](uisearchsuggestion.md).

## Topics

### Describing a search suggestion
- [var localizedSuggestion: String?](uisearchsuggestion/localizedsuggestion.md)
  A label for the suggestion, usually the search term the suggestion represents.
- [var localizedDescription: String?](uisearchsuggestion/localizeddescription.md)
  A description of the suggestion.
- [var localizedAttributedSuggestion: NSAttributedString?](uisearchsuggestion/localizedattributedsuggestion.md)
  An attributed label for the suggestion, usually the search term the suggestion represents.
- [var iconImage: UIImage?](uisearchsuggestion/iconimage.md)
  An image for display on the suggestion.
- [var representedObject: Any?](uisearchsuggestion/representedobject.md)
  An object for tracking supplementary information about the search suggestion.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UISearchSuggestionItem](uisearchsuggestionitem.md)

## See Also

- [var searchSuggestions: [any UISearchSuggestion]?](uisearchcontroller/searchsuggestions.md)
  A list of suggestions to offer as shortcuts below the search field.
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [class UISearchSuggestionItem](uisearchsuggestionitem.md)
  A selectable search parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestion)*
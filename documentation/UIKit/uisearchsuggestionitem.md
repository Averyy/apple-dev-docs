# UISearchSuggestionItem

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UISearchSuggestionItem : NSObject
```

#### Overview

This class provides a basic implementation of the [`UISearchSuggestion`](./uisearchsuggestion.md) protocol.

## Topics

### Creating a search suggestion
- [init(localizedSuggestion: String, localizedDescription: String?, iconImage: UIImage?)](./uisearchsuggestionitem/init%28localizedsuggestion,localizeddescription,iconimage%29.md)
  Creates a search suggestion with the specified text and image attributes.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?, iconImage: UIImage?)](./uisearchsuggestionitem/init%28localizedattributedsuggestion,localizeddescription,iconimage%29.md)
  Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [init(localizedSuggestion: String, localizedDescription: String?)](./uisearchsuggestionitem/init%28localizedsuggestion,localizeddescription%29.md)
  Creates a search suggestion with the specified label and accessibility description.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?)](./uisearchsuggestionitem/init%28localizedattributedsuggestion,localizeddescription%29.md)
  Creates a search suggestion with the specified attributed label and accessibility description.
- [init(localizedSuggestion: String)](./uisearchsuggestionitem/init%28localizedsuggestion%29.md)
  Creates a search suggestion with the specified label.
- [init(localizedAttributedSuggestion: NSAttributedString)](./uisearchsuggestionitem/init%28localizedattributedsuggestion%29.md)
  Creates a search suggestion with the specified attributed label.
### Describing a search suggestion
- [var localizedSuggestion: String?](./uisearchsuggestionitem/localizedsuggestion.md)
  A label for the suggestion, usually the search term the suggestion represents.
- [var localizedAttributedSuggestion: NSAttributedString?](./uisearchsuggestionitem/localizedattributedsuggestion.md)
  An attributed label for the suggestion, usually the search term the suggestion represents.
- [var localizedDescription: String?](./uisearchsuggestionitem/localizeddescription.md)
  A description of the suggestion.
- [var iconImage: UIImage?](./uisearchsuggestionitem/iconimage.md)
  An image for display on the suggestion.
- [var representedObject: Any?](./uisearchsuggestionitem/representedobject.md)
  An object for tracking supplementary information about the search suggestion.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UISearchSuggestion](./uisearchsuggestion.md)

## See Also

### Providing search suggestions
- [var searchSuggestions: [any UISearchSuggestion]?](./uisearchcontroller/searchsuggestions.md)
  A list of suggestions to offer as shortcuts below the search field.
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](./uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [protocol UISearchSuggestion](./uisearchsuggestion.md)
  A set of attributes that a selectable search suggestion must provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem)*
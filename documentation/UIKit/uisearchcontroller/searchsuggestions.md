# searchSuggestions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A list of suggestions to offer as shortcuts below the search field.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var searchSuggestions: [any UISearchSuggestion]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<id<UISearchSuggestion>> * searchSuggestions;
```

## Mentions

- [Building a desktop-class iPad app](../building-a-desktop-class-ipad-app.md)

## Discussion

Provide search suggestions to help people complete their query quickly. Update the suggestions as a person types by implementing [`updateSearchResults(for:)`](../uisearchresultsupdating/updatesearchresults%28for%29.md).

The presentation of the search suggestions varies according to the platform and [`searchBarPlacement`](../uinavigationitem/searchbarplacement-swift.property.md):

- In tvOS, the suggestions appear in a list below the keyboard.
- In iOS, the suggestions appear in a menu below the search field when the search bar placement is [`inline`](../uinavigationitem/searchbarplacement-swift.enum/inline.md), and in a list that overlays the [`searchResultsController`](./searchresultscontroller.md) when the search bar placement is [`UINavigationItem.SearchBarPlacement.stacked`](../uinavigationitem/searchbarplacement-swift.enum/stacked.md). To prevent the search controller from creating and presenting a search suggestions view controller when the [`searchBarPlacement`](./searchbarplacement.md) is [`UINavigationItem.SearchBarPlacement.stacked`](../uinavigationitem/searchbarplacement-swift.enum/stacked.md), set [`ignoresSearchSuggestionsForSearchBarPlacementStacked`](./ignoressearchsuggestionsforsearchbarplacementstacked.md) to [`true`](../../Swift/true.md) when you create the search controller.

When you assign new suggestions to this property, the suggestions onscreen refresh automatically. When a person selects a suggestion, the system sets this property to `nil` and dismisses the search suggestions menu. Implement [`updateSearchResults(for:selecting:)`](../uisearchresultsupdating/updatesearchresults%28for,selecting%29.md) to execute any necessary updates when a person selects a suggestion.

> **Note**:  In tvOS, when a person selects a search suggestion, the search controller automatically updates the search bar’s [`text`](../uisearchbar/text.md) according to the value of [`localizedSuggestion`](../uisearchsuggestion/localizedsuggestion.md).

If the search suggestions menu dismisses for other reasons, such as a person tapping outside the search bar, [`searchSuggestions`](./searchsuggestions.md) doesn’t reset to `nil` immediately. The system sets [`searchSuggestions`](./searchsuggestions.md) to `nil` only when a person interacts with search directly — for example, by typing in the search field, canceling search, or changing the search scope using the search bar’s scope bar. To dismiss the menu manually, set this property to `nil` or `[]`.

## See Also

### Providing search suggestions
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](./ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [class UISearchSuggestionItem](../uisearchsuggestionitem.md)
  A selectable search parameter.
- [protocol UISearchSuggestion](../uisearchsuggestion.md)
  A set of attributes that a selectable search suggestion must provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/searchsuggestions)*
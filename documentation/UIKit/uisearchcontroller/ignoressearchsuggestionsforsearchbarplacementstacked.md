# ignoresSearchSuggestionsForSearchBarPlacementStacked

**Framework**: UIKit  
**Kind**: property

A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool { get set }
```

#### Discussion

Defaults to [`false`](https://developer.apple.com/documentation/Swift/false). To prevent the search controller from creating and presenting a search suggestions view controller when the [`searchBarPlacement`](uisearchcontroller/searchbarplacement.md) is [`UINavigationItem.SearchBarPlacement.stacked`](uinavigationitem/searchbarplacement-swift.enum/stacked.md), set to [`true`](https://developer.apple.com/documentation/Swift/true) when you create the search controller.

If you set this value to [`true`](https://developer.apple.com/documentation/Swift/true) after the search controller has already displayed search suggestions, it hides the search suggestions view controller and won’t display it again until you set the value to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var obscuresBackgroundDuringPresentation: Bool](uisearchcontroller/obscuresbackgroundduringpresentation.md)
  A Boolean indicating whether to obscure the underlying content during a search.
- [var hidesNavigationBarDuringPresentation: Bool](uisearchcontroller/hidesnavigationbarduringpresentation.md)
  A Boolean indicating whether to hide the navigation bar when searching.
- [var automaticallyShowsCancelButton: Bool](uisearchcontroller/automaticallyshowscancelbutton.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [var automaticallyShowsSearchResultsController: Bool](uisearchcontroller/automaticallyshowssearchresultscontroller.md)
  A Boolean indicating whether the search controller manages the visibility of its results controller.
- [var showsSearchResultsController: Bool](uisearchcontroller/showssearchresultscontroller.md)
  A Boolean indicating whether the search results controller is visible when the search controller is active.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](uisearchcontroller/searchbarplacement.md)
  The placement of the search bar in the navigation bar.
- [var automaticallyShowsScopeBar: Bool](uisearchcontroller/automaticallyshowsscopebar.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.
- [var scopeBarActivation: UISearchController.ScopeBarActivation](uisearchcontroller/scopebaractivation-swift.property.md)
  A mode that determines when the search controller shows and hides the scope bar.
- [UISearchController.ScopeBarActivation](uisearchcontroller/scopebaractivation-swift.enum.md)
  Constants that specify the modes for showing and hiding the scope bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked)*
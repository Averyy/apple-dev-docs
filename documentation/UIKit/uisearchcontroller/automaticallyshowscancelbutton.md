# automaticallyShowsCancelButton

**Framework**: UIKit  
**Kind**: property

A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var automaticallyShowsCancelButton: Bool { get set }
```

#### Discussion

By default, [`UISearchController`](uisearchcontroller.md) shows the search bar’s cancel button when search becomes active and hides it when the user dismisses search. You can take over responsibility for showing and hiding the cancel button by setting this property to [`false`](https://developer.apple.com/documentation/Swift/false). If you set the search bar’s [`showsCancelButton`](uisearchbar/showscancelbutton.md) property, this property becomes [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var obscuresBackgroundDuringPresentation: Bool](uisearchcontroller/obscuresbackgroundduringpresentation.md)
  A Boolean indicating whether to obscure the underlying content during a search.
- [var hidesNavigationBarDuringPresentation: Bool](uisearchcontroller/hidesnavigationbarduringpresentation.md)
  A Boolean indicating whether to hide the navigation bar when searching.
- [var automaticallyShowsSearchResultsController: Bool](uisearchcontroller/automaticallyshowssearchresultscontroller.md)
  A Boolean indicating whether the search controller manages the visibility of its results controller.
- [var showsSearchResultsController: Bool](uisearchcontroller/showssearchresultscontroller.md)
  A Boolean indicating whether the search results controller is visible when the search controller is active.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](uisearchcontroller/searchbarplacement.md)
  The placement of the search bar in the navigation bar.
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [var automaticallyShowsScopeBar: Bool](uisearchcontroller/automaticallyshowsscopebar.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.
- [var scopeBarActivation: UISearchController.ScopeBarActivation](uisearchcontroller/scopebaractivation-swift.property.md)
  A mode that determines when the search controller shows and hides the scope bar.
- [UISearchController.ScopeBarActivation](uisearchcontroller/scopebaractivation-swift.enum.md)
  Constants that specify the modes for showing and hiding the scope bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/automaticallyshowscancelbutton)*
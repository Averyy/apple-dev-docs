# automaticallyShowsSearchResultsController

**Framework**: UIKit  
**Kind**: property

A Boolean indicating whether the search controller manages the visibility of its results controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var automaticallyShowsSearchResultsController: Bool { get set }
```

#### Discussion

The default value for this property is [`true`](https://developer.apple.com/documentation/Swift/true). When it’s [`true`](https://developer.apple.com/documentation/Swift/true), [`UISearchController`](uisearchcontroller.md) automatically shows its results controller based on the contents of its text property. If you set [`showsSearchResultsController`](uisearchcontroller/showssearchresultscontroller.md), this property becomes [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var obscuresBackgroundDuringPresentation: Bool](uisearchcontroller/obscuresbackgroundduringpresentation.md)
  A Boolean indicating whether to obscure the underlying content during a search.
- [var hidesNavigationBarDuringPresentation: Bool](uisearchcontroller/hidesnavigationbarduringpresentation.md)
  A Boolean indicating whether to hide the navigation bar when searching.
- [var automaticallyShowsCancelButton: Bool](uisearchcontroller/automaticallyshowscancelbutton.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/automaticallyshowssearchresultscontroller)*
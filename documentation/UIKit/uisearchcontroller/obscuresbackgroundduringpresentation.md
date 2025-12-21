# obscuresBackgroundDuringPresentation

**Framework**: UIKit  
**Kind**: property

A Boolean indicating whether to obscure the underlying content during a search.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var obscuresBackgroundDuringPresentation: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the search controller obscures the view controller containing your searchable content as soon as the user interacts with the search bar. When this property is [`false`](https://developer.apple.com/documentation/Swift/false), the search controller doesn’t obscure the original view controller. This property controls only whether the original view controller is initially obscured. When the user enters text in the search bar, the search controller immediately displays the search results controller with the results.

If you use the same view controller to display the searchable content and search results, it’s recommended that you set this property to [`false`](https://developer.apple.com/documentation/Swift/false). The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

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
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [var automaticallyShowsScopeBar: Bool](uisearchcontroller/automaticallyshowsscopebar.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.
- [var scopeBarActivation: UISearchController.ScopeBarActivation](uisearchcontroller/scopebaractivation-swift.property.md)
  A mode that determines when the search controller shows and hides the scope bar.
- [UISearchController.ScopeBarActivation](uisearchcontroller/scopebaractivation-swift.enum.md)
  Constants that specify the modes for showing and hiding the scope bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/obscuresbackgroundduringpresentation)*
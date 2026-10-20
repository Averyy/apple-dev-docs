# automaticallyShowsScopeBar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS 13.0+
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: In iOS, use [`scopeBarActivation`](./scopebaractivation-swift.property.md) instead.

## Declaration

```swift
var automaticallyShowsScopeBar: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyShowsScopeBar;
```

#### Discussion

By default, [`UISearchController`](../uisearchcontroller.md) shows the search bar’s scope bar when search becomes active and hides it when the user dismisses the search. Set this to [`false`](../../Swift/false.md) if you want to show and hide the scope bar in your own code. If you set the [`showsScopeBar`](../uisearchbar/showsscopebar.md) property, that also changes this property to [`false`](../../Swift/false.md).

> **Note**:  The search bar doesn’t show its scope bar at all if there are fewer than two titles in the search bar’s [`scopeButtonTitles`](../uisearchbar/scopebuttontitles.md).

## See Also

### Configuring the search interface
- [var obscuresBackgroundDuringPresentation: Bool](./obscuresbackgroundduringpresentation.md)
  A Boolean indicating whether to obscure the underlying content during a search.
- [var hidesNavigationBarDuringPresentation: Bool](./hidesnavigationbarduringpresentation.md)
  A Boolean indicating whether to hide the navigation bar when searching.
- [var automaticallyShowsCancelButton: Bool](./automaticallyshowscancelbutton.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
- [var automaticallyShowsSearchResultsController: Bool](./automaticallyshowssearchresultscontroller.md)
  A Boolean indicating whether the search controller manages the visibility of its results controller.
- [var showsSearchResultsController: Bool](./showssearchresultscontroller.md)
  A Boolean indicating whether the search results controller is visible when the search controller is active.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](./searchbarplacement.md)
  The placement of the search bar in the navigation bar.
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](./ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [var scopeBarActivation: UISearchController.ScopeBarActivation](./scopebaractivation-swift.property.md)
  A mode that determines when the search controller shows and hides the scope bar.
- [UISearchController.ScopeBarActivation](./scopebaractivation-swift.enum.md)
  Constants that specify the modes for showing and hiding the scope bar.
- [var dimsBackgroundDuringPresentation: Bool](./dimsbackgroundduringpresentation.md)
  A Boolean indicating whether to dim the underlying content during a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/automaticallyshowsscopebar)*
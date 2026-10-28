# ignoresSearchSuggestionsForSearchBarPlacementStacked

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool { get set }
```

```objc
@property (nonatomic) BOOL ignoresSearchSuggestionsForSearchBarPlacementStacked;
```

## Discussion

Defaults to [`false`](../../Swift/false.md). To prevent the search controller from creating and presenting a search suggestions view controller when the [`searchBarPlacement`](./searchbarplacement.md) is [`UINavigationItem.SearchBarPlacement.stacked`](../uinavigationitem/searchbarplacement-swift.enum/stacked.md), set to [`true`](../../Swift/true.md) when you create the search controller.

If you set this value to [`true`](../../Swift/true.md) after the search controller has already displayed search suggestions, it hides the search suggestions view controller and won’t display it again until you set the value to [`false`](../../Swift/false.md).

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
- [var scopeBarActivation: UISearchController.ScopeBarActivation](./scopebaractivation-swift.property.md)
  A mode that determines when the search controller shows and hides the scope bar.
- [UISearchController.ScopeBarActivation](./scopebaractivation-swift.enum.md)
  Constants that specify the modes for showing and hiding the scope bar.
- [var automaticallyShowsScopeBar: Bool](./automaticallyshowsscopebar.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.
- [var dimsBackgroundDuringPresentation: Bool](./dimsbackgroundduringpresentation.md)
  A Boolean indicating whether to dim the underlying content during a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked)*
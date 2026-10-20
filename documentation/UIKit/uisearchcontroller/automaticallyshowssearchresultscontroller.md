# automaticallyShowsSearchResultsController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the search controller manages the visibility of its results controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var automaticallyShowsSearchResultsController: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyShowsSearchResultsController;
```

#### Discussion

The default value for this property is [`true`](../../Swift/true.md). When it’s [`true`](../../Swift/true.md), [`UISearchController`](../uisearchcontroller.md) automatically shows its results controller based on the contents of its text property. If you set [`showsSearchResultsController`](./showssearchresultscontroller.md), this property becomes [`false`](../../Swift/false.md).

## See Also

### Configuring the search interface
- [var obscuresBackgroundDuringPresentation: Bool](./obscuresbackgroundduringpresentation.md)
  A Boolean indicating whether to obscure the underlying content during a search.
- [var hidesNavigationBarDuringPresentation: Bool](./hidesnavigationbarduringpresentation.md)
  A Boolean indicating whether to hide the navigation bar when searching.
- [var automaticallyShowsCancelButton: Bool](./automaticallyshowscancelbutton.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s cancel button.
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
- [var automaticallyShowsScopeBar: Bool](./automaticallyshowsscopebar.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.
- [var dimsBackgroundDuringPresentation: Bool](./dimsbackgroundduringpresentation.md)
  A Boolean indicating whether to dim the underlying content during a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/automaticallyshowssearchresultscontroller)*
# obscuresBackgroundDuringPresentation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether to obscure the underlying content during a search.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var obscuresBackgroundDuringPresentation: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL obscuresBackgroundDuringPresentation;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the search controller obscures the view controller containing your searchable content as soon as the user interacts with the search bar. When this property is [`false`](../../Swift/false.md), the search controller doesn’t obscure the original view controller. This property controls only whether the original view controller is initially obscured. When the user enters text in the search bar, the search controller immediately displays the search results controller with the results.

If you use the same view controller to display the searchable content and search results, set this property to [`false`](../../Swift/false.md). The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the search interface
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
- [var automaticallyShowsScopeBar: Bool](./automaticallyshowsscopebar.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.
- [var dimsBackgroundDuringPresentation: Bool](./dimsbackgroundduringpresentation.md)
  A Boolean indicating whether to dim the underlying content during a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/obscuresbackgroundduringpresentation)*
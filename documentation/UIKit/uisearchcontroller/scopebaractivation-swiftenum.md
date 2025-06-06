# UISearchController.ScopeBarActivation

**Framework**: UIKit  
**Kind**: enum

Constants that specify the modes for showing and hiding the scope bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum ScopeBarActivation
```

#### Overview

You use these constants with the [`scopeBarActivation`](uisearchcontroller/scopebaractivation-swift.property.md) property.

## Topics

### Constants
- [UISearchController.ScopeBarActivation.automatic](uisearchcontroller/scopebaractivation-swift.enum/automatic.md)
  A mode in which the system automatically determines when to show and hide the scope bar.
- [UISearchController.ScopeBarActivation.manual](uisearchcontroller/scopebaractivation-swift.enum/manual.md)
  A mode that gives you manual control over when to show and hide the scope bar.
- [UISearchController.ScopeBarActivation.onTextEntry](uisearchcontroller/scopebaractivation-swift.enum/ontextentry.md)
  A mode in which the search controller shows the scope bar when typing begins in the search field, and hides it after search cancellation.
- [UISearchController.ScopeBarActivation.onSearchActivation](uisearchcontroller/scopebaractivation-swift.enum/onsearchactivation.md)
  A mode in which the search controller shows the scope bar when search becomes active, and hides it after search cancellation.
### Initializers
- [init?(rawValue: Int)](uisearchcontroller/scopebaractivation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [var automaticallyShowsScopeBar: Bool](uisearchcontroller/automaticallyshowsscopebar.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.
- [var scopeBarActivation: UISearchController.ScopeBarActivation](uisearchcontroller/scopebaractivation-swift.property.md)
  A mode that determines when the search controller shows and hides the scope bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/scopebaractivation-swift.enum)*
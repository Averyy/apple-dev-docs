# UISearchController.ScopeBarActivation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UISearchControllerScopeBarActivation : NSInteger;
```

#### Overview

You use these constants with the [`scopeBarActivation`](./scopebaractivation-swift.property.md) property.

## Topics

### Constants
- [UISearchController.ScopeBarActivation.automatic](./scopebaractivation-swift.enum/automatic.md)
  A mode in which the system automatically determines when to show and hide the scope bar.
- [UISearchController.ScopeBarActivation.manual](./scopebaractivation-swift.enum/manual.md)
  A mode that gives you manual control over when to show and hide the scope bar.
- [UISearchController.ScopeBarActivation.onTextEntry](./scopebaractivation-swift.enum/ontextentry.md)
  A mode in which the search controller shows the scope bar when typing begins in the search field, and hides it after search cancellation.
- [UISearchController.ScopeBarActivation.onSearchActivation](./scopebaractivation-swift.enum/onsearchactivation.md)
  A mode in which the search controller shows the scope bar when search becomes active, and hides it after search cancellation.
### Initializers
- [init?(rawValue: Int)](./scopebaractivation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var automaticallyShowsScopeBar: Bool](./automaticallyshowsscopebar.md)
  A Boolean indicating whether the search controller manages the visibility of the search bar’s scope bar.
- [var dimsBackgroundDuringPresentation: Bool](./dimsbackgroundduringpresentation.md)
  A Boolean indicating whether to dim the underlying content during a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller/scopebaractivation-swift.enum)*
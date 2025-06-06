# UISearchContainerViewController

**Framework**: UIKit  
**Kind**: class

A view controller that manages the presentation of search results in your interface.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISearchContainerViewController
```

#### Overview

In tvOS, rather than push a [`UISearchController`](uisearchcontroller.md) onto a navigation controller’s stack or use one as a child of another container view controller, embed an instance of this class and let it manage the presentation of the search controller’s content.

[`UISearchContainerViewController`](uisearchcontainerviewcontroller.md) presents its [`UISearchController`](uisearchcontroller.md), instead of containing it. So implement view appearance methods, such as [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) and [`didMove(toParent:)`](uiviewcontroller/didmove(toparent:).md) on both view controllers.

## Topics

### Creating a search container view controller
- [init(searchController: UISearchController)](uisearchcontainerviewcontroller/init(searchcontroller:).md)
  Initializes and returns a search container view controller with the specified search controller object.
### Getting the search controller
- [var searchController: UISearchController](uisearchcontainerviewcontroller/searchcontroller.md)
  The search controller the search container view controller manages.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UISearchController](uisearchcontroller.md)
  A view controller that manages the display of search results based on interactions with a search bar.
- [class UISearchBar](uisearchbar.md)
  A specialized view for receiving search-related information from the user.
- [protocol UISearchResultsUpdating](uisearchresultsupdating.md)
  A set of methods that let you update search results based on information the user enters into the search bar.
- [Displaying searchable content by using a search controller](displaying-searchable-content-by-using-a-search-controller.md)
  Create a user interface with searchable content in a table view.
- [Using suggested searches with a search controller](using-suggested-searches-with-a-search-controller.md)
  Create a search interface with a table view of suggested searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller)*
# UISearchController

**Framework**: UIKit  
**Kind**: class

A view controller that manages the display of search results based on interactions with a search bar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISearchController
```

#### Overview

Use a search controller to provide a standard search experience of the contents of another view controller. When the user interacts with a [`UISearchBar`](uisearchbar.md), the search controller coordinates with a search results controller to display the search results.

In iOS, incorporate the search controller’s [`searchBar`](uisearchcontroller/searchbar.md) into your own view controller’s interface. Display your view controller in whatever way is appropriate for your app. See [`Displaying searchable content by using a search controller`](displaying-searchable-content-by-using-a-search-controller.md) and [`Using suggested searches with a search controller`](using-suggested-searches-with-a-search-controller.md) to learn how to implement a search controller in your app.

In tvOS, start with a [`UISearchContainerViewController`](uisearchcontainerviewcontroller.md) to manage the presentation of the search controller. See [`UIKit Catalog (tvOS): Creating and Customizing UIKit Controls`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/UICatalogFortvOS/Introduction/Intro.html#//apple_ref/doc/uid/TP40016433) to learn how to implement a search controller embedded inside a `UISearchContainerViewController` object.

> **Note**:  Don’t use a [`UISearchContainerViewController`](uisearchcontainerviewcontroller.md) in iOS.

 Don’t use a [`UISearchContainerViewController`](uisearchcontainerviewcontroller.md) in iOS.

##### Display Search Results

Specify a second view controller for displaying search results when you call [`init(searchResultsController:)`](uisearchcontroller/init(searchresultscontroller:).md). When the user interacts with the search bar, the search controller automatically displays the results controller with the results you specify. If your results view is full-screen in tvOS, set the [`searchControllerObservedScrollView`](uisearchcontroller/searchcontrollerobservedscrollview.md) to the results controller as well, so the search bar scrolls with your content view.

Provide a [`UISearchResultsUpdating`](uisearchresultsupdating.md) object to the search controller’s [`searchResultsUpdater`](uisearchcontroller/searchresultsupdater.md) property. Typically, the view controller with your searchable content also acts as the search results updater object, but you can use another object if you prefer. When the user interacts with the search bar, the search controller calls the appropriate [`UISearchResultsUpdating`](uisearchresultsupdating.md) method, giving your object the opportunity to perform the search and update the contents of your search results view.

##### Customize Transitions

To customize the presentation or dismissal of the search results controller, set the search controller’s [`delegate`](uisearchcontroller/delegate.md) property to an object that conforms to the [`UISearchControllerDelegate`](uisearchcontrollerdelegate.md) protocol. Then implement delegate methods in this object to receive presentation and dismissal events from the search controller.

## Topics

### Creating a search controller
- [init(searchResultsController: UIViewController?)](uisearchcontroller/init(searchresultscontroller:).md)
  Creates and returns a search controller with the specified view controller for displaying the results.
- [init?(coder: NSCoder)](uisearchcontroller/init(coder:).md)
  Returns an initialized search controller from data in the specified unarchiver.
- [init(nibName: String?, bundle: Bundle?)](uisearchcontroller/init(nibname:bundle:).md)
  Returns an initialized view controller with the nib file in the specified bundle.
### Responding to presentation and dismissal
- [var delegate: (any UISearchControllerDelegate)?](uisearchcontroller/delegate.md)
  The search controller’s delegate.
- [protocol UISearchControllerDelegate](uisearchcontrollerdelegate.md)
  A set of delegate methods for search controller objects.
### Managing the search results
- [var searchBar: UISearchBar](uisearchcontroller/searchbar.md)
  The search bar to install in your interface.
- [var searchResultsUpdater: (any UISearchResultsUpdating)?](uisearchcontroller/searchresultsupdater.md)
  The object responsible for updating the contents of the search results controller.
- [var searchResultsController: UIViewController?](uisearchcontroller/searchresultscontroller.md)
  The view controller that displays the results of the search.
- [var isActive: Bool](uisearchcontroller/isactive.md)
  The presented state of the search interface.
### Configuring the search interface
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
- [UISearchController.ScopeBarActivation](uisearchcontroller/scopebaractivation-swift.enum.md)
  Constants that specify the modes for showing and hiding the scope bar.
### Providing search suggestions
- [var searchSuggestions: [any UISearchSuggestion]?](uisearchcontroller/searchsuggestions.md)
  A list of suggestions to offer as shortcuts below the search field.
- [var ignoresSearchSuggestionsForSearchBarPlacementStacked: Bool](uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md)
  A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [class UISearchSuggestionItem](uisearchsuggestionitem.md)
  A selectable search parameter.
- [protocol UISearchSuggestion](uisearchsuggestion.md)
  A set of attributes that a selectable search suggestion must provide.
### Deprecated
- [var searchControllerObservedScrollView: UIScrollView?](uisearchcontroller/searchcontrollerobservedscrollview.md)
  The view with which the controller coordinates scrolling animations.
- [var dimsBackgroundDuringPresentation: Bool](uisearchcontroller/dimsbackgroundduringpresentation.md)
  A Boolean indicating whether to dim the underlying content during a search.

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
- [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md)
- [UIViewControllerTransitioningDelegate](uiviewcontrollertransitioningdelegate.md)

## See Also

- [class UISearchContainerViewController](uisearchcontainerviewcontroller.md)
  A view controller that manages the presentation of search results in your interface.
- [class UISearchBar](uisearchbar.md)
  A specialized view for receiving search-related information from the user.
- [protocol UISearchResultsUpdating](uisearchresultsupdating.md)
  A set of methods that let you update search results based on information the user enters into the search bar.
- [Displaying searchable content by using a search controller](displaying-searchable-content-by-using-a-search-controller.md)
  Create a user interface with searchable content in a table view.
- [Using suggested searches with a search controller](using-suggested-searches-with-a-search-controller.md)
  Create a search interface with a table view of suggested searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontroller)*
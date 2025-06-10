# UISearchBar

**Framework**: UIKit  
**Kind**: class

A specialized view for receiving search-related information from the user.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISearchBar
```

#### Overview

[`UISearchBar`](uisearchbar.md) provides a text field for entering text, a search button, a bookmark button, and a cancel button. A search bar doesn’t actually perform any searches. You use a delegate, an object conforming to the [`UISearchBarDelegate`](uisearchbardelegate.md) protocol, to implement the actions when the user enters text or clicks buttons. For details about interacting with the text field, accessing its content, and using tokens, see [`UISearchTextField`](uisearchtextfield.md) and [`UISearchToken`](uisearchtoken.md).

##### Customize Appearance

You can customize the appearance of search bars one at a time, or you can use the appearance proxy (`[UISearchBar appearance]`) to customize the appearance of all search bars in an app.

In general, you should specify a value for the normal state to be used by other states which don’t have a custom value set. Similarly, when a property is dependent on the bar metrics (on iPhone, in landscape orientation bars have a different height from standard), you should specify a value for `UIBarMetricsDefault`.

## Topics

### Creating a search bar
- [convenience init()](uisearchbar/init.md)
  Initializes the search bar to its default state.
- [init?(coder: NSCoder)](uisearchbar/init(coder:).md)
  Creates a search bar from data in a given unarchiver.
- [init(frame: CGRect)](uisearchbar/init(frame:).md)
  Creates a search bar with a specified frame.
### Handling search bar interactions
- [var delegate: (any UISearchBarDelegate)?](uisearchbar/delegate.md)
  The search bar’s delegate object.
- [protocol UISearchBarDelegate](uisearchbardelegate.md)
  A collection of optional methods that you implement to make a search bar control functional.
### Getting the search text
- [var placeholder: String?](uisearchbar/placeholder.md)
  The string to display when there’s no other text in the text field.
- [var prompt: String?](uisearchbar/prompt.md)
  A single line of text displayed at the top of the search bar.
- [var text: String?](uisearchbar/text.md)
  The current or starting search text.
- [var searchTextField: UISearchTextField](uisearchbar/searchtextfield.md)
  The text field that the user enters a search query into.
### Configuring the search bar
- [var isEnabled: Bool](uisearchbar/isenabled.md)
  A Boolean value indicating whether the search bar is in the enabled state.
- [var barTintColor: UIColor?](uisearchbar/bartintcolor.md)
  The tint color to apply to the search bar background.
- [var searchBarStyle: UISearchBar.Style](uisearchbar/searchbarstyle.md)
  A search bar style that specifies the search bar’s appearance.
- [UISearchBar.Style](uisearchbar/style.md)
  Specifies whether the search bar has a background.
- [var tintColor: UIColor!](uisearchbar/tintcolor.md)
  The tint color to apply to key elements in the search bar.
- [var isTranslucent: Bool](uisearchbar/istranslucent.md)
  A Boolean value that indicates whether the search bar is translucent (true) or not (false).
- [var barStyle: UIBarStyle](uisearchbar/barstyle.md)
  A bar style that specifies the search bar’s appearance.
- [enum UIBarStyle](uibarstyle.md)
  Defines the stylistic appearance of different types of views.
### Customizing the keyboard shortcut items
- [var inputAssistantItem: UITextInputAssistantItem](uisearchbar/inputassistantitem.md)
  The input assistant to use for configuring the keyboard’s shortcuts bar.
### Configuring the search interface
- [var showsBookmarkButton: Bool](uisearchbar/showsbookmarkbutton.md)
  A Boolean value indicating whether the bookmark button is displayed.
- [var showsCancelButton: Bool](uisearchbar/showscancelbutton.md)
  A Boolean value indicating whether the cancel button is displayed.
- [func setShowsCancelButton(Bool, animated: Bool)](uisearchbar/setshowscancelbutton(_:animated:).md)
  Sets the display state of the cancel button optionally with animation.
- [var showsSearchResultsButton: Bool](uisearchbar/showssearchresultsbutton.md)
  A Boolean value indicating whether the search results button is displayed.
- [var isSearchResultsButtonSelected: Bool](uisearchbar/issearchresultsbuttonselected.md)
  A Boolean value indicating whether the search results button is selected.
### Customizing the search bar appearance
- [var backgroundImage: UIImage?](uisearchbar/backgroundimage.md)
  The background image for the search bar.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](uisearchbar/backgroundimage(for:barmetrics:).md)
  Returns the image used for the background in a given position and with given metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](uisearchbar/setbackgroundimage(_:for:barmetrics:).md)
  Sets the image to use for the background in a given position and with given metrics.
- [func image(for: UISearchBar.Icon, state: UIControl.State) -> UIImage?](uisearchbar/image(for:state:).md)
  Returns the image for a given search bar icon type and control state.
- [func setImage(UIImage?, for: UISearchBar.Icon, state: UIControl.State)](uisearchbar/setimage(_:for:state:).md)
  Sets the image for a given search bar icon type and control state.
- [func positionAdjustment(for: UISearchBar.Icon) -> UIOffset](uisearchbar/positionadjustment(for:).md)
  Returns the position adjustment for a given icon.
- [func setPositionAdjustment(UIOffset, for: UISearchBar.Icon)](uisearchbar/setpositionadjustment(_:for:).md)
  Returns the position adjustment for a given icon.
- [var inputAccessoryView: UIView?](uisearchbar/inputaccessoryview.md)
  A custom input accessory view for the keyboard of the search bar.
- [func searchFieldBackgroundImage(for: UIControl.State) -> UIImage?](uisearchbar/searchfieldbackgroundimage(for:).md)
  Returns the search text field image for a given state.
- [func setSearchFieldBackgroundImage(UIImage?, for: UIControl.State)](uisearchbar/setsearchfieldbackgroundimage(_:for:).md)
  Sets the search text field image for a given state.
- [var searchFieldBackgroundPositionAdjustment: UIOffset](uisearchbar/searchfieldbackgroundpositionadjustment.md)
  The offset of the search text field background in the search bar.
- [var searchTextPositionAdjustment: UIOffset](uisearchbar/searchtextpositionadjustment.md)
  The offset of the text within the search text field background.
### Configuring scope bar buttons
- [var scopeButtonTitles: [String]?](uisearchbar/scopebuttontitles.md)
  An array of strings indicating the titles of the scope buttons.
- [var selectedScopeButtonIndex: Int](uisearchbar/selectedscopebuttonindex.md)
  The index of the selected scope button.
- [var showsScopeBar: Bool](uisearchbar/showsscopebar.md)
  Specifies whether the scope bar is displayed.
- [func setShowsScope(Bool, animated: Bool)](uisearchbar/setshowsscope(_:animated:).md)
  Specifies whether the scope bar is displayed, optionally using an animation.
### Customizing the scope bar appearance
- [var scopeBarBackgroundImage: UIImage?](uisearchbar/scopebarbackgroundimage.md)
  The background image for the scope bar.
- [func scopeBarButtonBackgroundImage(for: UIControl.State) -> UIImage?](uisearchbar/scopebarbuttonbackgroundimage(for:).md)
  Returns the background image for the scope bar button in a given state.
- [func setScopeBarButtonBackgroundImage(UIImage?, for: UIControl.State)](uisearchbar/setscopebarbuttonbackgroundimage(_:for:).md)
  Sets the background image for the scope bar button in a given state.
- [func scopeBarButtonDividerImage(forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State) -> UIImage?](uisearchbar/scopebarbuttondividerimage(forleftsegmentstate:rightsegmentstate:).md)
  Returns the divider image to use for a given combination of left and right segment states.
- [func setScopeBarButtonDividerImage(UIImage?, forLeftSegmentState: UIControl.State, rightSegmentState: UIControl.State)](uisearchbar/setscopebarbuttondividerimage(_:forleftsegmentstate:rightsegmentstate:).md)
  Sets the divider image to use for a given combination of left and right segment states.
- [func scopeBarButtonTitleTextAttributes(for: UIControl.State) -> [NSAttributedString.Key : Any]?](uisearchbar/scopebarbuttontitletextattributes(for:).md)
  Returns the text attributes for the search bar’s button’s title string for a given state.
- [func setScopeBarButtonTitleTextAttributes([NSAttributedString.Key : Any]?, for: UIControl.State)](uisearchbar/setscopebarbuttontitletextattributes(_:for:).md)
  Sets the text attributes for the search bar’ button’s title string for a given state.
### Managing dictation
- [var isLookToDictateEnabled: Bool](uisearchbar/islooktodictateenabled.md)
- [protocol UILookToDictateCapable](uilooktodictatecapable.md)
### Constants
- [UISearchBar.Icon](uisearchbar/icon.md)
  Constants to identify the icons used in the search bar.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIBarPositioning](uibarpositioning.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UILookToDictateCapable](uilooktodictatecapable.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITextInputTraits](uitextinputtraits.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UISearchContainerViewController](uisearchcontainerviewcontroller.md)
  A view controller that manages the presentation of search results in your interface.
- [class UISearchController](uisearchcontroller.md)
  A view controller that manages the display of search results based on interactions with a search bar.
- [protocol UISearchResultsUpdating](uisearchresultsupdating.md)
  A set of methods that let you update search results based on information the user enters into the search bar.
- [Displaying searchable content by using a search controller](displaying-searchable-content-by-using-a-search-controller.md)
  Create a user interface with searchable content in a table view.
- [Using suggested searches with a search controller](using-suggested-searches-with-a-search-controller.md)
  Create a search interface with a table view of suggested searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar)*
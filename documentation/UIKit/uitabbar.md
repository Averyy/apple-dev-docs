# UITabBar

**Framework**: UIKit  
**Kind**: class

A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITabBar
```

#### Overview

Typically, you use tab bars in conjunction with a [`UITabBarController`](uitabbarcontroller.md) object, but you can also use them as standalone controls in your app. Tab bars always appear across the bottom edge of the screen and display the contents of one or more [`UITabBarItem`](uitabbaritem.md) objects. A tab bar’s appearance can be customized with a background image or tint color to suit the needs of your interface. Tapping an item selects and highlights that item, and you use the selection of the item to enable the corresponding mode for your app.

You can configure tab bars programmatically or in Interface Builder. A [`UITabBarController`](uitabbarcontroller.md) object provides its own tab bar object and you must configure the object provided to you. When creating a tab bar programmatically, use the [`init(frame:)`](uiview/init(frame:).md) method or another view initializer method to set its initial configuration. Use the methods of this class to configure the appearance of the tab bar. For tab bars you create yourself, you also use the methods of this class to specify the items displayed by the tab bar.

> **Note**:  The [`UITabBar`](uitabbar.md) class and [`UIToolbar`](uitoolbar.md) classes have similar appearances but different purposes. Use tab bars to convey and change your app’s mode. Use toolbars to present the user with a set of actions that are relevant to the currently presented content.

A tab bar reports selections and user customizations to its delegate object. For tab bars you create yourself, use the delegate to respond to selections or to the addition, removal, or reordering of items in the tab bar. (A [`UITabBarController`](uitabbarcontroller.md) object acts as the delegate for the tab bar it manages.) For more information on implementing a tab bar delegate, see [`UITabBarDelegate`](uitabbardelegate.md).

##### Configure the Tab Bar Items

You can configure tab bar items using Interface Builder or create and configure them programmatically in your code. Tab bars in Interface Builder come preconfigured with some initial items and you can add, remove, or reorder items as needed. How you configure items at design time depends on whether your tab bar is associated with a [`UITabBarController`](uitabbarcontroller.md) object:

- Configuring your tab bar in Interface Builder:
- When a [`UITabBarController`](uitabbarcontroller.md) object is present, add or remove view controllers to your scene and create relationship segues between the tab bar controller and each new view controller. Creating a relationship segue automatically adds a new item to the tab bar, and deleting an existing relationship segue removes the corresponding tab bar item.
- When a tab bar controller isn’t present, drag tab bar items from the library onto your tab bar.
- Configuring your tab bar programmatically:
- To configure the tab bar associated with a [`UITabBarController`](uitabbarcontroller.md) object, configure the view controllers associated with the tab bar controller. The tab bar automatically obtains its items from the [`tabBarItem`](uiviewcontroller/tabbaritem.md) property of each view controller associated with the tab bar controller.
- To configure tab bar items directly, use the [`setItems(_:animated:)`](uitabbar/setitems(_:animated:).md) method of the tab bar itself.

A tab bar displays all of its tabs onscreen at once, using the [`itemPositioning`](uitabbar/itempositioning-swift.property.md) property to determine how to position items in the available space. If you have more items than can fit in the available space, display only a subset of them and let the user select which tabs are displayed. The [`beginCustomizingItems(_:)`](uitabbar/begincustomizingitems(_:).md) method displays an interface for selecting which tab bar items to display.

The contents of each item are stored in a [`UITabBarItem`](uitabbaritem.md) object. Each item contains a title and an image to display in the tab. You can also use tab bar items to add a badge to the corresponding tab. For more information about creating and configuring items, see [`UITabBarItem`](uitabbaritem.md).

##### Respond to Tab Selections

For tab bars with an associated tab bar controller, the tab bar controller automatically manages selections and displays the appropriate view controller. The only time you have to manage selections yourself is when you create the tab bar without a tab bar controller. The tab bar reports selections to the [`tabBar(_:didSelect:)`](uitabbardelegate/tabbar(_:didselect:).md) method of its [`delegate`](uitabbar/delegate.md) object, which you can use to respond to selection changes. For more information about implementing the delegate object, see [`UITabBarDelegate`](uitabbardelegate.md).

##### Configure a Tab Bar with Interface Builder

The following table lists the attributes that you configure for tab bars in Interface Builder.

| Attribute | Discussion |
| --- | --- |
| Background | The background image to display for the bar. If you specify a stretchable image, the image is stretched to fit the available space; otherwise, the image is tiled. When you configure a background image, the tab bar ignores the tint color information. To set this attribute programmatically, use the [`backgroundImage`](uitabbar/backgroundimage.md) property. |
| Shadow | The custom shadow image for the tab bar. This attribute is ignored if the tab bar does not also have a custom background image. To set this attribute programmatically, use the [`shadowImage`](uitabbar/shadowimage.md) property. |
| Selection | The image to use for the selected tab. To set this attribute programmatically, use the [`selectionIndicatorImage`](uitabbar/selectionindicatorimage.md) property. |
| Image Tint | The tint color to apply to the selected item. To set this attribute programmatically, use the [`tintColor`](uitabbar/tintcolor.md) property. |
| Style | The basic style to apply to the bar. You can configure a tab bar with a dark or light style and the bar can be opaque or translucent. To set the style programmatically, use the [`barStyle`](uitabbar/barstyle.md) and [`isTranslucent`](uitabbar/istranslucent.md) properties. |
| Bar Tint | The tint color to apply to the bar. To set this attribute programmatically, use the [`barTintColor`](uitabbar/bartintcolor.md) property. |
| Item Positioning | The positioning scheme to apply to items. Use this attribute to configure how items are spaced across the length of the tab bar. To set this attribute programmatically, use the [`itemPositioning`](uitabbar/itempositioning-swift.property.md) property. |

##### Internationalize a Tab Bar

To internationalize a tab bar, you must provide localized strings for the tab bar item titles.

For more information, see `Localization`.

##### Make a Tab Bar Accessible

Tab bars are accessible by default.

With VoiceOver enabled on an iOS device, when a user touches a tab in a tab bar, VoiceOver reads the title of the tab, its position in the bar, and whether it’s selected. For example in the iTunes app on iPad, you might hear “Selected, Audiobooks, four of seven” or “Genius, six of seven.”

For general information about making your interface accessible, see [`Accessibility for UIKit`](accessibility-for-uikit.md).

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/navigation-and-search/tab-bars).

## Topics

### Customizing the tab bar behavior
- [var delegate: (any UITabBarDelegate)?](uitabbar/delegate.md)
  The tab bar’s delegate object.
- [protocol UITabBarDelegate](uitabbardelegate.md)
  The [`UITabBarDelegate`](uitabbardelegate.md) protocol defines optional methods for a delegate of a [`UITabBar`](uitabbar.md) object. The [`UITabBar`](uitabbar.md) class provides the ability for the user to reorder, remove, and add items to the tab bar; this process is referred to as customizing the tab bar. The tab bar delegate receives messages when customizing occurs.
### Configuring tab bar items
- [var items: [UITabBarItem]?](uitabbar/items.md)
  The items displayed by the tab bar.
- [func setItems([UITabBarItem]?, animated: Bool)](uitabbar/setitems(_:animated:).md)
  Sets the items on the tab bar, optionally animating any changes into position.
- [var selectedItem: UITabBarItem?](uitabbar/selecteditem.md)
  The currently selected item on the tab bar.
### Customizing tab bar appearance
- [var standardAppearance: UITabBarAppearance](uitabbar/standardappearance.md)
  The appearance settings for a standard-height tab bar.
- [var scrollEdgeAppearance: UITabBarAppearance?](uitabbar/scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var leadingAccessoryView: UIView](uitabbar/leadingaccessoryview.md)
  The view at the leading edge of a tab bar on tvOS.
- [var trailingAccessoryView: UIView](uitabbar/trailingaccessoryview.md)
  The view at the trailing edge of a tab bar on tvOS.
- [var isTranslucent: Bool](uitabbar/istranslucent.md)
  A Boolean value that indicates whether the tab bar is translucent.
- [Legacy customizations](uitabbar-legacy-customizations.md)
  Customize appearance information directly on the tab bar object.
### Supporting user customization of tab bars
- [func beginCustomizingItems([UITabBarItem])](uitabbar/begincustomizingitems(_:).md)
  Presents a standard interface that lets the user customize the contents of the tab bar.
- [func endCustomizing(animated: Bool) -> Bool](uitabbar/endcustomizing(animated:).md)
  Dismisses the standard interface used to customize the tab bar.
- [var isCustomizing: Bool](uitabbar/iscustomizing.md)
  A Boolean value indicating whether the user is currently customizing the tab bar.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
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
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)
  Create a composite interface by combining content from one or more view controllers with other custom views.
- [class UISplitViewController](uisplitviewcontroller.md)
  A container view controller that implements a hierarchical interface.
- [class UINavigationController](uinavigationcontroller.md)
  A container view controller that defines a stack-based scheme for navigating hierarchical content.
- [class UINavigationBar](uinavigationbar.md)
  Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [class UINavigationItem](uinavigationitem.md)
  The items that a navigation bar displays when the associated view controller is visible.
- [class UITabBarController](uitabbarcontroller.md)
  A container view controller that manages a multiselection interface, where the selection determines which child view controller to display.
- [class UITabBarItem](uitabbaritem.md)
  An object that describes an item in a tab bar.
- [class UITab](uitab.md)
  An object that manages a tab in a tab bar.
- [class UITabAccessory](uitabaccessory.md)
- [class UISearchTab](uisearchtab.md)
  A tab subclass that represents the system’s search tab.
- [class UITabGroup](uitabgroup.md)
  An object that manages a collection of tab objects.
- [class UIPageViewController](uipageviewcontroller.md)
  A container view controller that manages navigation between pages of content, where a subview controller manages each page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar)*
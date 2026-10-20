# UITabBarControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods you implement to customize the behavior of a tab bar.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UITabBarControllerDelegate : NSObjectProtocol
```

```objc
@protocol UITabBarControllerDelegate <NSObject>
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](./elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

#### Overview

You use the [`UITabBarControllerDelegate`](./uitabbarcontrollerdelegate.md) protocol when you want to augment the behavior of a tab bar. In particular, you can use it to determine whether specific tabs should be selected, to perform actions after a tab is selected, or to perform actions before or after the user customizes the order of the tabs. After implementing these methods in your custom object, you should then assign that object to the [`delegate`](./uitabbarcontroller/delegate.md) property of the corresponding [`UITabBarController`](./uitabbarcontroller.md) object.

All of the methods in this protocol are optional. For more information on how to use and configure tab bar controllers and their delegates, see [View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

## Topics

### Managing tab bar selections
- [func tabBarController(UITabBarController, shouldSelect: UIViewController) -> Bool](./uitabbarcontrollerdelegate/tabbarcontroller%28_,shouldselect%29.md)
  Asks the delegate whether the specified view controller should be made active.
- [func tabBarController(UITabBarController, didSelect: UIViewController)](./uitabbarcontrollerdelegate/tabbarcontroller%28_,didselect%29.md)
  Tells the delegate that the user selected an item in the tab bar.
### Managing tab bar customizations
- [func tabBarController(UITabBarController, willBeginCustomizing: [UIViewController])](./uitabbarcontrollerdelegate/tabbarcontroller%28_,willbegincustomizing%29.md)
  Tells the delegate that the tab bar customization sheet is about to be displayed.
- [func tabBarController(UITabBarController, willEndCustomizing: [UIViewController], changed: Bool)](./uitabbarcontrollerdelegate/tabbarcontroller%28_,willendcustomizing,changed%29.md)
  Tells the delegate that the tab bar customization sheet is about to be dismissed.
- [func tabBarController(UITabBarController, didEndCustomizing: [UIViewController], changed: Bool)](./uitabbarcontrollerdelegate/tabbarcontroller%28_,didendcustomizing,changed%29.md)
  Tells the delegate that the tab bar customization sheet was dismissed.
### Overriding view rotation settings
- [func tabBarControllerSupportedInterfaceOrientations(UITabBarController) -> UIInterfaceOrientationMask](./uitabbarcontrollerdelegate/tabbarcontrollersupportedinterfaceorientations%28_%29.md)
  Called to allow the delegate to provide the complete set of supported interface orientations for the tab bar controller.
- [func tabBarControllerPreferredInterfaceOrientationForPresentation(UITabBarController) -> UIInterfaceOrientation](./uitabbarcontrollerdelegate/tabbarcontrollerpreferredinterfaceorientationforpresentation%28_%29.md)
  Called to allow the delegate to provide the preferred orientation for presentation of the tab bar controller.
### Supporting custom tab bar transition animations
- [func tabBarController(UITabBarController, animationControllerForTransitionFrom: UIViewController, to: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](./uitabbarcontrollerdelegate/tabbarcontroller%28_,animationcontrollerfortransitionfrom,to%29.md)
  Called to allow the delegate to return a [`UIViewControllerAnimatedTransitioning`](./uiviewcontrolleranimatedtransitioning.md) delegate object for use during a noninteractive tab bar view controller transition.
- [func tabBarController(UITabBarController, interactionControllerFor: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?](./uitabbarcontrollerdelegate/tabbarcontroller%28_,interactioncontrollerfor%29.md)
  Called to allow the delegate to return a [`UIViewControllerInteractiveTransitioning`](./uiviewcontrollerinteractivetransitioning.md) delegate object for use during an animated tab bar transition.
### Instance Methods
- [func tabBarController(UITabBarController, didSelectTab: UITab, previousTab: UITab?)](./uitabbarcontrollerdelegate/tabbarcontroller%28_,didselecttab,previoustab%29.md)
  Tells the delegate that the user selected the specified @c selectedTab in the tab bar controller.
- [func tabBarController(UITabBarController, displayOrderDidChangeFor: UITabGroup)](./uitabbarcontrollerdelegate/tabbarcontroller%28_,displayorderdidchangefor%29.md)
  Notifies the delegate that the display order for the specified tab has been changed by the user.
- [func tabBarController(UITabBarController, displayedViewControllersFor: UITab, proposedViewControllers: [UIViewController]) -> [UIViewController]](./uitabbarcontrollerdelegate/tabbarcontroller%28_,displayedviewcontrollersfor,proposedviewcontrollers%29.md)
  Used with `UITabGroup.managingNavigationController`, this method allows the delegate to customize the displayed view controllers within the navigation stack for each level of selected tab. This method is called by the system if the selected tab in the `UITabBarController` belongs to or is in the hierarchy of a managing tab group (i.e. a `UITabGroup` with a non-nil `managingNavigationController`). By default, if this method is not implemented, the system will build the navigation stack by adding each tab’s `viewController` into the hierarchy, if one exists. This is especially useful to hide certain view controllers when transitioning between compact and regular size classes.
- [func tabBarController(UITabBarController, shouldSelectTab: UITab) -> Bool](./uitabbarcontrollerdelegate/tabbarcontroller%28_,shouldselecttab%29.md)
  Asks the delegate whether the specified tab should be made active.
- [func tabBarController(UITabBarController, tab: UITab, acceptItemsFrom: any UIDropSession)](./uitabbarcontrollerdelegate/tabbarcontroller%28_,tab,acceptitemsfrom%29.md)
  Notifies the delegate to perform a drop into the specified @c tab from the specified session.
- [func tabBarController(UITabBarController, tab: UITab, operationForAcceptingItemsFrom: any UIDropSession) -> UIDropOperation](./uitabbarcontrollerdelegate/tabbarcontroller%28_,tab,operationforacceptingitemsfrom%29.md)
  Asks the delegate for a drop operation to determine if drag items can be dropped into the specified @c tab
- [func tabBarController(UITabBarController, visibilityDidChangeFor: [UITab])](./uitabbarcontrollerdelegate/tabbarcontroller%28_,visibilitydidchangefor%29.md)
  Notifies the delegate when editing has ended and the specified tabs have had their `isHidden` values changed by the user.
- [func tabBarControllerDidEndEditing(UITabBarController)](./uitabbarcontrollerdelegate/tabbarcontrollerdidendediting%28_%29.md)
  Notifies the delegate when the tab bar controller’s current editing state has ended.
- [func tabBarControllerWillBeginEditing(UITabBarController)](./uitabbarcontrollerdelegate/tabbarcontrollerwillbeginediting%28_%29.md)
  Notifies the delegate when the tab bar controller is about to begin editing.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Customizing the tab bar behavior
- [var delegate: (any UITabBarControllerDelegate)?](./uitabbarcontroller/delegate.md)
  The tab bar controller’s delegate object.
- [var tabBarMinimizeBehavior: UITabBarController.MinimizeBehavior](./uitabbarcontroller/tabbarminimizebehavior.md)
  Defines the minimize behavior for the tab bar, if it is supported.
- [UITabBarController.MinimizeBehavior](./uitabbarcontroller/minimizebehavior.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate)*
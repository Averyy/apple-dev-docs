# UIWindow

**Framework**: UIKit  
**Kind**: class

The backdrop for your app’s user interface and the object that dispatches events to your views.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIWindow
```

## Mentions

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)

#### Overview

Windows work with your view controllers to handle events and to perform many other tasks that are fundamental to your app’s operation. UIKit handles most window-related interactions, working with other objects as needed to implement many app behaviors.

You use windows only when you need to do the following:

- Provide a main window to display your app’s content.
- Create additional windows (as needed) to display additional content.

Normally, Xcode provides your app’s main window. New iOS projects use storyboards to define the app’s views. Storyboards require the presence of a [`window`](uiapplicationdelegate/window.md) property on the app delegate object, which the Xcode templates automatically provide. If your app doesn’t use storyboards, you must create this window yourself.

Most apps need only one window, which displays the app’s content on the device’s main screen. Although you can create additional windows on the device’s main screen, extra windows are commonly used to display content on an external screen, as described in [`Presenting content on a connected display`](presenting-content-on-a-connected-display.md).

You also use [`UIWindow`](uiwindow.md) objects for a handful of other tasks:

- Setting the z-axis level of your window, which affects the visibility of the window relative to other windows.
- Showing windows and making them the target of keyboard events.
- Converting coordinate values to and from the window’s coordinate system.
- Changing the root view controller of a window.
- Changing the screen on which the window is displayed.

Windows don’t have any visual appearance of their own. Instead, a window hosts one or more views, which are managed by the window’s root view controller. You configure the root view controller in your storyboards, adding whatever views are appropriate for your interface.

You should rarely need to subclass [`UIWindow`](uiwindow.md). The kinds of behaviors you might implement in a window can usually be implemented in a higher-level view controller more easily. One of the few times you might want to subclass is to override the [`becomeKey()`](uiwindow/becomekey().md) or [`resignKey()`](uiwindow/resignkey().md) methods to implement custom behaviors when a window’s key status changes. For information about how to display a window on a specific screen, see [`UIScreen`](uiscreen.md).

##### Understand Keyboard Interactions

Whereas touch events are delivered to the window where they occurred, events that don’t have a relevant coordinate value are delivered to the . Only one window at a time can be the key window, and you can use a window’s [`isKeyWindow`](uiwindow/iskeywindow.md) property to determine its status. Most of the time, your app’s main window is the key window, but UIKit may designate a different window as needed.

If you need to know which window is key, observe the [`didBecomeKeyNotification`](uiwindow/didbecomekeynotification.md) and [`didResignKeyNotification`](uiwindow/didresignkeynotification.md) notifications. The system sends those notifications on the main actor in response to key window changes in your app. To force a window become key, or to force a window to resign the key status, call the appropriate methods of this class.

## Topics

### Creating a window
- [init(windowScene: UIWindowScene)](uiwindow/init(windowscene:).md)
  Creates a window and associates it with the specified scene object.
### Configuring the window
- [var rootViewController: UIViewController?](uiwindow/rootviewcontroller.md)
  The root view controller for the window.
- [var windowLevel: UIWindow.Level](uiwindow/windowlevel.md)
  The position of the window in the z-axis.
- [UIWindow.Level](uiwindow/level.md)
  The positioning of windows relative to each other.
- [var canResizeToFitContent: Bool](uiwindow/canresizetofitcontent.md)
  A Boolean value that indicates whether the window’s constraint-based content determines its size.
- [var screen: UIScreen](uiwindow/screen.md)
  The screen to display the window on.
### Making windows key
- [var isKeyWindow: Bool](uiwindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window.
- [var canBecomeKey: Bool](uiwindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKeyAndVisible()](uiwindow/makekeyandvisible.md)
  Shows the window and makes it the key window.
- [func makeKey()](uiwindow/makekey.md)
  Makes the window the key window.
- [func becomeKey()](uiwindow/becomekey.md)
  Tells the window that it’s the key window.
- [func resignKey()](uiwindow/resignkey.md)
  Tells the window that it’s no longer the key window.
### Getting related objects
- [var windowScene: UIWindowScene?](uiwindow/windowscene.md)
  The scene containing the window.
- [var avDisplayManager: AVDisplayManager](uiwindow/avdisplaymanager.md)
  The display manager that handles requests for screen resolution, refresh rate, and HDR mode information.
### Converting coordinates
- [func convert(CGPoint, to: UIWindow?) -> CGPoint](uiwindow/convert(_:to:)-687rw.md)
  Converts a point from the current window’s coordinate system to the coordinate system of another window.
- [func convert(CGPoint, from: UIWindow?) -> CGPoint](uiwindow/convert(_:from:)-1gbm1.md)
  Converts a point from the coordinate system of a given window to the coordinate system of the current window.
- [func convert(CGRect, to: UIWindow?) -> CGRect](uiwindow/convert(_:to:)-7k3l0.md)
  Converts a rectangle from the current window’s coordinate system to the coordinate system of another window.
- [func convert(CGRect, from: UIWindow?) -> CGRect](uiwindow/convert(_:from:)-10p2b.md)
  Converts a rectangle from the coordinate system of another window to coordinate system of the current window.
### Sending events
- [func sendEvent(UIEvent)](uiwindow/sendevent(_:).md)
  Dispatches the specified event to its views.
### Responding to window-related notifications
- [class let didBecomeVisibleNotification: NSNotification.Name](uiwindow/didbecomevisiblenotification.md)
  A notification that posts when a window becomes visible.
- [class let didBecomeHiddenNotification: NSNotification.Name](uiwindow/didbecomehiddennotification.md)
  A notification that posts when a window becomes hidden.
- [class let didBecomeKeyNotification: NSNotification.Name](uiwindow/didbecomekeynotification.md)
  A notification that posts whenever a window becomes the key window.
- [class let didResignKeyNotification: NSNotification.Name](uiwindow/didresignkeynotification.md)
  A notification that posts whenever a window resigns its status as main window.
### Responding to keyboard notifications
- [class let keyboardWillShowNotification: NSNotification.Name](uiresponder/keyboardwillshownotification.md)
  A notification that posts immediately prior to displaying the keyboard.
- [class let keyboardDidShowNotification: NSNotification.Name](uiresponder/keyboarddidshownotification.md)
  A notification that posts immediately after displaying the keyboard.
- [class let keyboardWillHideNotification: NSNotification.Name](uiresponder/keyboardwillhidenotification.md)
  A notification that posts immediately prior to dismissing the keyboard.
- [class let keyboardDidHideNotification: NSNotification.Name](uiresponder/keyboarddidhidenotification.md)
  A notification that posts immediately after dismissing the keyboard.
- [class let keyboardWillChangeFrameNotification: NSNotification.Name](uiresponder/keyboardwillchangeframenotification.md)
  A notification that posts immediately prior to a change in the keyboard’s frame.
- [class let keyboardDidChangeFrameNotification: NSNotification.Name](uiresponder/keyboarddidchangeframenotification.md)
  A notification that posts immediately after a change in the keyboard’s frame.
- [class let keyboardAnimationCurveUserInfoKey: String](uiresponder/keyboardanimationcurveuserinfokey.md)
  A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [class let keyboardAnimationDurationUserInfoKey: String](uiresponder/keyboardanimationdurationuserinfokey.md)
  A user info key to retrieve the duration of the keyboard animation in seconds.
- [class let keyboardIsLocalUserInfoKey: String](uiresponder/keyboardislocaluserinfokey.md)
  A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [class let keyboardFrameBeginUserInfoKey: String](uiresponder/keyboardframebeginuserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [class let keyboardFrameEndUserInfoKey: String](uiresponder/keyboardframeenduserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the end of its animation.
### Working with layout guides
- [var safeAreaAspectFitLayoutGuide: any UILayoutGuide & UILayoutGuideAspectFitting](uiwindow/safeareaaspectfitlayoutguide.md)
  A layout guide for placing content of a particular aspect ratio.
- [protocol UILayoutGuideAspectFitting](uilayoutguideaspectfitting.md)
  The interface for a layout guide that supports a particular aspect ratio.

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
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [protocol UICoordinateSpace](uicoordinatespace.md)
  A set of methods for converting between different frames of reference on a screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow)*
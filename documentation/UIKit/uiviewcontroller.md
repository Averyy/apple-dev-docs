# UIViewController

**Framework**: UIKit  
**Kind**: class

An object that manages a view hierarchy for your UIKit app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIViewController
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)
- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)
- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)
- [Responding to memory warnings](responding-to-memory-warnings.md)

#### Overview

The [`UIViewController`](uiviewcontroller.md) class defines the shared behavior that’s common to all view controllers. You rarely create instances of the [`UIViewController`](uiviewcontroller.md) class directly. Instead, you subclass [`UIViewController`](uiviewcontroller.md) and add the methods and properties needed to manage the view controller’s view hierarchy.

A view controller’s main responsibilities include the following:

- Updating the contents of the views, usually in response to changes to the underlying data
- Responding to user interactions with views
- Resizing views and managing the layout of the overall interface
- Coordinating with other objects — including other view controllers — in your app

A view controller is tightly bound to the views it manages and takes part in handling events in its view hierarchy. Specifically, view controllers are [`UIResponder`](uiresponder.md) objects and are inserted into the responder chain between the view controller’s root view and that view’s superview, which typically belongs to a different view controller. If none of the view controller’s views handle an event, the view controller has the option of handling the event or passing it along to the superview.

View controllers are rarely used in isolation. Instead, you often use multiple view controllers, each of which owns a portion of your app’s user interface. For example, one view controller might display a table of items while a different view controller displays the selected item from that table. Usually, only the views from one view controller are visible at a time. A view controller may present a different view controller to display a new set of views, or it may act as a container for other view controllers’ content and animate views however it wants.

##### Subclassing Notes

Every app contains at least one custom subclass of [`UIViewController`](uiviewcontroller.md). More often, apps contain many custom view controllers. Custom view controllers define the overall behaviors of your app, including the app’s appearance and how it responds to user interactions. The following sections provide a brief overview of some of the tasks your custom subclass performs. For detailed information about using and implementing view controllers, see [`View Controller Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

###### Manage Views

Each view controller manages a view hierarchy, the root view of which is stored in the [`view`](uiviewcontroller/view.md) property of this class. The root view acts primarily as a container for the rest of the view hierarchy. The size and position of the root view is determined by the object that owns it, which is either a parent view controller or the app’s window. The view controller that’s owned by the window is the app’s root view controller and its view is sized to fill the window.

View controllers load their views lazily. Accessing the [`view`](uiviewcontroller/view.md) property for the first time loads or creates the view controller’s views. There are several ways to specify the views for a view controller:

- Specify the view controller and its views in your app’s storyboard. Storyboards are the preferred way to specify your views. With a storyboard, you specify the views and their connections to the view controller. You also specify the relationships and segues between your view controllers, which makes it easier to see and modify your app’s behavior.

To load a view controller from a storyboard, call the [`instantiateViewController(withIdentifier:)`](uistoryboard/instantiateviewcontroller(withidentifier:).md) method of the appropriate [`UIStoryboard`](uistoryboard.md) object. The storyboard object creates the view controller and returns it to your code.

- Specify the views for a view controller using a nib file. A nib file lets you specify the views of a single view controller but doesn’t let you define segues or relationships between view controllers. The nib file also stores only minimal information about the view controller itself.

To initialize a view controller object using a nib file, create your view controller class programmatically and initialize it using the [`init(nibName:bundle:)`](uiviewcontroller/init(nibname:bundle:).md) method. When its views are requested, the view controller loads them from the nib file.

- Specify the views for a view controller using the [`loadView()`](uiviewcontroller/loadview().md) method. In that method, create your view hierarchy programmatically and assign the root view of that hierarchy to the view controller’s [`view`](uiviewcontroller/view.md) property.

All of these techniques have the same end result, which is to create the appropriate set of views and expose them through the [`view`](uiviewcontroller/view.md) property.

> ❗ **Important**:  A view controller is the sole owner of its view and any subviews it creates. It’s responsible for creating those views and for relinquishing ownership of them at the appropriate times such as when the view controller itself is released. If you use a storyboard or a nib file to store your view objects, each view controller object automatically gets its own copy of these views when the view controller asks for them. However, if you create your views manually, each view controller must have its own unique set of views. You can’t share views between view controllers.

A view controller’s root view is always sized to fit its assigned space. For other views in your view hierarchy, use Interface Builder to specify the Auto Layout constraints that govern how each view is positioned and sized within its superview’s bounds. You can also create constraints programmatically and add them to your views at appropriate times. For more information about how to create constraints, see [`Auto Layout Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853).

###### Handle View Related Notifications

When the visibility of its views changes, a view controller automatically calls its own methods so that subclasses can respond to the change. Use a method like [`viewIsAppearing(_:)`](uiviewcontroller/viewisappearing(_:).md) to prepare your views to appear onscreen, and use [`viewWillDisappear(_:)`](uiviewcontroller/viewwilldisappear(_:).md) to save changes or other state information. Use other methods to make appropriate changes.

The following image shows the possible visible states for a view controller’s views and the state transitions that can occur. Not all `will` callback methods are paired with only a `did` callback method. You need to ensure that if you start a process in a `will` callback method, you end the process in both the corresponding `did` and the opposite `will` callback method.

![A diagram of four spheres arranged in a circle. The sphere on the right is labeled Appearing and has a clockwise arrow leading to the bottom sphere, which is labeled Appeared. A small dot on the arrow is labeled viewDidAppear. A clockwise arrow leads from the bottom sphere to the left sphere, which is labeled Disappearing. A small dot along the arrow is labeled viewWillDisappear. A clockwise arrow leads from the left sphere to the top sphere, which is labeled Disappeared. Two small dots along the arrow are labeled viewDidDisappear and View removed. A clockwise arrow leads from the top sphere to the right sphere. Three small dots along the arrow are labeled viewWillAppear, View added, and viewIsAppearing.](https://docs-assets.developer.apple.com/published/a941e6911051bdb9476e5c7b33a7eea2/media-1965800%402x.png)

###### Handle View Rotations

As of iOS 8, all rotation-related methods are deprecated. Instead, rotations are treated as a change in the size of the view controller’s view and are therefore reported using the [`viewWillTransition(to:with:)`](uicontentcontainer/viewwilltransition(to:with:).md) method. When the interface orientation changes, UIKit calls this method on the window’s root view controller. That view controller then notifies its child view controllers, propagating the message throughout the view controller hierarchy.

In iOS 6 and iOS 7, your app supports the interface orientations defined in your app’s `Info.plist` file. A view controller can override the [`supportedInterfaceOrientations`](uiviewcontroller/supportedinterfaceorientations.md) method to limit the list of supported orientations. Typically, the system calls this method only on the root view controller of the window or a view controller presented to fill the entire screen; child view controllers use the portion of the window provided for them by their parent view controller and no longer participate directly in decisions about what rotations are supported. The intersection of the app’s orientation mask and the view controller’s orientation mask is used to determine which orientations a view controller can be rotated into.

You can override the [`preferredInterfaceOrientationForPresentation`](uiviewcontroller/preferredinterfaceorientationforpresentation.md) for a view controller that’s intended to be presented full screen in a specific orientation.

When a rotation occurs for a visible view controller, the [`willRotate(to:duration:)`](uiviewcontroller/willrotate(to:duration:).md), [`willAnimateRotation(to:duration:)`](uiviewcontroller/willanimaterotation(to:duration:).md), and [`didRotate(from:)`](uiviewcontroller/didrotate(from:).md) methods are called during the rotation. The [`viewWillLayoutSubviews()`](uiviewcontroller/viewwilllayoutsubviews().md) method is also called after the view is resized and positioned by its parent. If a view controller isn’t visible when an orientation change occurs, then the rotation methods are never called. However, the [`viewWillLayoutSubviews()`](uiviewcontroller/viewwilllayoutsubviews().md) method is called when the view becomes visible.

> **Note**:  At launch time, apps should always set up their interface in a portrait orientation. After the [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) method returns, the app uses the view controller rotation mechanism described above to rotate the views to the appropriate orientation prior to showing the window.

###### Implement a Container View Controller

A custom [`UIViewController`](uiviewcontroller.md) subclass can also act as a container view controller. A container view controller manages the presentation of content of other view controllers it owns, also known as its child view controllers. A child’s view can be presented as-is or in conjunction with views owned by the container view controller.

Your container view controller subclass should declare a public interface to associate its children. The nature of these methods is up to you and depends on the semantics of the container you’re creating. You need to decide how many children can be displayed by your view controller at once, when those children are displayed, and where they appear in your view controller’s view hierarchy. Your view controller class defines what relationships, if any, are shared by the children. By establishing a clean public interface for your container, you ensure that children use its capabilities logically, without accessing too many private details about how your container implements the behavior.

Your container view controller must associate a child view controller with itself before adding the child’s root view to the view hierarchy. This allows iOS to properly route events to child view controllers and the views those controllers manage. Likewise, after it removes a child’s root view from its view hierarchy, it should disconnect that child view controller from itself. To make or break these associations, your container calls specific methods defined by the base class. These methods aren’t intended to be called by clients of your container class; they are to be used only by your container’s implementation to provide the expected containment behavior.

Here are the essential methods you might need to call:

- [`addChild(_:)`](uiviewcontroller/addchild(_:).md)
- [`removeFromParent()`](uiviewcontroller/removefromparent().md)
- [`willMove(toParent:)`](uiviewcontroller/willmove(toparent:).md)
- [`didMove(toParent:)`](uiviewcontroller/didmove(toparent:).md)

> **Note**:  You’re not required to override any methods when creating a container view controller. By default, rotation and appearance callbacks are automatically forwarded to children. You may optionally override the [`shouldAutomaticallyForwardRotationMethods()`](uiviewcontroller/shouldautomaticallyforwardrotationmethods().md) and [`shouldAutomaticallyForwardAppearanceMethods`](uiviewcontroller/shouldautomaticallyforwardappearancemethods.md) methods to take control of this behavior yourself.

###### Manage Memory

Memory is a critical resource in iOS, and view controllers provide built-in support for reducing their memory footprint at critical times. The [`UIViewController`](uiviewcontroller.md) class provides some automatic handling of low-memory conditions through its [`didReceiveMemoryWarning()`](uiviewcontroller/didreceivememorywarning().md) method, which releases unneeded memory.

###### Support State Preservation and Restoration

If you assign a value to the view controller’s [`restorationIdentifier`](uiviewcontroller/restorationidentifier.md) property, the system may ask the view controller to encode itself when the app transitions to the background. When preserved, a view controller preserves the state of any views in its view hierarchy that also have restoration identifiers. View controllers don’t automatically save any other state. If you’re implementing a custom container view controller, you must encode any child view controllers yourself. Each child you encode must have a unique restoration identifier.

For more information about how the system determines which view controllers to preserve and restore, see [`App Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072). To see an example of state preservation and restoration, see [`Restoring your app’s state`](restoring-your-app-s-state.md).

## Topics

### Creating a view controller
- [init(nibName: String?, bundle: Bundle?)](uiviewcontroller/init(nibname:bundle:).md)
  Creates a view controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](uiviewcontroller/init(coder:).md)
  Creates a view controller with data in an unarchiver.
### Getting the storyboard and nib information
- [var storyboard: UIStoryboard?](uiviewcontroller/storyboard.md)
  The storyboard from which the view controller originated.
- [var nibName: String?](uiviewcontroller/nibname.md)
  The name of the view controller’s nib file, if one was specified.
- [var nibBundle: Bundle?](uiviewcontroller/nibbundle.md)
  The view controller’s nib bundle if it exists.
### Managing the view
- [var view: UIView!](uiviewcontroller/view.md)
  The view that the controller manages.
- [var viewIfLoaded: UIView?](uiviewcontroller/viewifloaded.md)
  The view controller’s view, or `nil` if the view isn’t yet loaded.
- [var isViewLoaded: Bool](uiviewcontroller/isviewloaded.md)
  A Boolean value indicating whether the view is currently loaded into memory.
- [func loadView()](uiviewcontroller/loadview.md)
  Creates the view that the controller manages.
- [func viewDidLoad()](uiviewcontroller/viewdidload.md)
  Called after the controller’s view is loaded into memory.
- [func loadViewIfNeeded()](uiviewcontroller/loadviewifneeded.md)
  Loads the view controller’s view if it’s not loaded yet.
- [var title: String?](uiviewcontroller/title.md)
  A localized string that represents the view this controller manages.
- [var preferredContentSize: CGSize](uiviewcontroller/preferredcontentsize.md)
  The preferred size for the view controller’s view.
### Responding to view-related events
- [func viewWillAppear(Bool)](uiviewcontroller/viewwillappear(_:).md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
- [func viewIsAppearing(Bool)](uiviewcontroller/viewisappearing(_:).md)
  Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.
- [func viewDidAppear(Bool)](uiviewcontroller/viewdidappear(_:).md)
  Notifies the view controller that its view was added to a view hierarchy.
- [func viewWillDisappear(Bool)](uiviewcontroller/viewwilldisappear(_:).md)
  Notifies the view controller that its view is about to be removed from a view hierarchy.
- [func viewDidDisappear(Bool)](uiviewcontroller/viewdiddisappear(_:).md)
  Notifies the view controller that its view was removed from a view hierarchy.
- [var isBeingDismissed: Bool](uiviewcontroller/isbeingdismissed.md)
  A Boolean value indicating whether the view controller is in the process of being dismissed by one of its ancestors.
- [var isBeingPresented: Bool](uiviewcontroller/isbeingpresented.md)
  A Boolean value indicating whether the view controller in the process of being presented by one of its ancestors.
- [var isMovingFromParent: Bool](uiviewcontroller/ismovingfromparent.md)
  A Boolean value indicating whether the view controller is moving from a parent view controller.
- [var isMovingToParent: Bool](uiviewcontroller/ismovingtoparent.md)
  A Boolean value indicating whether the view controller is moving to a parent view controller.
### Extending the view’s safe area
- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
  Position views so that they aren’t obstructed by other content.
- [var additionalSafeAreaInsets: UIEdgeInsets](uiviewcontroller/additionalsafeareainsets.md)
  Custom insets that you specify to modify the view controller’s safe area.
- [func viewSafeAreaInsetsDidChange()](uiviewcontroller/viewsafeareainsetsdidchange.md)
  Called to notify the view controller that the safe area insets of its root view changed.
### Managing the view’s margins
- [Positioning content within layout margins](positioning-content-within-layout-margins.md)
  Position views so that they aren’t crowded by other content.
- [var viewRespectsSystemMinimumLayoutMargins: Bool](uiviewcontroller/viewrespectssystemminimumlayoutmargins.md)
  A Boolean value indicating whether the view controller’s view uses the system-defined minimum layout margins.
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](uiviewcontroller/systemminimumlayoutmargins.md)
  The minimum layout margins for the view controller’s root view.
- [func viewLayoutMarginsDidChange()](uiviewcontroller/viewlayoutmarginsdidchange.md)
  Called to notify the view controller that the layout margins of its root view changed.
### Configuring the view’s layout behavior
- [var edgesForExtendedLayout: UIRectEdge](uiviewcontroller/edgesforextendedlayout.md)
  The edges that you extend for your view controller.
- [struct UIRectEdge](uirectedge.md)
  Constants that specify the edges of a rectangle.
- [var extendedLayoutIncludesOpaqueBars: Bool](uiviewcontroller/extendedlayoutincludesopaquebars.md)
  A Boolean value indicating whether or not the extended layout includes opaque bars.
- [func viewWillLayoutSubviews()](uiviewcontroller/viewwilllayoutsubviews.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](uiviewcontroller/viewdidlayoutsubviews.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](uiviewcontroller/updateviewconstraints.md)
  Notifies the view controller when its view needs to update its constraints.
### Configuring the view rotation settings
- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](uiviewcontroller/supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [func setNeedsUpdateOfSupportedInterfaceOrientations()](uiviewcontroller/setneedsupdateofsupportedinterfaceorientations.md)
  Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [var prefersInterfaceOrientationLocked: Bool](uiviewcontroller/prefersinterfaceorientationlocked.md)
  Whether this view controller prefers the scene’s interface orientation to be locked when shown. The default is `NO`. Note that this preference may or may not be honored. See `UIWindowScene.Geometry` for the current state of interface orientation lock.
- [func setNeedsUpdateOfPrefersInterfaceOrientationLocked()](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked.md)
  Call whenever the view controller’s preference for interface orientation lock has changed
- [var childViewControllerForInterfaceOrientationLock: UIViewController?](uiviewcontroller/childviewcontrollerforinterfaceorientationlock.md)
  Override to return a child view controller or nil. If non-nil, that view controller’s preference for interface orientation lock will be used. If nil, `self` is used. Whenever the return value changes, call `setNeedsUpdateOfPrefersInterfaceOrientationLocked()`.
### Performing segues
- [func shouldPerformSegue(withIdentifier: String, sender: Any?) -> Bool](uiviewcontroller/shouldperformsegue(withidentifier:sender:).md)
  Determines whether the segue with the specified identifier should be performed.
- [func prepare(for: UIStoryboardSegue, sender: Any?)](uiviewcontroller/prepare(for:sender:).md)
  Notifies the view controller that a segue is about to be performed.
- [func performSegue(withIdentifier: String, sender: Any?)](uiviewcontroller/performsegue(withidentifier:sender:).md)
  Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [func allowedChildrenForUnwinding(from: UIStoryboardUnwindSegueSource) -> [UIViewController]](uiviewcontroller/allowedchildrenforunwinding(from:).md)
  Returns an array of child view controllers to search for an unwind segue destination.
- [func childContaining(UIStoryboardUnwindSegueSource) -> UIViewController?](uiviewcontroller/childcontaining(_:).md)
  Returns the child view controller that contains the source of the unwind segue.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, sender: Any?) -> Bool](uiviewcontroller/canperformunwindsegueaction(_:from:sender:).md)
  Called on a view controller to determine whether it responds to an unwind action.
- [func unwind(for: UIStoryboardSegue, towards: UIViewController)](uiviewcontroller/unwind(for:towards:).md)
  Called when an unwind segue transitions to a new view controller.
### Presenting a view controller
- [func show(UIViewController, sender: Any?)](uiviewcontroller/show(_:sender:).md)
  Presents a view controller in a primary context.
- [func showDetailViewController(UIViewController, sender: Any?)](uiviewcontroller/showdetailviewcontroller(_:sender:).md)
  Presents a view controller in a secondary (or detail) context.
- [func present(UIViewController, animated: Bool, completion: (() -> Void)?)](uiviewcontroller/present(_:animated:completion:).md)
  Presents a view controller modally.
- [func dismiss(animated: Bool, completion: (() -> Void)?)](uiviewcontroller/dismiss(animated:completion:).md)
  Dismisses the view controller that was presented modally by the view controller.
- [var modalPresentationStyle: UIModalPresentationStyle](uiviewcontroller/modalpresentationstyle.md)
  The presentation style for modal view controllers.
- [enum UIModalPresentationStyle](uimodalpresentationstyle.md)
  Modal presentation styles available when presenting view controllers.
- [var modalTransitionStyle: UIModalTransitionStyle](uiviewcontroller/modaltransitionstyle.md)
  The transition style to use when presenting the view controller.
- [enum UIModalTransitionStyle](uimodaltransitionstyle.md)
  Transition styles available when presenting view controllers.
- [var isModalInPresentation: Bool](uiviewcontroller/ismodalinpresentation.md)
  A Boolean value indicating whether the view controller enforces a modal behavior.
- [var definesPresentationContext: Bool](uiviewcontroller/definespresentationcontext.md)
  A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [var providesPresentationContextTransitionStyle: Bool](uiviewcontroller/providespresentationcontexttransitionstyle.md)
  A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [var disablesAutomaticKeyboardDismissal: Bool](uiviewcontroller/disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.
### Adding a custom transition or presentation
- [var transitioningDelegate: (any UIViewControllerTransitioningDelegate)?](uiviewcontroller/transitioningdelegate.md)
  The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [var transitionCoordinator: (any UIViewControllerTransitionCoordinator)?](uiviewcontroller/transitioncoordinator.md)
  Returns the active transition coordinator object.
- [func targetViewController(forAction: Selector, sender: Any?) -> UIViewController?](uiviewcontroller/targetviewcontroller(foraction:sender:).md)
  Returns the view controller that responds to the action.
- [var presentationController: UIPresentationController?](uiviewcontroller/presentationcontroller.md)
  The presentation controller that’s managing the current view controller.
- [var popoverPresentationController: UIPopoverPresentationController?](uiviewcontroller/popoverpresentationcontroller.md)
  The nearest popover presentation controller that is managing the current view controller.
- [var sheetPresentationController: UISheetPresentationController?](uiviewcontroller/sheetpresentationcontroller.md)
  The sheet presentation controller for the view controller.
- [var activePresentationController: UIPresentationController?](uiviewcontroller/activepresentationcontroller.md)
  The presentation controller that’s managing the view controller.
- [var restoresFocusAfterTransition: Bool](uiviewcontroller/restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.
### Adapting to environment changes
- [func collapseSecondaryViewController(UIViewController, for: UISplitViewController)](uiviewcontroller/collapsesecondaryviewcontroller(_:for:).md)
  Called when a split view controller transitions to a compact-width size class.
- [func separateSecondaryViewController(for: UISplitViewController) -> UIViewController?](uiviewcontroller/separatesecondaryviewcontroller(for:).md)
  Called when a split view controller transitions to a regular-width size class.
### Adjusting the interface style
- [var overrideUserInterfaceStyle: UIUserInterfaceStyle](uiviewcontroller/overrideuserinterfacestyle.md)
  The user interface style adopted by the view controller and all of its children.
- [var preferredUserInterfaceStyle: UIUserInterfaceStyle](uiviewcontroller/preferreduserinterfacestyle.md)
  The preferred interface style for this view controller.
- [var childViewControllerForUserInterfaceStyle: UIViewController?](uiviewcontroller/childviewcontrollerforuserinterfacestyle.md)
  The child view controller that supports the preferred user interface style.
- [func setNeedsUserInterfaceAppearanceUpdate()](uiviewcontroller/setneedsuserinterfaceappearanceupdate.md)
  Notifies the view controller that a change occurred that might affect the preferred interface style.
- [enum UIUserInterfaceStyle](uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.
### Observing trait changes
- [protocol UITraitChangeObservable](uitraitchangeobservable-67e94.md)
  A type that calls your code in reaction to changes in the trait environment.
### Overriding trait values
- [var traitOverrides: UITraitOverrides](uiviewcontroller/traitoverrides-1z1cc.md)
- [struct UITraitOverrides](uitraitoverrides-swift.struct.md)
### Managing child view controllers in a custom container
- [var children: [UIViewController]](uiviewcontroller/children.md)
  An array of view controllers that are children of the current view controller.
- [func addChild(UIViewController)](uiviewcontroller/addchild(_:).md)
  Adds the specified view controller as a child of the current view controller.
- [func removeFromParent()](uiviewcontroller/removefromparent.md)
  Removes the view controller from its parent.
- [func transition(from: UIViewController, to: UIViewController, duration: TimeInterval, options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiviewcontroller/transition(from:to:duration:options:animations:completion:).md)
  Transitions between two of the view controller’s child view controllers.
- [var shouldAutomaticallyForwardAppearanceMethods: Bool](uiviewcontroller/shouldautomaticallyforwardappearancemethods.md)
  Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [func beginAppearanceTransition(Bool, animated: Bool)](uiviewcontroller/beginappearancetransition(_:animated:).md)
  Tells a child controller its appearance is about to change.
- [func endAppearanceTransition()](uiviewcontroller/endappearancetransition.md)
  Tells a child controller its appearance has changed.
- [class let hierarchyInconsistencyException: NSExceptionName](uiviewcontroller/hierarchyinconsistencyexception.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.
### Responding to containment events
- [func willMove(toParent: UIViewController?)](uiviewcontroller/willmove(toparent:).md)
  Called just before the view controller is added or removed from a container view controller.
- [func didMove(toParent: UIViewController?)](uiviewcontroller/didmove(toparent:).md)
  Called after the view controller is added or removed from a container view controller.
### Getting other related view controllers
- [var presentingViewController: UIViewController?](uiviewcontroller/presentingviewcontroller.md)
  The view controller that presented this view controller.
- [var presentedViewController: UIViewController?](uiviewcontroller/presentedviewcontroller.md)
  The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [var parent: UIViewController?](uiviewcontroller/parent.md)
  The parent view controller of the recipient.
- [var splitViewController: UISplitViewController?](uiviewcontroller/splitviewcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a split view controller.
- [var navigationController: UINavigationController?](uiviewcontroller/navigationcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a navigation controller.
- [var tabBarController: UITabBarController?](uiviewcontroller/tabbarcontroller.md)
  The nearest ancestor in the view controller hierarchy that is a tab bar controller.
### Configuring a navigation interface
- [var navigationItem: UINavigationItem](uiviewcontroller/navigationitem.md)
  The navigation item used to represent the view controller in a parent’s navigation bar.
- [var hidesBottomBarWhenPushed: Bool](uiviewcontroller/hidesbottombarwhenpushed.md)
  A Boolean value indicating whether the toolbar at the bottom of the screen is hidden when the view controller is pushed on to a navigation controller.
- [func setToolbarItems([UIBarButtonItem]?, animated: Bool)](uiviewcontroller/settoolbaritems(_:animated:).md)
  Sets the toolbar items to be displayed along with the view controller.
- [var toolbarItems: [UIBarButtonItem]?](uiviewcontroller/toolbaritems.md)
  The toolbar items associated with the view controller.
### Configuring tab bar content
- [var tabBarItem: UITabBarItem!](uiviewcontroller/tabbaritem.md)
  The tab bar item that represents the view controller when added to a tab bar controller.
- [var tabBarObservedScrollView: UIScrollView?](uiviewcontroller/tabbarobservedscrollview.md)
  The full-screen scroll view to synchronize with a scrolling tab bar.
### Working with scrolling content
- [func setContentScrollView(UIScrollView?, for: NSDirectionalRectEdge)](uiviewcontroller/setcontentscrollview(_:for:).md)
  Sets the scroll view that bars observe for the specified edge.
- [func setContentScrollView(UIScrollView?)](uiviewcontroller/setcontentscrollview(_:).md)
  Sets the scroll view that bars observe for all edges of the view.
- [func contentScrollView(for: NSDirectionalRectEdge) -> UIScrollView?](uiviewcontroller/contentscrollview(for:).md)
  Returns the scroll view the view controller observes for the specified edge.
### Indicating missing content
- [var contentUnavailableConfiguration: (any UIContentConfiguration)?](uiviewcontroller/contentunavailableconfiguration-4b95e.md)
  The current content-unavailable configuration of the view controller.
- [var contentUnavailableConfigurationState: UIContentUnavailableConfigurationState](uiviewcontroller/contentunavailableconfigurationstate-7sczw.md)
  The current configuration state of the content-unavailable view.
- [func setNeedsUpdateContentUnavailableConfiguration()](uiviewcontroller/setneedsupdatecontentunavailableconfiguration.md)
  Requests that the system update the content-unavailable configuration for the latest state.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](uiviewcontroller/updatecontentunavailableconfiguration(using:).md)
  Updates the content-unavailable configuration for the provided state.
- [struct UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.
### Supporting app extensions
- [var extensionContext: NSExtensionContext?](uiviewcontroller/extensioncontext.md)
  Returns the extension context of the view controller.
### Coordinating with system gestures
- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md)
  The screen edges for which you want your gestures to take precedence over the system gestures.
- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](uiviewcontroller/childforscreenedgesdeferringsystemgestures.md)
  Returns the child view controller that should be queried to see if its gestures should take precedence.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var prefersHomeIndicatorAutoHidden: Bool](uiviewcontroller/prefershomeindicatorautohidden.md)
  A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [var childForHomeIndicatorAutoHidden: UIViewController?](uiviewcontroller/childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](uiviewcontroller/setneedsupdateofhomeindicatorautohidden.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.
### Working with transitions
- [var preferredTransition: UIViewController.Transition?](uiviewcontroller/preferredtransition.md)
  An object that defines the transition animation when switching to the view controller.
- [UIViewController.Transition](uiviewcontroller/transition.md)
  An object that defines the transition animation when switching to a new view controller.
### Working with focus
- [var focusGroupIdentifier: String?](uiviewcontroller/focusgroupidentifier.md)
  The identifier of the focus group that the view controller belongs to.
### Managing pointer lock state
- [var prefersPointerLocked: Bool](uiviewcontroller/preferspointerlocked.md)
  A Boolean value that indicates whether the view controller prefers to lock the pointer to a specific scene.
- [func setNeedsUpdateOfPrefersPointerLocked()](uiviewcontroller/setneedsupdateofpreferspointerlocked.md)
  Indicates that the view controller changed the pointer lock preference.
- [var childViewControllerForPointerLock: UIViewController?](uiviewcontroller/childviewcontrollerforpointerlock.md)
  A child view controller to query for the pointer lock preference.
### Managing the status bar
- [var prefersStatusBarHidden: Bool](uiviewcontroller/prefersstatusbarhidden.md)
  Specifies whether the view controller prefers the status bar to be hidden or shown.
- [var childForStatusBarHidden: UIViewController?](uiviewcontroller/childforstatusbarhidden.md)
  The view controller to use for determining the hidden state of the status bar.
- [var childForStatusBarStyle: UIViewController?](uiviewcontroller/childforstatusbarstyle.md)
  Called when the system needs the view controller to use for determining status bar style.
- [var preferredStatusBarStyle: UIStatusBarStyle](uiviewcontroller/preferredstatusbarstyle.md)
  The preferred status bar style for the view controller.
- [enum UIStatusBarStyle](uistatusbarstyle.md)
  Constants that describe the style of the device’s status bar.
- [var modalPresentationCapturesStatusBarAppearance: Bool](uiviewcontroller/modalpresentationcapturesstatusbarappearance.md)
  Specifies whether a view controller, presented non-fullscreen, takes over control of status bar appearance from the presenting view controller.
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](uiviewcontroller/preferredstatusbarupdateanimation.md)
  Specifies the animation style to use for hiding and showing the status bar for the view controller.
- [func setNeedsStatusBarAppearanceUpdate()](uiviewcontroller/setneedsstatusbarappearanceupdate.md)
  Indicates to the system that the view controller status bar attributes have changed.
### Managing the Touch Bar
- [var childViewControllerForTouchBar: UIViewController?](uiviewcontroller/childviewcontrollerfortouchbar.md)
  The child view controller that the system uses to display content in the Touch Bar.
- [func setNeedsTouchBarUpdate()](uiviewcontroller/setneedstouchbarupdate.md)
  Tells the system to update the Touch Bar.
### Accessing the available key commands
- [var performsActionsWhilePresentingModally: Bool](uiviewcontroller/performsactionswhilepresentingmodally.md)
  A Boolean value indicating whether the view controller performs menu-related actions.
- [func addKeyCommand(UIKeyCommand)](uiviewcontroller/addkeycommand(_:).md)
  Associates the specified keyboard shortcut with the view controller.
- [func removeKeyCommand(UIKeyCommand)](uiviewcontroller/removekeycommand(_:).md)
  Removes the key command from the view controller.
### Adding editing behaviors to your view controller
- [var isEditing: Bool](uiviewcontroller/isediting.md)
  A Boolean value indicating whether the view controller currently allows the user to edit the view contents.
- [func setEditing(Bool, animated: Bool)](uiviewcontroller/setediting(_:animated:).md)
  Sets whether the view controller shows an editable view.
- [var editButtonItem: UIBarButtonItem](uiviewcontroller/editbuttonitem.md)
  Returns a bar button item that toggles its title and associated state between Edit and Done.
### Handling memory warnings
- [func didReceiveMemoryWarning()](uiviewcontroller/didreceivememorywarning.md)
  Sent to the view controller when the app receives a memory warning.
### Managing state restoration
- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [var restorationIdentifier: String?](uiviewcontroller/restorationidentifier.md)
  The identifier that determines whether the view controller supports state restoration.
- [var restorationClass: (any UIViewControllerRestoration.Type)?](uiviewcontroller/restorationclass.md)
  The class responsible for recreating this view controller when restoring the app’s state.
- [func encodeRestorableState(with: NSCoder)](uiviewcontroller/encoderestorablestate(with:).md)
  Encodes state-related information for the view controller.
- [func decodeRestorableState(with: NSCoder)](uiviewcontroller/decoderestorablestate(with:).md)
  Decodes and restores state-related information for the view controller.
- [func applicationFinishedRestoringState()](uiviewcontroller/applicationfinishedrestoringstate.md)
  Called on restored view controllers after other object decoding is complete.
### Logging user interaction intervals
- [var interactionActivityTrackingBaseName: String?](uiviewcontroller/interactionactivitytrackingbasename.md)
  The base name the view controller uses for logging signposts that annotate user interactions.
### Supporting types
- [UIViewController.ViewLoading](uiviewcontroller/viewloading.md)
  A property wrapper that loads the view controller’s view before accessing the property.
- [enum UIContainerBackgroundStyle](uicontainerbackgroundstyle.md)
### Deprecated
- [Deprecated symbols](uiviewcontroller-deprecated-symbols.md)
  Symbols that view controllers no longer support.
### Structures
- [UIViewController.ShowDetailTargetDidChangeMessage](uiviewcontroller/showdetailtargetdidchangemessage.md)
### Instance Properties
- [var childViewControllerForPreferredContainerBackgroundStyle: UIViewController?](uiviewcontroller/childviewcontrollerforpreferredcontainerbackgroundstyle.md)
- [var ornaments: [UIOrnament]](uiviewcontroller/ornaments.md)
- [var preferredContainerBackgroundStyle: UIContainerBackgroundStyle](uiviewcontroller/preferredcontainerbackgroundstyle.md)
- [var tab: UITab?](uiviewcontroller/tab.md)
### Instance Methods
- [func setNeedsUpdateOfPreferredContainerBackgroundStyle()](uiviewcontroller/setneedsupdateofpreferredcontainerbackgroundstyle.md)
- [func setNeedsUpdateProperties()](uiviewcontroller/setneedsupdateproperties.md)
  Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updateProperties()](uiviewcontroller/updateproperties.md)
  Override point for subclasses to update properties of this view controller or its view. Never call this method directly; use `setNeedsUpdateProperties` to schedule an update.
- [func updatePropertiesIfNeeded()](uiviewcontroller/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
- [func updateTraitsIfNeeded()](uiviewcontroller/updatetraitsifneeded.md)

## Relationships

### Inherits From
- [UIResponder](uiresponder.md)
### Inherited By
- [UIActivityViewController](uiactivityviewcontroller.md)
- [UIAlertController](uialertcontroller.md)
- [UICloudSharingController](uicloudsharingcontroller.md)
- [UICollectionViewController](uicollectionviewcontroller.md)
- [UIColorPickerViewController](uicolorpickerviewcontroller.md)
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
- [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md)
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)
- [UIDocumentViewController](uidocumentviewcontroller.md)
- [UIFontPickerViewController](uifontpickerviewcontroller.md)
- [UIInputViewController](uiinputviewcontroller.md)
- [UINavigationController](uinavigationcontroller.md)
- [UIPageViewController](uipageviewcontroller.md)
- [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md)
- [UISearchContainerViewController](uisearchcontainerviewcontroller.md)
- [UISearchController](uisearchcontroller.md)
- [UISplitViewController](uisplitviewcontroller.md)
- [UITabBarController](uitabbarcontroller.md)
- [UITableViewController](uitableviewcontroller.md)
- [UITextFormattingViewController](uitextformattingviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)
  Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data.
- [Showing and hiding view controllers](showing-and-hiding-view-controllers.md)
  Display view controllers using different techniques, and pass data between them during transitions.
- [class UITableViewController](uitableviewcontroller.md)
  A view controller that specializes in managing a table view.
- [class UICollectionViewController](uicollectionviewcontroller.md)
  A view controller that specializes in managing a collection view.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller)*
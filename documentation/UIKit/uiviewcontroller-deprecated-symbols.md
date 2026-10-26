# Deprecated symbols

**Framework**: UIKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func setOverrideTraitCollection(UITraitCollection?, forChild: UIViewController)](./uiviewcontroller/setoverridetraitcollection%28_,forchild%29.md)
  Changes the traits assigned to the specified child view controller.
- [func overrideTraitCollection(forChild: UIViewController) -> UITraitCollection?](./uiviewcontroller/overridetraitcollection%28forchild%29.md)
  Retrieves the trait collection for a child view controller.
- [class func attemptRotationToDeviceOrientation()](./uiviewcontroller/attemptrotationtodeviceorientation%28%29.md)
  Attempts to rotate all windows to the orientation of the device.
- [func registerForPreviewing(with: any UIViewControllerPreviewingDelegate, sourceView: UIView) -> any UIViewControllerPreviewing](./uiviewcontroller/registerforpreviewing%28with,sourceview%29.md)
  Registers a view controller to participate with 3D Touch preview (peek) and commit (pop).
- [func unregisterForPreviewing(withContext: any UIViewControllerPreviewing)](./uiviewcontroller/unregisterforpreviewing%28withcontext%29.md)
  Unregisters a previously registered view controller identified by its context object.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, withSender: Any) -> Bool](./uiviewcontroller/canperformunwindsegueaction%28_,from,withsender%29.md)
  Called on a view controller to determine whether it wants to respond to an unwind action.
- [func didRotate(from: UIInterfaceOrientation)](./uiviewcontroller/didrotate%28from%29.md)
  Sent to the view controller after the user interface rotates.
- [func dismissMoviePlayerViewControllerAnimated()](./uiviewcontroller/dismissmovieplayerviewcontrolleranimated%28%29.md)
  Dismisses a movie player view controller using the standard movie player transition.
- [func forUnwindSegueAction(Selector, from: UIViewController, withSender: Any?) -> UIViewController?](./uiviewcontroller/forunwindsegueaction%28_,from,withsender%29.md)
  Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action.
- [func presentMoviePlayerViewControllerAnimated(MPMoviePlayerViewController!)](./uiviewcontroller/presentmovieplayerviewcontrolleranimated%28_%29.md)
  Presents the movie player view controller using the standard movie player transition.
- [func rotatingFooterView() -> UIView?](./uiviewcontroller/rotatingfooterview%28%29.md)
  Returns the footer view to transition during an interface orientation change.
- [func rotatingHeaderView() -> UIView?](./uiviewcontroller/rotatingheaderview%28%29.md)
  Returns the header view to transition during an interface orientation change.
- [func segueForUnwinding(to: UIViewController, from: UIViewController, identifier: String?) -> UIStoryboardSegue?](./uiviewcontroller/segueforunwinding%28to,from,identifier%29.md)
  Called when an unwind segue action needs to transition between two view controllers.
- [func shouldAutomaticallyForwardRotationMethods() -> Bool](./uiviewcontroller/shouldautomaticallyforwardrotationmethods%28%29.md)
  Returns a Boolean value indicating whether rotation methods are forwarded to child view controllers.
- [func willAnimateRotation(to: UIInterfaceOrientation, duration: TimeInterval)](./uiviewcontroller/willanimaterotation%28to,duration%29.md)
  Sent to the view controller before performing a one-step user interface rotation.
- [func willRotate(to: UIInterfaceOrientation, duration: TimeInterval)](./uiviewcontroller/willrotate%28to,duration%29.md)
  Sent to the view controller just before the user interface begins rotating.
- [- automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers](./uiviewcontroller/automaticallyforwardappearanceandrotationmethodstochildviewcontrollers.md)
  Returns a Boolean value that indicates whether appearance and rotation methods are forwarded.
- [- didAnimateFirstHalfOfRotationToInterfaceOrientation:](./uiviewcontroller/didanimatefirsthalfofrotationtointerfaceorientation_.md)
  Sent to the view controller after the completion of the first half of the user interface rotation.
- [- dismissModalViewControllerAnimated:](./uiviewcontroller/dismissmodalviewcontrolleranimated_.md)
  Dismisses the view controller that was presented by the receiver.
- [- presentModalViewController:animated:](./uiviewcontroller/presentmodalviewcontroller_animated_.md)
  Presents a modal view managed by the given view controller to the user.
- [- shouldAutorotateToInterfaceOrientation:](./uiviewcontroller/shouldautorotatetointerfaceorientation_.md)
  Returns a Boolean value indicating whether the view controller supports the specified orientation.
- [- viewDidUnload](./uiviewcontroller/viewdidunload.md)
  Called when the controller’s view is released from memory.
- [- viewWillUnload](./uiviewcontroller/viewwillunload.md)
  Called just before releasing the controller’s view from memory.
- [- willAnimateFirstHalfOfRotationToInterfaceOrientation:duration:](./uiviewcontroller/willanimatefirsthalfofrotationtointerfaceorientation_duration_.md)
  Sent to the view controller before performing the first half of a user interface rotation.
- [- willAnimateSecondHalfOfRotationFromInterfaceOrientation:duration:](./uiviewcontroller/willanimatesecondhalfofrotationfrominterfaceorientation_duration_.md)
  Sent to the view controller before the second half of the user interface rotates.
### Deprecated properties
- [var shouldAutorotate: Bool](./uiviewcontroller/shouldautorotate.md)
  A Boolean value that indicates whether the view controller’s contents should autorotate.
- [var previewActionItems: [any UIPreviewActionItem]](./uiviewcontroller/previewactionitems.md)
  The quick actions displayed when a user swipes upward on a 3D Touch preview.
- [var automaticallyAdjustsScrollViewInsets: Bool](./uiviewcontroller/automaticallyadjustsscrollviewinsets.md)
  A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets.
- [var bottomLayoutGuide: any UILayoutSupport](./uiviewcontroller/bottomlayoutguide.md)
  Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [var interfaceOrientation: UIInterfaceOrientation](./uiviewcontroller/interfaceorientation.md)
  Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen.
- [var isModalInPopover: Bool](./uiviewcontroller/ismodalinpopover.md)
  A Boolean value indicating whether the view controller should be presented modally by a popover.
- [var searchDisplayController: UISearchDisplayController?](./uiviewcontroller/searchdisplaycontroller.md)
  The search display controller associated with the view controller.
- [var topLayoutGuide: any UILayoutSupport](./uiviewcontroller/toplayoutguide.md)
  Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints.
- [contentSizeForViewInPopover](./uiviewcontroller/contentsizeforviewinpopover.md)
  The size of the view controller’s view while displayed in a popover.
- [modalViewController](./uiviewcontroller/modalviewcontroller.md)
  The controller for the active presented view’that is, the view that is temporarily displayed on top of the view managed by the receiver.
- [wantsFullScreenLayout](./uiviewcontroller/wantsfullscreenlayout.md)
  A Boolean value indicating whether the view should underlap the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller-deprecated-symbols)*
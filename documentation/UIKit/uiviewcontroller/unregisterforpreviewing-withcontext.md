# unregisterForPreviewing(withContext:)

**Framework**: UIKit  
**Kind**: method

Unregisters a previously registered view controller identified by its context object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func unregisterForPreviewing(withContext previewing: any UIViewControllerPreviewing)
```

#### Discussion

The system calls this method automatically when a 3D Touch-registered view controller is deallocated.

In some circumstances, you must explicitly call this method. This is the case if a registered view controller’s view hierarchy changes state, or if presenting a preview is otherwise no longer possible. In such cases, call this method.

## Parameters

- `previewing`: The context object that was returned when you registered the view controller by calling the   method.

## See Also

- [func setOverrideTraitCollection(UITraitCollection?, forChild: UIViewController)](uiviewcontroller/setoverridetraitcollection(_:forchild:).md)
  Changes the traits assigned to the specified child view controller.
- [func overrideTraitCollection(forChild: UIViewController) -> UITraitCollection?](uiviewcontroller/overridetraitcollection(forchild:).md)
  Retrieves the trait collection for a child view controller.
- [class func attemptRotationToDeviceOrientation()](uiviewcontroller/attemptrotationtodeviceorientation.md)
  Attempts to rotate all windows to the orientation of the device.
- [func registerForPreviewing(with: any UIViewControllerPreviewingDelegate, sourceView: UIView) -> any UIViewControllerPreviewing](uiviewcontroller/registerforpreviewing(with:sourceview:).md)
  Registers a view controller to participate with 3D Touch preview (peek) and commit (pop).
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, withSender: Any) -> Bool](uiviewcontroller/canperformunwindsegueaction(_:from:withsender:).md)
  Called on a view controller to determine whether it wants to respond to an unwind action.
- [func didRotate(from: UIInterfaceOrientation)](uiviewcontroller/didrotate(from:).md)
  Sent to the view controller after the user interface rotates.
- [func dismissMoviePlayerViewControllerAnimated()](uiviewcontroller/dismissmovieplayerviewcontrolleranimated.md)
  Dismisses a movie player view controller using the standard movie player transition.
- [func forUnwindSegueAction(Selector, from: UIViewController, withSender: Any?) -> UIViewController?](uiviewcontroller/forunwindsegueaction(_:from:withsender:).md)
  Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action.
- [func presentMoviePlayerViewControllerAnimated(MPMoviePlayerViewController!)](uiviewcontroller/presentmovieplayerviewcontrolleranimated(_:).md)
  Presents the movie player view controller using the standard movie player transition.
- [func rotatingFooterView() -> UIView?](uiviewcontroller/rotatingfooterview.md)
  Returns the footer view to transition during an interface orientation change.
- [func rotatingHeaderView() -> UIView?](uiviewcontroller/rotatingheaderview.md)
  Returns the header view to transition during an interface orientation change.
- [func segueForUnwinding(to: UIViewController, from: UIViewController, identifier: String?) -> UIStoryboardSegue?](uiviewcontroller/segueforunwinding(to:from:identifier:).md)
  Called when an unwind segue action needs to transition between two view controllers.
- [func shouldAutomaticallyForwardRotationMethods() -> Bool](uiviewcontroller/shouldautomaticallyforwardrotationmethods.md)
  Returns a Boolean value indicating whether rotation methods are forwarded to child view controllers.
- [func willAnimateRotation(to: UIInterfaceOrientation, duration: TimeInterval)](uiviewcontroller/willanimaterotation(to:duration:).md)
  Sent to the view controller before performing a one-step user interface rotation.
- [func willRotate(to: UIInterfaceOrientation, duration: TimeInterval)](uiviewcontroller/willrotate(to:duration:).md)
  Sent to the view controller just before the user interface begins rotating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/unregisterforpreviewing(withcontext:))*
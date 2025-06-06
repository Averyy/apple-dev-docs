# willRotate(to:duration:)

**Framework**: UIKit  
**Kind**: method

Sent to the view controller just before the user interface begins rotating.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration: TimeInterval)
```

#### Discussion

Subclasses may override this method to perform additional actions immediately prior to the rotation. For example, you might use this method to disable view interactions, stop media playback, or temporarily turn off expensive drawing or live updates. You might also use it to swap the current view for one that reflects the new interface orientation. When this method is called, the [`interfaceOrientation`](uiviewcontroller/interfaceorientation.md) property still contains the view’s original orientation. Your implementation of this method must call `super` at some point during its execution.

This method is called regardless of whether your code performs one-step or two-step rotations.

## Parameters

- `toInterfaceOrientation`: The new orientation for the user interface. The possible values are described in  .
- `duration`: The duration of the pending rotation, measured in seconds.

## See Also

- [func setOverrideTraitCollection(UITraitCollection?, forChild: UIViewController)](uiviewcontroller/setoverridetraitcollection(_:forchild:).md)
  Changes the traits assigned to the specified child view controller.
- [func overrideTraitCollection(forChild: UIViewController) -> UITraitCollection?](uiviewcontroller/overridetraitcollection(forchild:).md)
  Retrieves the trait collection for a child view controller.
- [class func attemptRotationToDeviceOrientation()](uiviewcontroller/attemptrotationtodeviceorientation.md)
  Attempts to rotate all windows to the orientation of the device.
- [func registerForPreviewing(with: any UIViewControllerPreviewingDelegate, sourceView: UIView) -> any UIViewControllerPreviewing](uiviewcontroller/registerforpreviewing(with:sourceview:).md)
  Registers a view controller to participate with 3D Touch preview (peek) and commit (pop).
- [func unregisterForPreviewing(withContext: any UIViewControllerPreviewing)](uiviewcontroller/unregisterforpreviewing(withcontext:).md)
  Unregisters a previously registered view controller identified by its context object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/willrotate(to:duration:))*
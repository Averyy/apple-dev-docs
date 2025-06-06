# forUnwindSegueAction(_:from:withSender:)

**Framework**: UIKit  
**Kind**: method

Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func forUnwindSegueAction(_ action: Selector, from fromViewController: UIViewController, withSender sender: Any?) -> UIViewController?
```

#### Return Value

The view controller that wants to handle the unwind action.

#### Discussion

A custom container view controller should override this method and use it to search its children for a view controller to handle the unwind action. It does this by invoking the [`canPerformUnwindSegueAction(_:from:withSender:)`](uiviewcontroller/canperformunwindsegueaction(_:from:withsender:).md) method on each child. If a view controller wants to handle the action, your method should return it. If none of the container’s children want to handle the unwind action, invoke the super’s implementation and return the result of that method.

## Parameters

- `action`: The action that triggered the unwind action.
- `fromViewController`: The view controller that is the source of the unwinding action.
- `sender`: The object that initiated the action.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/forunwindsegueaction(_:from:withsender:))*
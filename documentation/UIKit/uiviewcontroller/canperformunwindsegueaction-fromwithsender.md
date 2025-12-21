# canPerformUnwindSegueAction(_:from:withSender:)

**Framework**: UIKit  
**Kind**: method

Called on a view controller to determine whether it wants to respond to an unwind action.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func canPerformUnwindSegueAction(_ action: Selector, from fromViewController: UIViewController, withSender sender: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the view controller wants to handle the unwind action, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When an unwind segue is triggered, UIKit uses this method and the [`allowedChildrenForUnwinding(from:)`](uiviewcontroller/allowedchildrenforunwinding(from:).md) method to locate a suitable view controller to handle the unwind segue.

The default implementation of this method returns [`true`](https://developer.apple.com/documentation/Swift/true) when the current view controller implements the `action` method and is not the same view controller as the one in the `fromViewController` parameter. You can override this method as needed to change the default behavior. For example, you might return [`false`](https://developer.apple.com/documentation/Swift/false) if the current view controller does not make a suitable return target when unwinding from the specified view controller.

## Parameters

- `action`: The unwind action to invoke on your view controller.
- `fromViewController`: The view controller that initiated the unwind action.
- `sender`: The object that triggered the action.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/canperformunwindsegueaction(_:from:withsender:))*
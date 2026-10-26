# presentModalViewController:animated:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents a modal view managed by the given view controller to the user.

**Availability**:
- iOS 2.0+ - Deprecated in 6.0
- iPadOS 2.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`present(_:animated:completion:)`](./present%28_,animated,completion%29.md) instead.

## Declaration

```objc
- (void) presentModalViewController:(UIViewController *) modalViewController animated:(BOOL) animated;
```

#### Discussion

On iPhone and iPod touch devices, the view of `modalViewController` is always presented full screen. On iPad, the presentation depends on the value in the [`modalPresentationStyle`](./modalpresentationstyle.md) property.

Sets the [`modalViewController`](./modalviewcontroller.md) property to the specified view controller. Resizes its view and attaches it to the view hierarchy. The view is animated according to the transition style specified in the [`modalTransitionStyle`](./modaltransitionstyle.md) property of the controller in the `modalViewController` parameter.

## Parameters

- `modalViewController`: The view controller that manages the modal view.
- `animated`: If [`true`](../../Swift/true.md), animates the view as it’s presented; otherwise, does not.

## See Also

### Deprecated methods
- [func setOverrideTraitCollection(UITraitCollection?, forChild: UIViewController)](./setoverridetraitcollection%28_,forchild%29.md)
  Changes the traits assigned to the specified child view controller.
- [func overrideTraitCollection(forChild: UIViewController) -> UITraitCollection?](./overridetraitcollection%28forchild%29.md)
  Retrieves the trait collection for a child view controller.
- [class func attemptRotationToDeviceOrientation()](./attemptrotationtodeviceorientation%28%29.md)
  Attempts to rotate all windows to the orientation of the device.
- [func registerForPreviewing(with: any UIViewControllerPreviewingDelegate, sourceView: UIView) -> any UIViewControllerPreviewing](./registerforpreviewing%28with,sourceview%29.md)
  Registers a view controller to participate with 3D Touch preview (peek) and commit (pop).
- [func unregisterForPreviewing(withContext: any UIViewControllerPreviewing)](./unregisterforpreviewing%28withcontext%29.md)
  Unregisters a previously registered view controller identified by its context object.
- [- automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers](./automaticallyforwardappearanceandrotationmethodstochildviewcontrollers.md)
  Returns a Boolean value that indicates whether appearance and rotation methods are forwarded.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, withSender: Any) -> Bool](./canperformunwindsegueaction%28_,from,withsender%29.md)
  Called on a view controller to determine whether it wants to respond to an unwind action.
- [- didAnimateFirstHalfOfRotationToInterfaceOrientation:](./didanimatefirsthalfofrotationtointerfaceorientation_.md)
  Sent to the view controller after the completion of the first half of the user interface rotation.
- [func didRotate(from: UIInterfaceOrientation)](./didrotate%28from%29.md)
  Sent to the view controller after the user interface rotates.
- [- dismissModalViewControllerAnimated:](./dismissmodalviewcontrolleranimated_.md)
  Dismisses the view controller that was presented by the receiver.
- [func dismissMoviePlayerViewControllerAnimated()](./dismissmovieplayerviewcontrolleranimated%28%29.md)
  Dismisses a movie player view controller using the standard movie player transition.
- [func forUnwindSegueAction(Selector, from: UIViewController, withSender: Any?) -> UIViewController?](./forunwindsegueaction%28_,from,withsender%29.md)
  Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action.
- [func presentMoviePlayerViewControllerAnimated(MPMoviePlayerViewController!)](./presentmovieplayerviewcontrolleranimated%28_%29.md)
  Presents the movie player view controller using the standard movie player transition.
- [func rotatingFooterView() -> UIView?](./rotatingfooterview%28%29.md)
  Returns the footer view to transition during an interface orientation change.
- [func rotatingHeaderView() -> UIView?](./rotatingheaderview%28%29.md)
  Returns the header view to transition during an interface orientation change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/presentmodalviewcontroller:animated:)*
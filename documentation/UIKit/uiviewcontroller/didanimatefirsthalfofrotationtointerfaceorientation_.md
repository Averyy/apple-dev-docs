# didAnimateFirstHalfOfRotationToInterfaceOrientation:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the view controller after the completion of the first half of the user interface rotation.

**Availability**:
- iOS 2.0+ - Deprecated in 5.0
- iPadOS 2.0+ - Deprecated in 5.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`viewWillTransition(to:with:)`](../uicontentcontainer/viewwilltransition%28to,with%29.md) to make interface-based adjustments.

## Declaration

```objc
- (void) didAnimateFirstHalfOfRotationToInterfaceOrientation:(UIInterfaceOrientation) toInterfaceOrientation;
```

## Discussion

This method is called during two-step rotation animations only. Subclasses can override this method and use it to adjust their views between the first and second half of the animations. This method is called outside of any animation transactions and while any header or footer views are offscreen.

## Parameters

- `toInterfaceOrientation`: The state of the app’s user interface orientation after the rotation. The possible values are described in the [`UIInterfaceOrientation`](../uiinterfaceorientation.md) enum.

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
- [func didRotate(from: UIInterfaceOrientation)](./didrotate%28from%29.md)
  Sent to the view controller after the user interface rotates.
- [- dismissModalViewControllerAnimated:](./dismissmodalviewcontrolleranimated_.md)
  Dismisses the view controller that was presented by the receiver.
- [func dismissMoviePlayerViewControllerAnimated()](./dismissmovieplayerviewcontrolleranimated%28%29.md)
  Dismisses a movie player view controller using the standard movie player transition.
- [func forUnwindSegueAction(Selector, from: UIViewController, withSender: Any?) -> UIViewController?](./forunwindsegueaction%28_,from,withsender%29.md)
  Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action.
- [- presentModalViewController:animated:](./presentmodalviewcontroller_animated_.md)
  Presents a modal view managed by the given view controller to the user.
- [func presentMoviePlayerViewControllerAnimated(MPMoviePlayerViewController!)](./presentmovieplayerviewcontrolleranimated%28_%29.md)
  Presents the movie player view controller using the standard movie player transition.
- [func rotatingFooterView() -> UIView?](./rotatingfooterview%28%29.md)
  Returns the footer view to transition during an interface orientation change.
- [func rotatingHeaderView() -> UIView?](./rotatingheaderview%28%29.md)
  Returns the header view to transition during an interface orientation change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/didanimatefirsthalfofrotationtointerfaceorientation:)*
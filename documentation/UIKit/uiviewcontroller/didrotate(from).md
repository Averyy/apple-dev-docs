# didRotate(from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the view controller after the user interface rotates.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`viewWillTransition(to:with:)`](../uicontentcontainer/viewwilltransition%28to,with%29.md) to make interface-based adjustments.

## Declaration

```swift
func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)
```

```objc
- (void) didRotateFromInterfaceOrientation:(UIInterfaceOrientation) fromInterfaceOrientation;
```

## Discussion

Subclasses may override this method to perform additional actions immediately after the rotation. For example, you might use this method to reenable view interactions, start media playback again, or turn on expensive drawing or live updates. By the time this method is called, the [`interfaceOrientation`](./interfaceorientation.md) property is already set to the new orientation. Your implementation of this method must call `super` at some point during its execution.

This method is called regardless of whether your code performs one-step or two-step rotations.

## Parameters

- `fromInterfaceOrientation`: The old orientation of the user interface. For possible values, see [`UIInterfaceOrientation`](../uiinterfaceorientation.md).

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
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, withSender: Any) -> Bool](./canperformunwindsegueaction%28_,from,withsender%29.md)
  Called on a view controller to determine whether it wants to respond to an unwind action.
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
- [func segueForUnwinding(to: UIViewController, from: UIViewController, identifier: String?) -> UIStoryboardSegue?](./segueforunwinding%28to,from,identifier%29.md)
  Called when an unwind segue action needs to transition between two view controllers.
- [func shouldAutomaticallyForwardRotationMethods() -> Bool](./shouldautomaticallyforwardrotationmethods%28%29.md)
  Returns a Boolean value indicating whether rotation methods are forwarded to child view controllers.
- [func willAnimateRotation(to: UIInterfaceOrientation, duration: TimeInterval)](./willanimaterotation%28to,duration%29.md)
  Sent to the view controller before performing a one-step user interface rotation.
- [func willRotate(to: UIInterfaceOrientation, duration: TimeInterval)](./willrotate%28to,duration%29.md)
  Sent to the view controller just before the user interface begins rotating.
- [- automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers](./automaticallyforwardappearanceandrotationmethodstochildviewcontrollers.md)
  Returns a Boolean value that indicates whether appearance and rotation methods are forwarded.
- [- didAnimateFirstHalfOfRotationToInterfaceOrientation:](./didanimatefirsthalfofrotationtointerfaceorientation_.md)
  Sent to the view controller after the completion of the first half of the user interface rotation.
- [- dismissModalViewControllerAnimated:](./dismissmodalviewcontrolleranimated_.md)
  Dismisses the view controller that was presented by the receiver.
- [- presentModalViewController:animated:](./presentmodalviewcontroller_animated_.md)
  Presents a modal view managed by the given view controller to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/didrotate(from:))*
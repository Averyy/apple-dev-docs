# forUnwindSegueAction(_:from:withSender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when an unwind segue action wants to search a container’s children for a view controller to handle the unwind action.

**Availability**:
- iOS 6.0+ - Deprecated in 9.0
- iPadOS 6.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: Override the [`allowedChildrenForUnwinding(from:)`](./allowedchildrenforunwinding%28from%29.md) method instead.

## Declaration

```swift
func forUnwindSegueAction(_ action: Selector, from fromViewController: UIViewController, withSender sender: Any?) -> UIViewController?
```

```objc
- (UIViewController *) viewControllerForUnwindSegueAction:(SEL) action fromViewController:(UIViewController *) fromViewController withSender:(id) sender;
```

## Return Value

The view controller that wants to handle the unwind action.

## Discussion

A custom container view controller should override this method and use it to search its children for a view controller to handle the unwind action. It does this by invoking the [`canPerformUnwindSegueAction(_:from:withSender:)`](./canperformunwindsegueaction%28_,from,withsender%29.md) method on each child. If a view controller wants to handle the action, your method should return it. If none of the container’s children want to handle the unwind action, invoke the super’s implementation and return the result of that method.

## Parameters

- `action`: The action that triggered the unwind action.
- `fromViewController`: The view controller that is the source of the unwinding action.
- `sender`: The object that initiated the action.

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
- [func didRotate(from: UIInterfaceOrientation)](./didrotate%28from%29.md)
  Sent to the view controller after the user interface rotates.
- [func dismissMoviePlayerViewControllerAnimated()](./dismissmovieplayerviewcontrolleranimated%28%29.md)
  Dismisses a movie player view controller using the standard movie player transition.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/forunwindsegueaction(_:from:withsender:))*
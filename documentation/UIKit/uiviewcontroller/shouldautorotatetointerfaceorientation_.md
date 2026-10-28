# shouldAutorotateToInterfaceOrientation:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the view controller supports the specified orientation.

**Availability**:
- iOS 2.0+ - Deprecated in 6.0
- iPadOS 2.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Override the [`supportedInterfaceOrientations`](./supportedinterfaceorientations.md) and [`preferredInterfaceOrientationForPresentation`](./preferredinterfaceorientationforpresentation.md) methods instead.

## Declaration

```objc
- (BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation) toInterfaceOrientation;
```

## Return Value

[`true`](../../Swift/true.md) if the view controller auto-rotates its view to the specified orientation; otherwise, [`false`](../../Swift/false.md).

## Discussion

By default, this method returns [`true`](../../Swift/true.md) for the [`UIInterfaceOrientation.portrait`](../uiinterfaceorientation/portrait.md) orientation only. If your view controller supports additional orientations, override this method and return [`true`](../../Swift/true.md) for all orientations it supports.

Your implementation of this method should simply return [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md) based on the value in the `interfaceOrientation` parameter. Do not attempt to get the value of the [`interfaceOrientation`](./interfaceorientation.md) property or check the orientation value reported by the [`UIDevice`](../uidevice.md) class. Your view controller is either capable of supporting a given orientation or it is not.

## Parameters

- `toInterfaceOrientation`: The orientation of the app’s user interface after the rotation. The possible values are described in [`UIInterfaceOrientation`](../uiinterfaceorientation.md).

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
- [- presentModalViewController:animated:](./presentmodalviewcontroller_animated_.md)
  Presents a modal view managed by the given view controller to the user.
- [func presentMoviePlayerViewControllerAnimated(MPMoviePlayerViewController!)](./presentmovieplayerviewcontrolleranimated%28_%29.md)
  Presents the movie player view controller using the standard movie player transition.
- [func rotatingFooterView() -> UIView?](./rotatingfooterview%28%29.md)
  Returns the footer view to transition during an interface orientation change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldautorotatetointerfaceorientation:)*
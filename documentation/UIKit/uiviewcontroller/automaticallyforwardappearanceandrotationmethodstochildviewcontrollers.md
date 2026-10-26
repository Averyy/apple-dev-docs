# automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether appearance and rotation methods are forwarded.

**Availability**:
- iOS 5.0+ - Deprecated in 6.0
- iPadOS 5.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Manually forward calls to the [`viewWillTransition(to:with:)`](../uicontentcontainer/viewwilltransition%28to,with%29.md) method as needed.

## Declaration

```objc
- (BOOL) automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers;
```

#### Return Value

A Boolean value that indicates whether appearance and rotation methods are forwarded.

#### Discussion

This method is called to determine whether to automatically forward containment callbacks to the child view controllers.

The default implementation returns [`true`](../../Swift/true.md). Subclasses of the [`UIViewController`](../uiviewcontroller.md) class that implement containment logic may override this method to control how these methods are forwarded. If you override this method and return [`false`](../../Swift/false.md), you are responsible for forwarding the following methods to child view controllers at the appropriate times:

- [`viewWillAppear(_:)`](./viewwillappear%28_%29.md)
- [`viewDidAppear(_:)`](./viewdidappear%28_%29.md)
- [`viewWillDisappear(_:)`](./viewwilldisappear%28_%29.md)
- [`viewDidDisappear(_:)`](./viewdiddisappear%28_%29.md)
- [`willRotate(to:duration:)`](./willrotate%28to,duration%29.md)
- [`willAnimateRotation(to:duration:)`](./willanimaterotation%28to,duration%29.md)
- [`didRotate(from:)`](./didrotate%28from%29.md)

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
- [func rotatingHeaderView() -> UIView?](./rotatingheaderview%28%29.md)
  Returns the header view to transition during an interface orientation change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/automaticallyforwardappearanceandrotationmethodstochildviewcontrollers)*
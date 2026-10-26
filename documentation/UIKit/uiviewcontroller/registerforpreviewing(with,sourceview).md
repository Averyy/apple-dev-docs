# registerForPreviewing(with:sourceView:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers a view controller to participate with 3D Touch preview (peek) and commit (pop).

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: Use [`UIContextMenuInteraction`](../uicontextmenuinteraction.md) instead.

## Declaration

```swift
func registerForPreviewing(with delegate: any UIViewControllerPreviewingDelegate, sourceView: UIView) -> any UIViewControllerPreviewing
```

```objc
- (id<UIViewControllerPreviewing>) registerForPreviewingWithDelegate:(id<UIViewControllerPreviewingDelegate>) delegate sourceView:(UIView *) sourceView;
```

#### Return Value

A context object for managing the preview. This object conforms to the [`UIViewControllerPreviewing`](../uiviewcontrollerpreviewing.md) protocol.

#### Discussion

A preview, or *peek* in end-user terminology, provides additional content related to the view the user pressed (that is, related to the `sourceView` view).

Calling this method does three things:

- Registers the previewing view controller (the one that receives this method call) to participate with 3D Touch preview and commit
- Designates the source view, from the receiver’s view hierarchy, as the view to respond to a forceful touch
- Designates a delegate object for mediating the presentation of the preview (peek) and commit (pop) views as a user requests them in turn by pressing more deeply

You can designate more than one source view for a single registered view controller, but you cannot designate a single view as a source view more than once.

The lifetime of this method’s returned context object is managed by the system. If you need to explicitly unregister a view controller, pass its context object to the [`unregisterForPreviewing(withContext:)`](./unregisterforpreviewing%28withcontext%29.md) method. If you do not unregister a view controller, the system automatically unregisters it when the view controller is deallocated.

## Parameters

- `delegate`: The delegate object mediates the presentation of views from the preview (peek) view controller and the commit (pop) view controller. In practice, these two are typically the same view controller. The delegate performs this mediation through your implementation of the methods of the [`UIViewControllerPreviewingDelegate`](../uiviewcontrollerpreviewingdelegate.md) protocol.
- `sourceView`: The view, in the view hierarchy of the receiver of this method call, that invokes a preview when pressed by the user.

  When lightly pressed, the source view remains visually sharp while surrounding content blurs. When pressed more deeply, the system calls the [`previewingContext(_:viewControllerForLocation:)`](../uiviewcontrollerpreviewingdelegate/previewingcontext%28_,viewcontrollerforlocation%29.md) method in your `delegate` object, which presents the preview (peek) view from another view controller.

## See Also

### Deprecated methods
- [func setOverrideTraitCollection(UITraitCollection?, forChild: UIViewController)](./setoverridetraitcollection%28_,forchild%29.md)
  Changes the traits assigned to the specified child view controller.
- [func overrideTraitCollection(forChild: UIViewController) -> UITraitCollection?](./overridetraitcollection%28forchild%29.md)
  Retrieves the trait collection for a child view controller.
- [class func attemptRotationToDeviceOrientation()](./attemptrotationtodeviceorientation%28%29.md)
  Attempts to rotate all windows to the orientation of the device.
- [func unregisterForPreviewing(withContext: any UIViewControllerPreviewing)](./unregisterforpreviewing%28withcontext%29.md)
  Unregisters a previously registered view controller identified by its context object.
- [func canPerformUnwindSegueAction(Selector, from: UIViewController, withSender: Any) -> Bool](./canperformunwindsegueaction%28_,from,withsender%29.md)
  Called on a view controller to determine whether it wants to respond to an unwind action.
- [func didRotate(from: UIInterfaceOrientation)](./didrotate%28from%29.md)
  Sent to the view controller after the user interface rotates.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/registerforpreviewing(with:sourceview:))*
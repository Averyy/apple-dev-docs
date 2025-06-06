# registerForPreviewing(with:sourceView:)

**Framework**: UIKit  
**Kind**: method

Registers a view controller to participate with 3D Touch preview (peek) and commit (pop).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
func registerForPreviewing(with delegate: any UIViewControllerPreviewingDelegate, sourceView: UIView) -> any UIViewControllerPreviewing
```

#### Return Value

A context object for managing the preview. This object conforms to the [`UIViewControllerPreviewing`](uiviewcontrollerpreviewing.md) protocol.

#### Discussion

A preview, or  in end-user terminology, provides additional content related to the view the user pressed (that is, related to the `sourceView` view).

Calling this method does three things:

- Registers the previewing view controller (the one that receives this method call) to participate with 3D Touch preview and commit
- Designates the source view, from the receiver’s view hierarchy, as the view to respond to a forceful touch
- Designates a delegate object for mediating the presentation of the preview (peek) and commit (pop) views as a user requests them in turn by pressing more deeply

You can designate more than one source view for a single registered view controller, but you cannot designate a single view as a source view more than once.

The lifetime of this method’s returned context object is managed by the system. If you need to explicitly unregister a view controller, pass its context object to the [`unregisterForPreviewing(withContext:)`](uiviewcontroller/unregisterforpreviewing(withcontext:).md) method. If you do not unregister a view controller, the system automatically unregisters it when the view controller is deallocated.

## Parameters

- `delegate`: The delegate object mediates the presentation of views from the preview (peek) view controller and the commit (pop) view controller. In practice, these two are typically the same view controller. The delegate performs this mediation through your implementation of the methods of the   protocol.
- `sourceView`: When lightly pressed, the source view remains visually sharp while surrounding content blurs. When pressed more deeply, the system calls the   method in your   object, which presents the preview (peek) view from another view controller.

## See Also

- [func setOverrideTraitCollection(UITraitCollection?, forChild: UIViewController)](uiviewcontroller/setoverridetraitcollection(_:forchild:).md)
  Changes the traits assigned to the specified child view controller.
- [func overrideTraitCollection(forChild: UIViewController) -> UITraitCollection?](uiviewcontroller/overridetraitcollection(forchild:).md)
  Retrieves the trait collection for a child view controller.
- [class func attemptRotationToDeviceOrientation()](uiviewcontroller/attemptrotationtodeviceorientation.md)
  Attempts to rotate all windows to the orientation of the device.
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
- [func willRotate(to: UIInterfaceOrientation, duration: TimeInterval)](uiviewcontroller/willrotate(to:duration:).md)
  Sent to the view controller just before the user interface begins rotating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/registerforpreviewing(with:sourceview:))*
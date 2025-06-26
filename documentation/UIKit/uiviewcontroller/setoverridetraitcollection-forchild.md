# setOverrideTraitCollection(_:forChild:)

**Framework**: UIKit  
**Kind**: method

Changes the traits assigned to the specified child view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setOverrideTraitCollection(_ collection: UITraitCollection?, forChild childViewController: UIViewController)
```

## Mentions

- [Choosing a specific interface style for your iOS app](choosing-a-specific-interface-style-for-your-ios-app.md)
- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)

#### Discussion

Usually, traits are passed unmodified from the parent view controller to its child view controllers. When implementing a custom container view controller, you can use this method to change the traits of any embedded child view controllers to something more appropriate for your layout. Making such a change alters other view controller behaviors associated with that child. For example, modal presentations behave differently in a horizontally compact versus horizontally regular environment. You might also make such a change to force the same set of traits on the child view controller regardless of the actual trait environment.

## Parameters

- `collection`: The new traits to apply to the child view controller.
- `childViewController`: The child view controller whose trait collection is to be changed.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setoverridetraitcollection(_:forchild:))*
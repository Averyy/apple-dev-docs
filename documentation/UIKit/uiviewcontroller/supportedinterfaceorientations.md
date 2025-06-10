# supportedInterfaceOrientations

**Framework**: UIKit  
**Kind**: property

The interface orientations that the view controller supports.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }
```

#### Discussion

This property returns a bit mask that specifies which orientations the view controller supports. For more information, see [`UIInterfaceOrientationMask`](uiinterfaceorientationmask.md).

When the device orientation changes, the system calls this method on the root view controller or the topmost modal view controller that fills the window. If the view controller supports the new orientation, the system rotates the window and the view controller. The system only calls this method if the view controller’s [`shouldAutorotate`](uiviewcontroller/shouldautorotate.md) method returns [`true`](https://developer.apple.com/documentation/swift/true).

Override this method to declare which orientations the view controller supports. The default value is [`all`](uiinterfaceorientationmask/all.md) for the iPad idiom and [`allButUpsideDown`](uiinterfaceorientationmask/allbutupsidedown.md) for the iPhone idiom. The value you return must not be 0.

To determine whether to rotate, the system compares the view controller’s supported orientations with the app’s supported orientations — as determined by the `Info.plist` file or the app delegate’s [`application(_:supportedInterfaceOrientationsFor:)`](uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:).md) method — and the device’s supported orientations.

> **Note**:  All iPadOS devices support the [`portraitUpsideDown`](uiinterfaceorientationmask/portraitupsidedown.md) orientation. It’s best practice to enable it for the iPad idiom. iOS devices without a Home button, such as iPhone 12, don’t support this orientation. You should disable it entirely for the iPhone idiom.

If your app supports multitasking, the system doesn’t call this method on your view controller because multitasking apps must support all orientations. You can opt out of multitasking by enabling  on your iOS target or by not declaring support for all possible orientations within the `Info.plist` file.

For design guidance, see [`Adaptivity and Layout`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/visual-design/adaptivity-and-layout/) in the iOS Human Interface Guidelines.

## See Also

- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [func setNeedsUpdateOfSupportedInterfaceOrientations()](uiviewcontroller/setneedsupdateofsupportedinterfaceorientations.md)
  Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [var prefersInterfaceOrientationLocked: Bool](uiviewcontroller/prefersinterfaceorientationlocked.md)
  Whether this view controller prefers the scene’s interface orientation to be locked when shown. The default is `NO`. Note that this preference may or may not be honored. See `UIWindowScene.Geometry` for the current state of interface orientation lock.
- [func setNeedsUpdateOfPrefersInterfaceOrientationLocked()](uiviewcontroller/setneedsupdateofprefersinterfaceorientationlocked.md)
  Call whenever the view controller’s preference for interface orientation lock has changed
- [var childViewControllerForInterfaceOrientationLock: UIViewController?](uiviewcontroller/childviewcontrollerforinterfaceorientationlock.md)
  Override to return a child view controller or nil. If non-nil, that view controller’s preference for interface orientation lock will be used. If nil, `self` is used. Whenever the return value changes, call `setNeedsUpdateOfPrefersInterfaceOrientationLocked()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/supportedinterfaceorientations)*
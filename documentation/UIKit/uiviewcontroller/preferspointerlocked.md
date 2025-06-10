# prefersPointerLocked

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the view controller prefers to lock the pointer to a specific scene.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var prefersPointerLocked: Bool { get }
```

#### Discussion

The default is [`false`](https://developer.apple.com/documentation/swift/false). Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) indicates the view controller’s preference to lock the pointer, although the system may not honor the request. Use [`isLocked`](uipointerlockstate/islocked.md) to determine the current pointer lock state. For the system to consider locking the pointer:

- The scene must be full screen, not in Split View or Slide Over, with no other apps in Slide Over.
- The scene must be in the [`UIScene.ActivationState.foregroundActive`](uiscene/activationstate-swift.enum/foregroundactive.md) state.
- For an app built with Mac Catalyst, the app must be in the foreground, and the window that contains the scene ordered to the front.

> **Note**:  Bringing an app built with Mac Catalyst to the foreground doesn’t immediately enable pointer lock. To enable pointer lock, the user must click in the window. To exit pointer lock, users can use Command-tab to switch to another app, or using Command-tilde.

The system continuously monitors the state and when the app no longer satisfies the requirements, it disables the pointer lock. When the lock state changes, the system posts [`didChangeNotification`](uipointerlockstate/didchangenotification.md).

If you change the value of [`prefersPointerLocked`](uiviewcontroller/preferspointerlocked.md), call [`setNeedsUpdateOfPrefersPointerLocked()`](uiviewcontroller/setneedsupdateofpreferspointerlocked().md).

## See Also

- [func setNeedsUpdateOfPrefersPointerLocked()](uiviewcontroller/setneedsupdateofpreferspointerlocked.md)
  Indicates that the view controller changed the pointer lock preference.
- [var childViewControllerForPointerLock: UIViewController?](uiviewcontroller/childviewcontrollerforpointerlock.md)
  A child view controller to query for the pointer lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferspointerlocked)*
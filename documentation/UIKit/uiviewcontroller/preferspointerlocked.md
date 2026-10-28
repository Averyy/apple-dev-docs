# prefersPointerLocked

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view controller prefers to lock the pointer to a specific scene.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var prefersPointerLocked: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL prefersPointerLocked;
```

## Discussion

The default is [`false`](../../Swift/false.md). Setting this property to [`true`](../../Swift/true.md) indicates the view controller’s preference to lock the pointer, although the system may not honor the request. Use [`isLocked`](../uipointerlockstate/islocked.md) to determine the current pointer lock state. For the system to consider locking the pointer:

- The scene must be full screen, not in Split View or Slide Over, with no other apps in Slide Over.
- The scene must be in the [`UIScene.ActivationState.foregroundActive`](../uiscene/activationstate-swift.enum/foregroundactive.md) state.
- For an app built with Mac Catalyst, the app must be in the foreground, and the window that contains the scene ordered to the front.

> **Note**:  Bringing an app built with Mac Catalyst to the foreground doesn’t immediately enable pointer lock. To enable pointer lock, the user must click in the window. To exit pointer lock, users can use Command-tab to switch to another app, or using Command-tilde.

The system continuously monitors the state and when the app no longer satisfies the requirements, it disables the pointer lock. When the lock state changes, the system posts [`didChangeNotification`](../uipointerlockstate/didchangenotification.md).

If you change the value of [`prefersPointerLocked`](./preferspointerlocked.md), call [`setNeedsUpdateOfPrefersPointerLocked()`](./setneedsupdateofpreferspointerlocked%28%29.md).

## See Also

### Managing pointer lock state
- [func setNeedsUpdateOfPrefersPointerLocked()](./setneedsupdateofpreferspointerlocked%28%29.md)
  Indicates that the view controller changed the pointer lock preference.
- [var childViewControllerForPointerLock: UIViewController?](./childviewcontrollerforpointerlock.md)
  A child view controller to query for the pointer lock preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferspointerlocked)*
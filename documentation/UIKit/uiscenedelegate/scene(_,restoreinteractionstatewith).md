# scene(_:restoreInteractionStateWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func scene(_ scene: UIScene, restoreInteractionStateWith stateRestorationActivity: NSUserActivity)
```

```objc
- (void) scene:(UIScene *) scene restoreInteractionStateWithUserActivity:(NSUserActivity *) stateRestorationActivity;
```

## See Also

### Saving the state of the scene
- [Restoring your app’s state](../restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [func stateRestorationActivity(for: UIScene) -> NSUserActivity?](./staterestorationactivity%28for%29.md)
  Returns a user activity object encapsulating the current state of the specified scene.
- [func scene(UIScene, didUpdate: NSUserActivity)](./scene%28_,didupdate%29.md)
  Tells the delegate that the specified activity object was updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:restoreinteractionstatewith:))*
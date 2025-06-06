# scene(_:restoreInteractionStateWith:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scene(_ scene: UIScene, restoreInteractionStateWith stateRestorationActivity: NSUserActivity)
```

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [func stateRestorationActivity(for: UIScene) -> NSUserActivity?](uiscenedelegate/staterestorationactivity(for:).md)
  Returns a user activity object encapsulating the current state of the specified scene.
- [func scene(UIScene, didUpdate: NSUserActivity)](uiscenedelegate/scene(_:didupdate:).md)
  Tells the delegate that the specified activity object was updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:restoreinteractionstatewith:))*
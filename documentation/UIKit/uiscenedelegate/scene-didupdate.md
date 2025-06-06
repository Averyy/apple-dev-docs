# scene(_:didUpdate:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified activity object was updated.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func scene(_ scene: UIScene, didUpdate userActivity: NSUserActivity)
```

#### Discussion

Use this method to add any final data to the specified user activity object. UIKit calls this method on your app’s main thread after calling your [`stateRestorationActivity(for:)`](uiscenedelegate/staterestorationactivity(for:).md) method and after giving other parts of your app an opportunity to update the activity object returned by that method.

## Parameters

- `scene`: The scene handling the activity.
- `userActivity`: The user activity object containing the updated data.

## See Also

- [Restoring your app’s state](restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [func stateRestorationActivity(for: UIScene) -> NSUserActivity?](uiscenedelegate/staterestorationactivity(for:).md)
  Returns a user activity object encapsulating the current state of the specified scene.
- [func scene(UIScene, restoreInteractionStateWith: NSUserActivity)](uiscenedelegate/scene(_:restoreinteractionstatewith:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:didupdate:))*
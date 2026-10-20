# stateRestorationActivity(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a user activity object encapsulating the current state of the specified scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func stateRestorationActivity(for scene: UIScene) -> NSUserActivity?
```

```objc
- (NSUserActivity *) stateRestorationActivityForScene:(UIScene *) scene;
```

#### Discussion

Use this method to return an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object with information about your scene’s current state. Save enough information to be able to restore that state again after UIKit disconnects and then reconnects the scene. User activity objects are a mechanism to record what the user is doing, so you don’t need to manually persist the state of your scene’s UI.

After calling this method, and before archiving the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object and saving it to disk, UIKit lets you add state information as follows:

- If you set a delegate for the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object in your app, UIKit calls the delegate’s [`userActivityWillSave(_:)`](../../Foundation/nsuseractivitydelegate/useractivitywillsave%28_%29.md) method.
- If you assign the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object to the [`userActivity`](../uiresponder/useractivity.md) property of any responders, UIKit calls each responder’s [`updateUserActivityState(_:)`](../uiresponder/updateuseractivitystate%28_%29.md) method.

When reconnecting the scene and restoring state, the user activity provided by this method will be provided in the [`stateRestorationActivity`](../uiscenesession/staterestorationactivity.md) property of [`UISceneSession`](../uiscenesession.md).

## Parameters

- `scene`: The scene whose state information is needed.

## See Also

### Saving the state of the scene
- [Restoring your app’s state](../restoring-your-app-s-state.md)
  Provide continuity for the user by preserving current activities.
- [func scene(UIScene, restoreInteractionStateWith: NSUserActivity)](./scene%28_,restoreinteractionstatewith%29.md)
- [func scene(UIScene, didUpdate: NSUserActivity)](./scene%28_,didupdate%29.md)
  Tells the delegate that the specified activity object was updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenedelegate/staterestorationactivity(for:))*
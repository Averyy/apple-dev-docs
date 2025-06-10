# UISceneCollectionJoinBehavior.preferred

**Framework**: UIKit  
**Kind**: case

A behavior that adds the new scene to the requesting scene’s collection and activate it, or attempts to join a compatible collection.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```swift
case preferred
```

#### Discussion

If [`requestingScene`](uiscene/activationrequestoptions/requestingscene.md) is set, this behavior adds the new scene to its collection and activates it. Otherwise, the scene attempts to join a compatible collection.

## See Also

- [UISceneCollectionJoinBehavior.automatic](uiscenecollectionjoinbehavior/automatic.md)
  A behavior that uses the system preferences for joining collections.
- [UISceneCollectionJoinBehavior.preferredWithoutActivating](uiscenecollectionjoinbehavior/preferredwithoutactivating.md)
  A behavior that adds the new scene to the requesting scene’s collection without activating it, or attempts to join a compatible collection.
- [UISceneCollectionJoinBehavior.disallowed](uiscenecollectionjoinbehavior/disallowed.md)
  A behavior that creates a new collection for the new scene, ignoring system preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenecollectionjoinbehavior/preferred)*
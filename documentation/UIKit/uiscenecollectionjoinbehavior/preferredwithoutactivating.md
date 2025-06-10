# UISceneCollectionJoinBehavior.preferredWithoutActivating

**Framework**: UIKit  
**Kind**: case

A behavior that adds the new scene to the requesting scene’s collection without activating it, or attempts to join a compatible collection.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```swift
case preferredWithoutActivating
```

#### Discussion

If [`requestingScene`](uiscene/activationrequestoptions/requestingscene.md) is set, this behavior adds the new scene without deactivating the [`requestingScene`](uiscene/activationrequestoptions/requestingscene.md). Otherwise, this behavior behaves the same as [`UISceneCollectionJoinBehavior.preferred`](uiscenecollectionjoinbehavior/preferred.md). For example, in apps built with Mac Catalyst, you can use this behavior to open a link in a new tab in the background.

## See Also

- [UISceneCollectionJoinBehavior.automatic](uiscenecollectionjoinbehavior/automatic.md)
  A behavior that uses the system preferences for joining collections.
- [UISceneCollectionJoinBehavior.preferred](uiscenecollectionjoinbehavior/preferred.md)
  A behavior that adds the new scene to the requesting scene’s collection and activate it, or attempts to join a compatible collection.
- [UISceneCollectionJoinBehavior.disallowed](uiscenecollectionjoinbehavior/disallowed.md)
  A behavior that creates a new collection for the new scene, ignoring system preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenecollectionjoinbehavior/preferredwithoutactivating)*
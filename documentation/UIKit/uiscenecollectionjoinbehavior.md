# UISceneCollectionJoinBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A set of behaviors that specify how a new scene joins a scene collection.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```swift
enum UISceneCollectionJoinBehavior
```

```c
enum UISceneCollectionJoinBehavior : NSInteger;
```

## Topics

### Constants
- [UISceneCollectionJoinBehavior.automatic](./uiscenecollectionjoinbehavior/automatic.md)
  A behavior that uses the system preferences for joining collections.
- [UISceneCollectionJoinBehavior.preferred](./uiscenecollectionjoinbehavior/preferred.md)
  A behavior that adds the new scene to the requesting scene’s collection and activate it, or attempts to join a compatible collection.
- [UISceneCollectionJoinBehavior.preferredWithoutActivating](./uiscenecollectionjoinbehavior/preferredwithoutactivating.md)
  A behavior that adds the new scene to the requesting scene’s collection without activating it, or attempts to join a compatible collection.
- [UISceneCollectionJoinBehavior.disallowed](./uiscenecollectionjoinbehavior/disallowed.md)
  A behavior that creates a new collection for the new scene, ignoring system preferences.
### Initializers
- [init?(rawValue: Int)](./uiscenecollectionjoinbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Specifying collection join behavior
- [var collectionJoinBehavior: UISceneCollectionJoinBehavior](./uiscene/activationrequestoptions/collectionjoinbehavior.md)
  The behavior that specifies how a new scene joins a scene collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenecollectionjoinbehavior)*
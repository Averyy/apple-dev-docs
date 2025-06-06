# collectionJoinBehavior

**Framework**: UIKit  
**Kind**: property

The behavior that specifies how a new scene joins a scene collection.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var collectionJoinBehavior: UISceneCollectionJoinBehavior { get set }
```

#### Discussion

A scene collection is a group of scenes that display together. In apps built with Mac Catalyst, you use this behavior to add windows to an [`NSWindowTabGroup`](https://developer.apple.com/documentation/AppKit/NSWindowTabGroup).

## See Also

- [enum UISceneCollectionJoinBehavior](uiscenecollectionjoinbehavior.md)
  A set of behaviors that specify how a new scene joins a scene collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationrequestoptions/collectionjoinbehavior)*
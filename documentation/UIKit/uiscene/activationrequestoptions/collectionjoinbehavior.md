# collectionJoinBehavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The behavior that specifies how a new scene joins a scene collection.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```swift
var collectionJoinBehavior: UISceneCollectionJoinBehavior { get set }
```

```objc
@property (nonatomic, readwrite) UISceneCollectionJoinBehavior collectionJoinBehavior;
```

## Discussion

A scene collection is a group of scenes that display together. In apps built with Mac Catalyst, you use this behavior to add windows to an [`NSWindowTabGroup`](../../../AppKit/nswindowtabgroup.md).

## See Also

### Specifying collection join behavior
- [enum UISceneCollectionJoinBehavior](../../uiscenecollectionjoinbehavior.md)
  A set of behaviors that specify how a new scene joins a scene collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/activationrequestoptions/collectionjoinbehavior)*
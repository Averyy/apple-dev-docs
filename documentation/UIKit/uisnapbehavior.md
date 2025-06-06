# UISnapBehavior

**Framework**: UIKit  
**Kind**: class

A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISnapBehavior
```

#### Overview

A  is any iOS or custom object that conforms to the [`UIDynamicItem`](uidynamicitem.md) protocol. The [`UIView`](uiview.md) and [`UICollectionViewLayoutAttributes`](uicollectionviewlayoutattributes.md) classes implement this protocol starting in iOS 7.0. You can use a custom object as a dynamic item for such purposes as reacting to rotation or position changes computed by a dynamic animator—an instance of the [`UIDynamicAnimator`](uidynamicanimator.md) class.

To use a snap behavior with a dynamic item, perform these two steps:

1. Initialize a new snap behavior with the item using the [`init(item:snapTo:)`](uisnapbehavior/init(item:snapto:).md) method
2. Enable the behavior by adding it to an animator using the [`addBehavior(_:)`](uidynamicanimator/addbehavior(_:).md) method

The coordinate system that pertains to a snap behavior, and the types of dynamic items you can use with the behavior, depend on how you initialized the associated animator. For details, read the Overview of [`UIDynamicAnimator`](uidynamicanimator.md).

You can include a snap behavior in a custom, composite behavior by starting with a [`UIDynamicBehavior`](uidynamicbehavior.md) object and adding a snap behavior with the [`addChildBehavior(_:)`](uidynamicbehavior/addchildbehavior(_:).md) method.  If you want to influence a snap behavior at each step of a dynamic animation, implement the inherited [`action`](uidynamicbehavior/action.md) method.

## Topics

### Initializing a snap behavior
- [init(item: any UIDynamicItem, snapTo: CGPoint)](uisnapbehavior/init(item:snapto:).md)
  Initializes a snap behavior with a dynamic item and a snap point.
### Configuring a snap behavior
- [var snapPoint: CGPoint](uisnapbehavior/snappoint.md)
  The point to which to snap.
- [var damping: CGFloat](uisnapbehavior/damping.md)
  The amount of oscillation of a dynamic item during the conclusion of a snap.

## Relationships

### Inherits From
- [UIDynamicBehavior](uidynamicbehavior.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIDynamicBehavior](uidynamicbehavior.md)
  An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.
- [class UIAttachmentBehavior](uiattachmentbehavior.md)
  A relationship between two dynamic items, or between a dynamic item and an anchor point.
- [class UICollisionBehavior](uicollisionbehavior.md)
  An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.
- [class UIFieldBehavior](uifieldbehavior.md)
  An object that applies field-based physics to dynamic items.
- [class UIGravityBehavior](uigravitybehavior.md)
  An object that applies a gravity-like force to all of its associated dynamic items.
- [class UIPushBehavior](uipushbehavior.md)
  A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisnapbehavior)*
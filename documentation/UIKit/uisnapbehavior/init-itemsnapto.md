# init(item:snapTo:)

**Framework**: UIKit  
**Kind**: init

Initializes a snap behavior with a dynamic item and a snap point.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(item: any UIDynamicItem, snapTo point: CGPoint)
```

#### Return Value

The initialized snap behavior, or `nil` if there was a problem initializing the object.

#### Discussion

At the conclusion of a snap, the rotation value (as indicated by the [`transform`](uidynamicitem/transform.md) property) for a dynamic item is `0`.

## Parameters

- `item`: The dynamic item that you want to apply a snap behavior to.
- `point`: The point that you want the dynamic item to snap to. The coordinate system for the   parameter depends on how you initialize the dynamic animator you’re adding the snap behavior to, as described in the overview of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisnapbehavior/init(item:snapto:))*
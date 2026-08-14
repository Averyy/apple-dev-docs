# USDPrim.ListPosition

**Framework**: USDKit  
**Kind**: enum

Where a new composition arc should be inserted relative to existing arcs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ListPosition
```

## Topics

### Enumeration Cases
- [USDPrim.ListPosition.backOfAppendList](usdprim/listposition/backofappendlist.md)
  Insert at the back of the append list, making this the weakest arc.
- [USDPrim.ListPosition.backOfPrependList](usdprim/listposition/backofprependlist.md)
  Insert at the back of the prepend list.
- [USDPrim.ListPosition.frontOfAppendList](usdprim/listposition/frontofappendlist.md)
  Insert at the front of the append list.
- [USDPrim.ListPosition.frontOfPrependList](usdprim/listposition/frontofprependlist.md)
  Insert at the front of the prepend list, making this the strongest arc.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var references: USDPrim.ReferenceCollection](usdprim/references.md)
  The reference composition arcs on this prim.
- [USDPrim.Reference](usdprim/reference.md)
  A reference to an external layer or asset.
- [USDPrim.ReferenceCollection](usdprim/referencecollection.md)
  Manages reference composition arcs on a prim.
- [USDPrim.Payload](usdprim/payload.md)
  A payload to an external asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/listposition)*
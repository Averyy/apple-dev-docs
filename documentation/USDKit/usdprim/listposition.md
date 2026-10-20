# USDPrim.ListPosition

**Framework**: USDKit  
**Kind**: enum  
**Role**: Enumeration

Where a new composition arc should be inserted relative to existing arcs.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum ListPosition
```

## Topics

### Enumeration Cases
- [USDPrim.ListPosition.backOfAppendList](./listposition/backofappendlist.md)
  Insert at the back of the append list, making this the weakest arc.
- [USDPrim.ListPosition.backOfPrependList](./listposition/backofprependlist.md)
  Insert at the back of the prepend list.
- [USDPrim.ListPosition.frontOfAppendList](./listposition/frontofappendlist.md)
  Insert at the front of the append list.
- [USDPrim.ListPosition.frontOfPrependList](./listposition/frontofprependlist.md)
  Insert at the front of the prepend list, making this the strongest arc.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Composing references and payloads
- [var references: USDPrim.ReferenceCollection](./references.md)
  The reference composition arcs on this prim.
- [USDPrim.Reference](./reference.md)
  A reference to an external layer or asset.
- [USDPrim.ReferenceCollection](./referencecollection.md)
  Manages reference composition arcs on a prim.
- [USDPrim.Payload](./payload.md)
  A payload to an external asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/listposition)*
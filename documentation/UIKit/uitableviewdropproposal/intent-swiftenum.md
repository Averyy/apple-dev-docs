# UITableViewDropProposal.Intent

**Framework**: UIKit  
**Kind**: enum

Constants indicating how you intend to handle a drop.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Intent
```

## Topics

### Constants
- [UITableViewDropProposal.Intent.unspecified](uitableviewdropproposal/intent-swift.enum/unspecified.md)
  No drop proposal was specified.
- [UITableViewDropProposal.Intent.insertAtDestinationIndexPath](uitableviewdropproposal/intent-swift.enum/insertatdestinationindexpath.md)
  Insert the dropped content at the specified index path.
- [UITableViewDropProposal.Intent.insertIntoDestinationIndexPath](uitableviewdropproposal/intent-swift.enum/insertintodestinationindexpath.md)
  Incorporate the dropped content into the row at the specified index path.
- [UITableViewDropProposal.Intent.automatic](uitableviewdropproposal/intent-swift.enum/automatic.md)
  Incorporate the content in an appropriate way based on the drop location.
### Initializers
- [init?(rawValue: Int)](uitableviewdropproposal/intent-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var intent: UITableViewDropProposal.Intent](uitableviewdropproposal/intent-swift.property.md)
  The option to use when incorporating dropped items into your content.
- [enum UIDropOperation](uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropproposal/intent-swift.enum)*
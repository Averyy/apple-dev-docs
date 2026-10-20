# UITableViewDropProposal.Intent

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UITableViewDropIntent : NSInteger;
```

## Topics

### Constants
- [UITableViewDropProposal.Intent.unspecified](./intent-swift.enum/unspecified.md)
  No drop proposal was specified.
- [UITableViewDropProposal.Intent.insertAtDestinationIndexPath](./intent-swift.enum/insertatdestinationindexpath.md)
  Insert the dropped content at the specified index path.
- [UITableViewDropProposal.Intent.insertIntoDestinationIndexPath](./intent-swift.enum/insertintodestinationindexpath.md)
  Incorporate the dropped content into the row at the specified index path.
- [UITableViewDropProposal.Intent.automatic](./intent-swift.enum/automatic.md)
  Incorporate the content in an appropriate way based on the drop location.
### Initializers
- [init?(rawValue: Int)](./intent-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the proposed drop location
- [var intent: UITableViewDropProposal.Intent](./intent-swift.property.md)
  The option to use when incorporating dropped items into your content.
- [enum UIDropOperation](../uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropproposal/intent-swift.enum)*
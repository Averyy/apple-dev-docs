# hasActiveDrop

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the table view is currently tracking a drop session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hasActiveDrop: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the table view is tracking a drop session.

## See Also

- [var dropDelegate: (any UITableViewDropDelegate)?](uitableview/dropdelegate.md)
  The delegate object that manages the dropping of content into the table view.
- [protocol UITableViewDropDelegate](uitableviewdropdelegate.md)
  The interface for handling drops in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/hasactivedrop)*
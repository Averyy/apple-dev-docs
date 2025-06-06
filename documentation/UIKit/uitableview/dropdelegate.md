# dropDelegate

**Framework**: UIKit  
**Kind**: property

The delegate object that manages the dropping of content into the table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var dropDelegate: (any UITableViewDropDelegate)? { get set }
```

## Mentions

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

## See Also

- [protocol UITableViewDropDelegate](uitableviewdropdelegate.md)
  The interface for handling drops in a table view.
- [var hasActiveDrop: Bool](uitableview/hasactivedrop.md)
  A Boolean value that indicates whether the table view is currently tracking a drop session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/dropdelegate)*
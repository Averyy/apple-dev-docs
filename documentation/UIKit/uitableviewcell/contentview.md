# contentView

**Framework**: UIKit  
**Kind**: property

The content view of the cell object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentView: UIView { get }
```

#### Discussion

The content view of a [`UITableViewCell`](uitableviewcell.md) object is the default superview for content that the cell displays. If you want to customize cells by simply adding additional views, you should add them to the content view so they position appropriately as the cell transitions in to and out of editing mode.

## See Also

- [var backgroundView: UIView?](uitableviewcell/backgroundview.md)
  The view to use as the background of the cell.
- [func defaultContentConfiguration() -> UIListContentConfiguration](uitableviewcell/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the cell’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](uitableviewcell/contentconfiguration-9ktox.md)
  The current content configuration of the cell.
- [var automaticallyUpdatesContentConfiguration: Bool](uitableviewcell/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/contentview)*
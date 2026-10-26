# contentView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The content view of the cell object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var contentView: UIView { get }
```

```objc
@property (nonatomic, strong, readonly) UIView * contentView;
```

#### Discussion

The content view of a [`UITableViewCell`](../uitableviewcell.md) object is the default superview for content that the cell displays. If you want to customize cells by simply adding additional views, you should add them to the content view so they position appropriately as the cell transitions in to and out of editing mode.

## See Also

### Related Documentation
- [var backgroundView: UIView?](./backgroundview.md)
  The view to use as the background of the cell.
### Managing the content
- [func defaultContentConfiguration() -> UIListContentConfiguration](./defaultcontentconfiguration%28%29.md)
  Retrieves a default list content configuration for the cell’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](./contentconfiguration-9ktox.md)
  The current content configuration of the cell.
- [var automaticallyUpdatesContentConfiguration: Bool](./automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
- [- defaultContentConfiguration](./defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the cell’s style.
- [contentConfiguration](./contentconfiguration-2lzvp.md)
  The current content configuration of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/contentview)*
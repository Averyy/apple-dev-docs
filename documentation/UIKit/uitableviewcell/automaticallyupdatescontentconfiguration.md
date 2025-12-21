# automaticallyUpdatesContentConfiguration

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var automaticallyUpdatesContentConfiguration: Bool { get set }
```

#### Discussion

When this value is [`true`](https://developer.apple.com/documentation/Swift/true), the cell automatically calls [`updated(for:)`](uicontentconfiguration-9eib5/updated(for:).md) on its [`contentConfiguration`](uitableviewcell/contentconfiguration-9ktox.md) when the cell’s [`configurationState`](uitableviewcell/configurationstate-4xwj0.md) changes, and applies the updated configuration back to the cell. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

If you override [`updateConfiguration(using:)`](uitableviewcell/updateconfiguration(using:).md) to manually update and customize the content configuration, disable automatic updates by setting this property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func defaultContentConfiguration() -> UIListContentConfiguration](uitableviewcell/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the cell’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](uitableviewcell/contentconfiguration-9ktox.md)
  The current content configuration of the cell.
- [var contentView: UIView](uitableviewcell/contentview.md)
  The content view of the cell object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/automaticallyupdatescontentconfiguration)*
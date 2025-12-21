# automaticallyUpdatesBackgroundConfiguration

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var automaticallyUpdatesBackgroundConfiguration: Bool { get set }
```

#### Discussion

When this value is [`true`](https://developer.apple.com/documentation/Swift/true), the cell automatically calls `updated(for:)` on its [`backgroundConfiguration`](uitableviewcell/backgroundconfiguration-24e8e.md) when the cell’s [`configurationState`](uitableviewcell/configurationstate-4xwj0.md) changes, and applies the updated configuration back to the cell. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

If you override [`updateConfiguration(using:)`](uitableviewcell/updateconfiguration(using:).md) to manually update and customize the background configuration, disable automatic updates by setting this property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uitableviewcell/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](uitableviewcell/backgroundconfiguration-24e8e.md)
  The current background configuration of the cell.
- [var backgroundView: UIView?](uitableviewcell/backgroundview.md)
  The view to use as the background of the cell.
- [var selectedBackgroundView: UIView?](uitableviewcell/selectedbackgroundview.md)
  The view to use as the background for a selected cell.
- [var multipleSelectionBackgroundView: UIView?](uitableviewcell/multipleselectionbackgroundview.md)
  The background view to use for a selected cell when the table view allows multiple row selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/automaticallyupdatesbackgroundconfiguration)*
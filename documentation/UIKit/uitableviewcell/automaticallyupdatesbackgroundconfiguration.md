# automaticallyUpdatesBackgroundConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var automaticallyUpdatesBackgroundConfiguration: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyUpdatesBackgroundConfiguration;
```

#### Discussion

When this value is [`true`](../../Swift/true.md), the cell automatically calls `updated(for:)` on its [`backgroundConfiguration`](./backgroundconfiguration-24e8e.md) when the cell’s [`configurationState`](./configurationstate-4xwj0.md) changes, and applies the updated configuration back to the cell. The default value is [`true`](../../Swift/true.md).

If you override [`updateConfiguration(using:)`](./updateconfiguration%28using%29.md) to manually update and customize the background configuration, disable automatic updates by setting this property to [`false`](../../Swift/false.md).

## See Also

### Configuring the background
- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](./defaultbackgroundconfiguration%28%29.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](./backgroundconfiguration-24e8e.md)
  The current background configuration of the cell.
- [var backgroundView: UIView?](./backgroundview.md)
  The view to use as the background of the cell.
- [var selectedBackgroundView: UIView?](./selectedbackgroundview.md)
  The view to use as the background for a selected cell.
- [var multipleSelectionBackgroundView: UIView?](./multipleselectionbackgroundview.md)
  The background view to use for a selected cell when the table view allows multiple row selections.
- [- defaultBackgroundConfiguration](./defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [backgroundConfiguration](./backgroundconfiguration-93a2v.md)
  The current background configuration of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/automaticallyupdatesbackgroundconfiguration)*
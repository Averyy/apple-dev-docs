# automaticallyUpdatesContentConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view automatically updates its content configuration when its state changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var automaticallyUpdatesContentConfiguration: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyUpdatesContentConfiguration;
```

#### Discussion

When this value is [`true`](../../Swift/true.md), the cell automatically calls [`updated(for:)`](../uicontentconfiguration-9eib5/updated%28for%29.md) on its [`contentConfiguration`](./contentconfiguration-6b4eg.md) when the view’s [`configurationState`](./configurationstate-7xj7r.md) changes, and applies the updated configuration back to the view. The default value is [`true`](../../Swift/true.md).

If you override [`updateConfiguration(using:)`](./updateconfiguration%28using%29.md) to manually update and customize the content configuration, disable automatic updates by setting this property to [`false`](../../Swift/false.md).

## See Also

### Managing the content
- [func defaultContentConfiguration() -> UIListContentConfiguration](./defaultcontentconfiguration%28%29.md)
  Retrieves a default list content configuration for the view’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](./contentconfiguration-6b4eg.md)
  The current content configuration of the view.
- [var contentView: UIView](./contentview.md)
  The content view of the header or footer.
- [var textLabel: UILabel?](./textlabel.md)
  A primary text label for the view.
- [var detailTextLabel: UILabel?](./detailtextlabel.md)
  A detail text label for the view.
- [- defaultContentConfiguration](./defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the view’s style.
- [contentConfiguration](./contentconfiguration-r49e.md)
  The current content configuration of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/automaticallyupdatescontentconfiguration)*
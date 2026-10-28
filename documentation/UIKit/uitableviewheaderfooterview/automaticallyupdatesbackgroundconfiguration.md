# automaticallyUpdatesBackgroundConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view automatically updates its background configuration when its state changes.

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

## Discussion

When this value is [`true`](../../Swift/true.md), the cell automatically calls `updated(for:)` on its [`backgroundConfiguration`](./backgroundconfiguration-52wng.md) when the view’s [`configurationState`](./configurationstate-7xj7r.md) changes, and applies the updated configuration back to the view. The default value is [`true`](../../Swift/true.md).

If you override [`updateConfiguration(using:)`](./updateconfiguration%28using%29.md) to manually update and customize the background configuration, disable automatic updates by setting this property to [`false`](../../Swift/false.md).

## See Also

### Configuring the background
- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](./defaultbackgroundconfiguration%28%29.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](./backgroundconfiguration-52wng.md)
  The current background configuration of the view.
- [var backgroundView: UIView?](./backgroundview.md)
  The background view of the header or footer.
- [- defaultBackgroundConfiguration](./defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [backgroundConfiguration](./backgroundconfiguration-2o8ke.md)
  The current background configuration of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/automaticallyupdatesbackgroundconfiguration)*
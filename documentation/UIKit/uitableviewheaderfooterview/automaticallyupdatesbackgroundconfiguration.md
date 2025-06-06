# automaticallyUpdatesBackgroundConfiguration

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the view automatically updates its background configuration when its state changes.

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

When this value is [`true`](https://developer.apple.com/documentation/swift/true), the cell automatically calls `updated(for:)` on its [`backgroundConfiguration`](uitableviewheaderfooterview/backgroundconfiguration-52wng.md) when the view’s [`configurationState`](uitableviewheaderfooterview/configurationstate-7xj7r.md) changes, and applies the updated configuration back to the view. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

If you override [`updateConfiguration(using:)`](uitableviewheaderfooterview/updateconfiguration(using:).md) to manually update and customize the background configuration, disable automatic updates by setting this property to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uitableviewheaderfooterview/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](uitableviewheaderfooterview/backgroundconfiguration-52wng.md)
  The current background configuration of the view.
- [var backgroundView: UIView?](uitableviewheaderfooterview/backgroundview.md)
  The background view of the header or footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/automaticallyupdatesbackgroundconfiguration)*
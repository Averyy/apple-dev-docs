# automaticallyUpdatesContentConfiguration

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the view automatically updates its content configuration when its state changes.

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

When this value is [`true`](https://developer.apple.com/documentation/Swift/true), the cell automatically calls [`updated(for:)`](uicontentconfiguration-9eib5/updated(for:).md) on its [`contentConfiguration`](uitableviewheaderfooterview/contentconfiguration-6b4eg.md) when the view’s [`configurationState`](uitableviewheaderfooterview/configurationstate-7xj7r.md) changes, and applies the updated configuration back to the view. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

If you override [`updateConfiguration(using:)`](uitableviewheaderfooterview/updateconfiguration(using:).md) to manually update and customize the content configuration, disable automatic updates by setting this property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func defaultContentConfiguration() -> UIListContentConfiguration](uitableviewheaderfooterview/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the view’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](uitableviewheaderfooterview/contentconfiguration-6b4eg.md)
  The current content configuration of the view.
- [var contentView: UIView](uitableviewheaderfooterview/contentview.md)
  The content view of the header or footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/automaticallyupdatescontentconfiguration)*
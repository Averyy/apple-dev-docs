# contentConfiguration

**Framework**: UIKit  
**Kind**: property

The current content configuration of the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var contentConfiguration: (any UIContentConfiguration)? { get set }
```

#### Discussion

Using a content configuration, you can set the view’s content and styling for a variety of different view states. You can get the default configuration using [`defaultContentConfiguration()`](uitableviewheaderfooterview/defaultcontentconfiguration().md), assign your content to the configuration, customize any other properties, and assign it to the view as the current [`contentConfiguration`](uitableviewheaderfooterview/contentconfiguration-6b4eg.md).

Setting a content configuration replaces the existing [`contentView`](uitableviewheaderfooterview/contentview.md) of the view with a new content view instance from the configuration, or directly applies the configuration to the existing content view if the configuration is compatible with the existing content view type.

The default value is `nil`. After you set a content configuration to this property, setting this property back to `nil` replaces the current content view with a new, empty content view.

## See Also

- [func defaultContentConfiguration() -> UIListContentConfiguration](uitableviewheaderfooterview/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the view’s style.
- [var automaticallyUpdatesContentConfiguration: Bool](uitableviewheaderfooterview/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the view automatically updates its content configuration when its state changes.
- [var contentView: UIView](uitableviewheaderfooterview/contentview.md)
  The content view of the header or footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/contentconfiguration-6b4eg)*
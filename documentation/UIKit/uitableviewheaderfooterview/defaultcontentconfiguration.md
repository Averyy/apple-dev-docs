# defaultContentConfiguration()

**Framework**: UIKit  
**Kind**: method

Retrieves a default list content configuration for the view’s style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func defaultContentConfiguration() -> UIListContentConfiguration
```

#### Return Value

A default list content configuration. The system determines default values for the configuration according to the section where the view appears.

#### Discussion

The default content configuration has preconfigured default styling, but doesn’t contain any content. After you get the default configuration, you assign your content to it, customize any other properties, and assign it to the view as the current [`contentConfiguration`](uitableviewheaderfooterview/contentconfiguration-6b4eg.md).

## See Also

- [var contentConfiguration: (any UIContentConfiguration)?](uitableviewheaderfooterview/contentconfiguration-6b4eg.md)
  The current content configuration of the view.
- [var automaticallyUpdatesContentConfiguration: Bool](uitableviewheaderfooterview/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the view automatically updates its content configuration when its state changes.
- [var contentView: UIView](uitableviewheaderfooterview/contentview.md)
  The content view of the header or footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/defaultcontentconfiguration())*
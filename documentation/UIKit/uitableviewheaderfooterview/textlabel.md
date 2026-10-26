# textLabel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A primary text label for the view.

**Availability**:
- iOS 6.0+ - Deprecated in 27.0
- iPadOS 6.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use a content configuration to manage the view’s text instead. Use [`defaultContentConfiguration()`](./defaultcontentconfiguration%28%29.md) to get a default list content configuration, set your primary text to the [`text`](../uilistcontentconfiguration-swift.struct/text.md) property of the configuration, and apply the configuration by setting it to the [`contentConfiguration`](./contentconfiguration-6b4eg.md) property of the view.

## Declaration

```swift
var textLabel: UILabel? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UILabel * textLabel;
```

#### Discussion

Accessing the value in this property causes the view to create a default label for displaying a detail text string. If you are managing the content of the view yourself by adding subviews to the [`contentView`](./contentview.md) property, you should not access this property.

The label sizes to fit the content view area in the best way possible according to the size of the string. Its size also adjusts depending on whether there is a detail text label present.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](./contentconfiguration-6b4eg.md) resets this property to `nil`.

## See Also

### Managing the content
- [func defaultContentConfiguration() -> UIListContentConfiguration](./defaultcontentconfiguration%28%29.md)
  Retrieves a default list content configuration for the view’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](./contentconfiguration-6b4eg.md)
  The current content configuration of the view.
- [var automaticallyUpdatesContentConfiguration: Bool](./automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the view automatically updates its content configuration when its state changes.
- [var contentView: UIView](./contentview.md)
  The content view of the header or footer.
- [var detailTextLabel: UILabel?](./detailtextlabel.md)
  A detail text label for the view.
- [- defaultContentConfiguration](./defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the view’s style.
- [contentConfiguration](./contentconfiguration-r49e.md)
  The current content configuration of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/textlabel)*
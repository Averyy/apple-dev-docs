# backgroundView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The background view of the header or footer.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var backgroundView: UIView? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIView * backgroundView;
```

## Mentions

- [Adding headers and footers to table sections](../adding-headers-and-footers-to-table-sections.md)

## Discussion

The view in this property appears behind the view in the [`contentView`](./contentview.md) property and displays static background content behind the header or footer. For example, you might assign an image view to this property and use it to display a custom background image.

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [`backgroundConfiguration`](./backgroundconfiguration-52wng.md) to `nil`.

## See Also

### Configuring the background
- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](./defaultbackgroundconfiguration%28%29.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](./backgroundconfiguration-52wng.md)
  The current background configuration of the view.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](./automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
- [- defaultBackgroundConfiguration](./defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [backgroundConfiguration](./backgroundconfiguration-2o8ke.md)
  The current background configuration of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/backgroundview)*
# defaultBackgroundConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves a background configuration with system default values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (UIBackgroundConfiguration *) defaultBackgroundConfiguration;
```

## Return Value

A default background configuration. The system determines default values for the configuration according to the section where the view appears.

## See Also

### Configuring the background
- [backgroundConfiguration](./backgroundconfiguration-2o8ke.md)
  The current background configuration of the view.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](./automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](./backgroundview.md)
  The background view of the header or footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/defaultbackgroundconfiguration)*
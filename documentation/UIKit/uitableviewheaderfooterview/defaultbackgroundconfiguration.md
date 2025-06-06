# defaultBackgroundConfiguration()

**Framework**: UIKit  
**Kind**: method

Retrieves a background configuration with system default values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func defaultBackgroundConfiguration() -> UIBackgroundConfiguration
```

#### Return Value

A default background configuration. The system determines default values for the configuration according to the section where the view appears.

## See Also

- [var backgroundConfiguration: UIBackgroundConfiguration?](uitableviewheaderfooterview/backgroundconfiguration-52wng.md)
  The current background configuration of the view.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uitableviewheaderfooterview/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uitableviewheaderfooterview/backgroundview.md)
  The background view of the header or footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/defaultbackgroundconfiguration())*
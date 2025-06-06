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

A default background configuration. The system determines default values for the configuration according to the section where the cell appears.

## See Also

- [var backgroundConfiguration: UIBackgroundConfiguration?](uitableviewcell/backgroundconfiguration-24e8e.md)
  The current background configuration of the cell.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uitableviewcell/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uitableviewcell/backgroundview.md)
  The view to use as the background of the cell.
- [var selectedBackgroundView: UIView?](uitableviewcell/selectedbackgroundview.md)
  The view to use as the background for a selected cell.
- [var multipleSelectionBackgroundView: UIView?](uitableviewcell/multipleselectionbackgroundview.md)
  The background view to use for a selected cell when the table view allows multiple row selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/defaultbackgroundconfiguration())*
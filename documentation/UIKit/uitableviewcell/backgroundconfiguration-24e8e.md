# backgroundConfiguration

**Framework**: UIKit  
**Kind**: property

The current background configuration of the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var backgroundConfiguration: UIBackgroundConfiguration? { get set }
```

#### Discussion

[`UITableViewCell`](uitableviewcell.md) automatically sets up a default background configuration to provide its default appearance.

Using a background configuration, you can obtain system default background styling for a variety of different cell states. Create a background configuration with one of the default system styles, customize the configuration to match your cell’s style as necessary, and assign the configuration to this property.

```swift
var backgroundConfig = UIBackgroundConfiguration.listPlainCell()

// Set a nil background color to use the view's tint color. 
backgroundConfig.backgroundColor = nil 

cell.backgroundConfiguration = backgroundConfig 
```

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets the following APIs to `nil`:

- [`backgroundColor`](uiview/backgroundcolor.md)
- [`backgroundView`](uitableviewcell/backgroundview.md)
- [`selectedBackgroundView`](uitableviewcell/selectedbackgroundview.md)
- [`multipleSelectionBackgroundView`](uitableviewcell/multipleselectionbackgroundview.md)

## See Also

- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uitableviewcell/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uitableviewcell/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uitableviewcell/backgroundview.md)
  The view to use as the background of the cell.
- [var selectedBackgroundView: UIView?](uitableviewcell/selectedbackgroundview.md)
  The view to use as the background for a selected cell.
- [var multipleSelectionBackgroundView: UIView?](uitableviewcell/multipleselectionbackgroundview.md)
  The background view to use for a selected cell when the table view allows multiple row selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/backgroundconfiguration-24e8e)*
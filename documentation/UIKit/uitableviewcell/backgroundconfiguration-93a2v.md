# backgroundConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current background configuration of the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) UIBackgroundConfiguration * backgroundConfiguration;
```

## Discussion

[`UITableViewCell`](../uitableviewcell.md) automatically sets up a default background configuration to provide its default appearance.

Using a background configuration, you can obtain system default background styling for a variety of different cell states. Create a background configuration with one of the default system styles, customize the configuration to match your cell’s style as necessary, and assign the configuration to this property.

```objc
UIBackgroundConfiguration *backgroundConfig = [UIBackgroundConfiguration listPlainCellConfiguration];

// Set a nil background color to use the view's tint color.
[backgroundConfig setBackgroundColor:nil];

[cell setBackgroundConfiguration:backgroundConfig];
```

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets the following APIs to `nil`:

- [`backgroundColor`](../uiview/backgroundcolor.md)
- [`backgroundView`](./backgroundview.md)
- [`selectedBackgroundView`](./selectedbackgroundview.md)
- [`multipleSelectionBackgroundView`](./multipleselectionbackgroundview.md)

## See Also

### Configuring the background
- [- defaultBackgroundConfiguration](./defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](./automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](./backgroundview.md)
  The view to use as the background of the cell.
- [var selectedBackgroundView: UIView?](./selectedbackgroundview.md)
  The view to use as the background for a selected cell.
- [var multipleSelectionBackgroundView: UIView?](./multipleselectionbackgroundview.md)
  The background view to use for a selected cell when the table view allows multiple row selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/backgroundconfiguration-93a2v)*
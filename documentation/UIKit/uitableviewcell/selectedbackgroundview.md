# selectedBackgroundView

**Framework**: UIKit  
**Kind**: property

The view to use as the background for a selected cell.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedBackgroundView: UIView? { get set }
```

#### Discussion

[`UITableViewCell`](uitableviewcell.md) adds the value of this property as a subview only when the cell has a selected state. It adds the selected background view as a subview directly above the background view ([`backgroundView`](uitableviewcell/backgroundview.md)) if it isn’t `nil`, or behind all other views. Calling [`setSelected(_:animated:)`](uitableviewcell/setselected(_:animated:).md) causes the selected background view to animate in and out with an alpha fade.

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [`backgroundConfiguration`](uitableviewcell/backgroundconfiguration-24e8e.md) to `nil`.

## See Also

- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uitableviewcell/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](uitableviewcell/backgroundconfiguration-24e8e.md)
  The current background configuration of the cell.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uitableviewcell/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uitableviewcell/backgroundview.md)
  The view to use as the background of the cell.
- [var multipleSelectionBackgroundView: UIView?](uitableviewcell/multipleselectionbackgroundview.md)
  The background view to use for a selected cell when the table view allows multiple row selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/selectedbackgroundview)*
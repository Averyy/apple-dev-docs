# editingAccessoryView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view to use on the right side of the cell, typically as a control, in the table view’s editing state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var editingAccessoryView: UIView? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIView * editingAccessoryView;
```

## Discussion

If the value of this property is not `nil`, the `UITableViewCell` class uses the given view for the accessory view in the table view’s editing state; it ignores the value of the [`editingAccessoryType`](./editingaccessorytype.md) property. The provided accessory view can be a framework-provided control or label or a custom view. The accessory view appears in the right side of the cell.

The accessory type cross-fades between normal and editing states if it set for both states; use the [`accessoryType`](./accessorytype-swift.property.md) property to set the accessory view for the cell during the table view’s normal state. If this property is not set for both states, the cell is animated to slide or out, as necessary.

## See Also

### Related Documentation
- [func willTransition(to: UITableViewCell.StateMask)](./willtransition%28to%29.md)
  Notifies the cell that it’s about to transition to a new cell state.
- [func didTransition(to: UITableViewCell.StateMask)](./didtransition%28to%29.md)
  Notifies the cell that it transitioned to a new cell state.
### Managing accessory views
- [var accessoryType: UITableViewCell.AccessoryType](./accessorytype-swift.property.md)
  The type of standard accessory view for the cell to use in the table view’s normal state.
- [var accessoryView: UIView?](./accessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [var editingAccessoryType: UITableViewCell.AccessoryType](./editingaccessorytype.md)
  The type of standard accessory view for the cell to use in the table view’s editing state.
- [UITableViewCell.AccessoryType](./accessorytype-swift.enum.md)
  The type of standard accessory control used by a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/editingaccessoryview)*
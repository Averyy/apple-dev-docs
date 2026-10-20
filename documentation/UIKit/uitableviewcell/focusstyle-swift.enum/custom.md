# UITableViewCell.FocusStyle.custom

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The cell doesn’t alter its appearance automatically when it becomes focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case custom
```

```c
UITableViewCellFocusStyleCustom
```

#### Discussion

Specifying this style allows you to create your own custom appearance for the cell. It’s recommended that you create custom-looking cells by subclassing [`UITableViewCell`](../../uitableviewcell.md) and overriding [`didUpdateFocus(in:with:)`](../../uifocusenvironment/didupdatefocus%28in,with%29.md).

## See Also

### Constants
- [UITableViewCell.FocusStyle.default](./default.md)
  The cell alters its appearance in a standard, system-defined way when it becomes focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/focusstyle-swift.enum/custom)*
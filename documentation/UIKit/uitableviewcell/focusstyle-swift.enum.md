# UITableViewCell.FocusStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The style of focused cells.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum FocusStyle
```

```c
enum UITableViewCellFocusStyle : NSInteger;
```

#### Overview

You use these constants to set the value of the [`focusStyle`](./focusstyle-swift.property.md) property.

## Topics

### Constants
- [UITableViewCell.FocusStyle.default](./focusstyle-swift.enum/default.md)
  The cell alters its appearance in a standard, system-defined way when it becomes focused.
- [UITableViewCell.FocusStyle.custom](./focusstyle-swift.enum/custom.md)
  The cell doesn’t alter its appearance automatically when it becomes focused.
### Initializers
- [init?(rawValue: Int)](./focusstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing focus
- [var focusStyle: UITableViewCell.FocusStyle](./focusstyle-swift.property.md)
  The appearance of the cell when focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/focusstyle-swift.enum)*
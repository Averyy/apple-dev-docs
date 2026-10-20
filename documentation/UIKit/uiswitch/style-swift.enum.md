# UISwitch.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Styles that determine the appearance of the switch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Style
```

```c
enum UISwitchStyle : NSInteger;
```

## Topics

### Styles
- [UISwitch.Style.automatic](./style-swift.enum/automatic.md)
  A style indicating that the system chooses the appearance of the switch according to the current user interface idiom.
- [UISwitch.Style.checkbox](./style-swift.enum/checkbox.md)
  A style indicating that the switch appears as a Mac-style checkbox.
- [UISwitch.Style.sliding](./style-swift.enum/sliding.md)
  A style indicating that the switch appears as an on/off slider.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting the display style
- [Displaying a checkbox in your Mac app built with Mac Catalyst](../displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)
  Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [var preferredStyle: UISwitch.Style](./preferredstyle.md)
  The preferred display style for the switch.
- [var style: UISwitch.Style](./style-swift.property.md)
  The display style for the switch.
- [var title: String?](./title.md)
  The title displayed next to a checkbox-style switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/style-swift.enum)*
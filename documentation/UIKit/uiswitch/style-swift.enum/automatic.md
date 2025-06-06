# UISwitch.Style.automatic

**Framework**: UIKit  
**Kind**: case

A style indicating that the system chooses the appearance of the switch according to the current user interface idiom.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
case automatic
```

## Mentions

- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)

#### Discussion

The system chooses the [`UISwitch.Style.checkbox`](uiswitch/style-swift.enum/checkbox.md) style when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md); otherwise, it chooses the [`UISwitch.Style.sliding`](uiswitch/style-swift.enum/sliding.md) style.

## See Also

- [UISwitch.Style.checkbox](uiswitch/style-swift.enum/checkbox.md)
  A style indicating that the switch appears as a Mac-style checkbox.
- [UISwitch.Style.sliding](uiswitch/style-swift.enum/sliding.md)
  A style indicating that the switch appears as an on/off slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/style-swift.enum/automatic)*
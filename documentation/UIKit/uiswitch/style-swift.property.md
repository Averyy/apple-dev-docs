# style

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The display style for the switch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var style: UISwitch.Style { get }
```

```objc
@property (nonatomic, readonly) UISwitchStyle style;
```

## Discussion

This property returns the resolved style based on the user interface idiom, and never returns [`UISwitch.Style.automatic`](./style-swift.enum/automatic.md).

## See Also

### Setting the display style
- [Displaying a checkbox in your Mac app built with Mac Catalyst](../displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)
  Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [var preferredStyle: UISwitch.Style](./preferredstyle.md)
  The preferred display style for the switch.
- [UISwitch.Style](./style-swift.enum.md)
  Styles that determine the appearance of the switch.
- [var title: String?](./title.md)
  The title displayed next to a checkbox-style switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/style-swift.property)*
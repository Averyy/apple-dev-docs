# preferredStyle

**Framework**: UIKit  
**Kind**: property

The preferred display style for the switch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredStyle: UISwitch.Style { get set }
```

## Mentions

- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)
- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)

#### Discussion

Use this property to specify the display style that you prefer. If the style changes, the switch may generate a layout pass to update the display.

The default style is [`UISwitch.Style.automatic`](uiswitch/style-swift.enum/automatic.md). For a list of styles, see [`UISwitch.Style`](uiswitch/style-swift.enum.md).

## See Also

- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)
  Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [var style: UISwitch.Style](uiswitch/style-swift.property.md)
  The display style for the switch.
- [UISwitch.Style](uiswitch/style-swift.enum.md)
  Styles that determine the appearance of the switch.
- [var title: String?](uiswitch/title.md)
  The title displayed next to a checkbox-style switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/preferredstyle)*
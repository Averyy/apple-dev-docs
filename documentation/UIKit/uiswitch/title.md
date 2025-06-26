# title

**Framework**: UIKit  
**Kind**: property

The title displayed next to a checkbox-style switch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var title: String? { get set }
```

## Mentions

- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)
- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md)

#### Discussion

Set [`title`](uiswitch/title.md) only when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md); otherwise, a runtime exception occurs.

```swift
let showFavoritesAtTop = UISwitch()
showFavoritesAtTop.preferredStyle = .checkbox
if traitCollection.userInterfaceIdiom == .mac {
    showFavoritesAtTop.title = "Always show favorite recipes at the top"
}
```

The switch ignores [`title`](uiswitch/title.md) when the value of [`style`](uiswitch/style-swift.property.md) isn’t [`UISwitch.Style.checkbox`](uiswitch/style-swift.enum/checkbox.md).

## See Also

- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md)
  Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [var preferredStyle: UISwitch.Style](uiswitch/preferredstyle.md)
  The preferred display style for the switch.
- [var style: UISwitch.Style](uiswitch/style-swift.property.md)
  The display style for the switch.
- [UISwitch.Style](uiswitch/style-swift.enum.md)
  Styles that determine the appearance of the switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/title)*
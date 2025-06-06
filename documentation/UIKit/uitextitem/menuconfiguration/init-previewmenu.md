# init(preview:menu:)

**Framework**: UIKit  
**Kind**: init

Creates a text item menu configuration with the specified menu and preview.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(preview: UITextItem.MenuConfiguration.Preview? = .default, menu: UIMenu)
```

## Parameters

- `preview`: The preview to display alongside the menu.
- `menu`: The menu to present when the user interacts with the text item.

## See Also

- [UITextItem.MenuConfiguration.Preview](uitextitem/menuconfiguration/preview.md)
  Constants that indicate what type of preview to display alongside the text item’s menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextitem/menuconfiguration/init(preview:menu:))*
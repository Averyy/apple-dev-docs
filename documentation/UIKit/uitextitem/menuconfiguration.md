# UITextItem.MenuConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that describes what type of menu and preview to show for a text item.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MenuConfiguration
```

```objc
@interface UITextItemMenuConfiguration : NSObject
```

#### Overview

Create and return a menu configuration for a text item in [`textView(_:menuConfigurationFor:defaultMenu:)`](../uitextviewdelegate/textview%28_,menuconfigurationfor,defaultmenu%29.md) to provide a custom menu that the system shows when someone interacts with the text item. Provide a custom view for the item’s preview, or specify that the system displays a default preview.

## Topics

### Creating a menu configuration
- [convenience init(preview: UITextItem.MenuConfiguration.Preview?, menu: UIMenu)](./menuconfiguration/init%28preview,menu%29.md)
  Creates a text item menu configuration with the specified menu and preview.
- [UITextItem.MenuConfiguration.Preview](./menuconfiguration/preview.md)
  Constants that indicate what type of preview to display alongside the text item’s menu.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Text actions and menus
- [class UITextItem](../uitextitem.md)
  An object for attaching custom actions and menus to links, text attachments, or other specific text in a text view.
- [protocol UITextViewDelegate](../uitextviewdelegate.md)
  The methods for receiving editing-related messages for text view objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextitem/menuconfiguration)*
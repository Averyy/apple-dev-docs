# UITextItem

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object for attaching custom actions and menus to links, text attachments, or other specific text in a text view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextItem
```

```objc
@interface UITextItem : NSObject
```

## Overview

A text item represents a link with a URL destination, a custom tag for a topic that you specify in your app, or a text attachment in a text view. In your text view’s [`UITextViewDelegate`](./uitextviewdelegate.md), implement [`textView(_:primaryActionFor:defaultAction:)`](./uitextviewdelegate/textview%28_,primaryactionfor,defaultaction%29.md) to provide a custom action when someone interacts with a text item. Implement [`textView(_:menuConfigurationFor:defaultMenu:)`](./uitextviewdelegate/textview%28_,menuconfigurationfor,defaultmenu%29.md) to provide a custom menu for a text item.

## Topics

### Specifying the content type
- [var content: UITextItem.Content](./uitextitem/content-swift.property.md)
  The content type and related value of the text item.
- [UITextItem.Content](./uitextitem/content-swift.enum.md)
  Constants that describe and capture the type of content a text item represents along with a specific related value.
- [contentType](./uitextitem/contenttype.md)
  The content type and related value of the text item.
### Specifying the range
- [var range: NSRange](./uitextitem/range.md)
  The range that delineates the text item in an attributed string.
### Creating a menu
- [UITextItem.MenuConfiguration](./uitextitem/menuconfiguration.md)
  An object that describes what type of menu and preview to show for a text item.
### Getting the value
- [link](./uitextitem/link.md)
  The URL associated with the link text.
- [textAttachment](./uitextitem/textattachment.md)
  The attachment for with the text item.
- [tagIdentifier](./uitextitem/tagidentifier.md)
  The tag associated with the text item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Text actions and menus
- [UITextItem.MenuConfiguration](./uitextitem/menuconfiguration.md)
  An object that describes what type of menu and preview to show for a text item.
- [protocol UITextViewDelegate](./uitextviewdelegate.md)
  The methods for receiving editing-related messages for text view objects.
- [UITextItemContentType](./uitextitemcontenttype.md)
  Constants that describe and capture the type of content a text item represents along with a specific related value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextitem)*
# UITextInputTextColorKey

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The color of the text.

**Availability**:
- iOS 3.2+ - Deprecated in 8.0 (renamed: NSAttributedString.Key.foregroundColor)
- iPadOS 3.2+ - Deprecated in 8.0 (renamed: NSAttributedString.Key.foregroundColor)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSAttributedString.Key.foregroundColor)

> **Deprecated**: In Swift, use [`foregroundColor`](../Foundation/nsattributedstring/key/foregroundcolor.md) instead. In Objective-C, use [`NSForegroundColorAttributeName`](./nsforegroundcolorattributename.md) instead.

## Declaration

```swift
let UITextInputTextColorKey: String
```

```c
extern NSString * const UITextInputTextColorKey;
```

## Discussion

The value of this key is a [`UIColor`](./uicolor.md) object.

## See Also

### Deprecated
- [let UITextInputTextBackgroundColorKey: String](./uitextinputtextbackgroundcolorkey.md)
  The background color of the text.
- [let UITextInputTextFontKey: String](./uitextinputtextfontkey.md)
  The font of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtextcolorkey)*
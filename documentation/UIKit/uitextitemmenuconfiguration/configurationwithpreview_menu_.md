# configurationWithPreview:menu:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a menu configuration with the specified menu and custom preview.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) configurationWithPreview:(UITextItemMenuPreview *) preview menu:(UIMenu *) menu;
```

## Parameters

- `preview`: The preview associated with the menu. Specify @c nil for no preview.
- `menu`: The menu to be presented.

## See Also

### Creating a menu configuration
- [+ configurationWithMenu:](./configurationwithmenu_.md)
  Creates a menu configuration with the specified menu and a default preview.
- [UITextItemMenuPreview](../uitextitemmenupreview.md)
  An object representing the preview for a text item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextitemmenuconfiguration/configurationwithpreview:menu:)*
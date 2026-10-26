# UITextFormattingViewControllerChangeValue

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Describes text formatting change that is a result of user action. Contains type of change, any associated value that may be applicable to that change.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 26.0+

## Declaration

```objc
@interface UITextFormattingViewControllerChangeValue : NSObject
```

## Topics

### Instance Properties
- [changeType](./uitextformattingviewcontrollerchangevalue/changetype.md)
  Type of change.
- [color](./uitextformattingviewcontrollerchangevalue/color.md)
  Any color value that may be associated with the change. For example, this property will be available if user has changed text color.
- [font](./uitextformattingviewcontrollerchangevalue/font.md)
  Any font that may be associated with the change. For example, this property will be available in case of font typography settings change or new font selection.
- [formattingStyleKey](./uitextformattingviewcontrollerchangevalue/formattingstylekey.md)
  On formatting style change, use this property to determine selected style.
- [highlight](./uitextformattingviewcontrollerchangevalue/highlight.md)
  Text highlight associated with the `UITextFormattingViewControllerHighlightChangeType`. If property is nil for `UITextFormattingViewControllerHighlightChangeType`, it indicates highlight has been removed.
- [numberValue](./uitextformattingviewcontrollerchangevalue/numbervalue.md)
  Any number value that may be associated with the change. For example, if case of font point size change, this property will reflect new point size.
- [textAlignment](./uitextformattingviewcontrollerchangevalue/textalignment.md)
  Text alignment associated with the `UITextFormattingViewControllerTextAlignmentChangeType`.
- [textList](./uitextformattingviewcontrollerchangevalue/textlist.md)
  Text list style associated with the `UITextFormattingViewControllerTextListChangeType`. If property is nil for `UITextFormattingViewControllerTextListChangeType`, it indicates text list has been removed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Classes
- [UITextFormattingViewController.Component](./uitextformattingviewcontroller/component.md)
  Defines text formatting view component.
- [UITextFormattingViewController.ComponentGroup](./uitextformattingviewcontroller/componentgroup.md)
  Defines grouping of text formatting components in view.
- [UITextFormattingViewController.Configuration](./uitextformattingviewcontroller/configuration-swift.class.md)
  Text formatting view controller configuration object.
- [UITextFormattingViewControllerFormattingDescriptor](./uitextformattingviewcontrollerformattingdescriptor.md)
  Object that represents current text formatting state. This can apply to formatting state of some selected range of text or currently applicable input formatting.
- [UITextFormattingViewControllerFormattingStyle](./uitextformattingviewcontrollerformattingstyle.md)
  Type that defines formatting style presented in text formatting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerchangevalue)*
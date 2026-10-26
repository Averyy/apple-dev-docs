# UITextFormattingViewControllerFormattingDescriptor

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Object that represents current text formatting state. This can apply to formatting state of some selected range of text or currently applicable input formatting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 26.0+

## Declaration

```objc
@interface UITextFormattingViewControllerFormattingDescriptor : NSObject
```

## Topics

### Instance Properties
- [fonts](./uitextformattingviewcontrollerformattingdescriptor/fonts.md)
- [formattingStyleKey](./uitextformattingviewcontrollerformattingdescriptor/formattingstylekey.md)
- [highlights](./uitextformattingviewcontrollerformattingdescriptor/highlights.md)
- [lineHeight](./uitextformattingviewcontrollerformattingdescriptor/lineheight.md)
- [strikethroughPresent](./uitextformattingviewcontrollerformattingdescriptor/strikethroughpresent.md)
- [textAlignments](./uitextformattingviewcontrollerformattingdescriptor/textalignments.md)
- [textColors](./uitextformattingviewcontrollerformattingdescriptor/textcolors.md)
- [textLists](./uitextformattingviewcontrollerformattingdescriptor/textlists.md)
- [underlinePresent](./uitextformattingviewcontrollerformattingdescriptor/underlinepresent.md)
### Instance Methods
- [- init](./uitextformattingviewcontrollerformattingdescriptor/init.md)
  Initializes formatting descriptor with default property values.
- [- initWithAttributes:](./uitextformattingviewcontrollerformattingdescriptor/initwithattributes_.md)
  Initializes formatting descriptor with attribute dictionary.
- [- initWithString:range:](./uitextformattingviewcontrollerformattingdescriptor/initwithstring_range_.md)
  Initializes formatting descriptor with a string and selected range of string.

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
- [UITextFormattingViewControllerChangeValue](./uitextformattingviewcontrollerchangevalue.md)
  Describes text formatting change that is a result of user action. Contains type of change, any associated value that may be applicable to that change.
- [UITextFormattingViewControllerFormattingStyle](./uitextformattingviewcontrollerformattingstyle.md)
  Type that defines formatting style presented in text formatting view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerformattingdescriptor)*
# AXAttributeConstants.h

**Framework**: Application Services

#### Overview

Each UIElement has a set of attributes that assistive applications use to get information about the UIElement. The list of attributes vary depending on the type of UIElement. The value of some attributes can be changed, while others cannot. For example, changing the "value" attribute of a slider changes the slider's setting.

Attribute values are stored as Core Foundation types, CFTypeRefs, and are reference counted (CFRetain/CFRelease). Some attributes have a particular type associated with them. For example, the "title" attribute, if defined, always has a string value, regardless of the type of UIElement from which it is obtained. A UIElement's "value" attribute, however, varies with the UIElement. For example, a text field's value is a string whereas a checkbox's value is a boolean. You need to explictly test the returned objects, using the CFGetTypeID function, for what type they really are.

Finally, some attribute values hold simple structures, such as CGPoint and CGRect, instead of regular CFTypes. These are still passed between the target and assistive application as CFTypeRefs, but they merely wrap an encoded version of the structure. You need to use the functions AXValueCreate and AXValueGetValue to convert between the structures and CFTypeRefs. Each supported structure has an AXValueType associated with it. The AXValueGetType function returns the AXValueType of the structure contained within a CFTypeRef.

## Topics

### Constants
- [Miscellaneous Defines](axattributeconstants_h/miscellaneous_defines.md)
- [struct AXMenuItemModifiers](axmenuitemmodifiers.md)
  Values that indicate the keyboard shortcut modifiers for a menu item (used with the kAXMenuItemCmdModifiersAttribute attribute).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axattributeconstants_h)*
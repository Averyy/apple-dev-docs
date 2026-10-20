# UITextFormattingViewController.Component

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Defines text formatting view component.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 26.0+

## Declaration

```swift
class Component
```

```objc
@interface UITextFormattingViewControllerComponent : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./component/init%28coder%29.md)
- [init(componentKey: UITextFormattingViewController.ComponentKey, preferredSize: UITextFormattingViewController.ComponentSize)](./component/init%28componentkey,preferredsize%29.md)
  Creates a text formatting view component configuration with component key and preferred size.
### Instance Properties
- [var componentKey: UITextFormattingViewController.ComponentKey](./component/componentkey.md)
  Unique key that identifies text formatting view component.
- [var preferredSize: UITextFormattingViewController.ComponentSize](./component/preferredsize.md)
  Specifies preferred size of the component in text formatting view.
### Type Methods
- [static func component(UITextFormattingViewController.ComponentKey, UITextFormattingViewController.ComponentSize) -> UITextFormattingViewController.Component](./component/component%28_,_%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Classes
- [UITextFormattingViewController.ComponentGroup](./componentgroup.md)
  Defines grouping of text formatting components in view.
- [UITextFormattingViewController.Configuration](./configuration-swift.class.md)
  Text formatting view controller configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontroller/component)*
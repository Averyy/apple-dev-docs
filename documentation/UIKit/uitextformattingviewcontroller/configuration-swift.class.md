# UITextFormattingViewController.Configuration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Text formatting view controller configuration object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 26.0+

## Declaration

```swift
class Configuration
```

```objc
@interface UITextFormattingViewControllerConfiguration : NSObject
```

## Topics

### Initializers
- [init()](./configuration-swift.class/init%28%29.md)
  Creates a default configuration with most common text formatting options.
- [init?(coder: NSCoder)](./configuration-swift.class/init%28coder%29.md)
- [convenience init(groups: [UITextFormattingViewController.ComponentGroup])](./configuration-swift.class/init%28groups%29.md)
  Creates a configuration object with provided component groups.
### Instance Properties
- [var fontPickerConfiguration: UIFontPickerViewController.Configuration?](./configuration-swift.class/fontpickerconfiguration.md)
  Configuration object that will be used to customize `UIFontPickerViewController` if presented by `UITextFormattingViewController`.
- [var formattingStyles: [UITextFormattingViewController.FormattingStyle]?](./configuration-swift.class/formattingstyles.md)
- [var groups: [UITextFormattingViewController.ComponentGroup]](./configuration-swift.class/groups.md)
  Component groups displayed by text formatting view.

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
- [UITextFormattingViewController.Component](./component.md)
  Defines text formatting view component.
- [UITextFormattingViewController.ComponentGroup](./componentgroup.md)
  Defines grouping of text formatting components in view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontroller/configuration-swift.class)*
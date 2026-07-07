# UITextFormattingViewController.Configuration

**Framework**: UIKit  
**Kind**: class

Text formatting view controller configuration object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 26.0+

## Declaration

```swift
class Configuration
```

## Topics

### Initializers
- [init()](uitextformattingviewcontroller/configuration-swift.class/init.md)
  Creates a default configuration with most common text formatting options.
- [init?(coder: NSCoder)](uitextformattingviewcontroller/configuration-swift.class/init(coder:).md)
- [convenience init(groups: [UITextFormattingViewController.ComponentGroup])](uitextformattingviewcontroller/configuration-swift.class/init(groups:).md)
  Creates a configuration object with provided component groups.
### Instance Properties
- [var fontPickerConfiguration: UIFontPickerViewController.Configuration?](uitextformattingviewcontroller/configuration-swift.class/fontpickerconfiguration.md)
  Configuration object that will be used to customize `UIFontPickerViewController` if presented by `UITextFormattingViewController`.
- [var formattingStyles: [UITextFormattingViewController.FormattingStyle]?](uitextformattingviewcontroller/configuration-swift.class/formattingstyles.md)
- [var groups: [UITextFormattingViewController.ComponentGroup]](uitextformattingviewcontroller/configuration-swift.class/groups.md)
  Component groups displayed by text formatting view.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [UITextFormattingViewController.Component](uitextformattingviewcontroller/component.md)
  Defines text formatting view component.
- [UITextFormattingViewController.ComponentGroup](uitextformattingviewcontroller/componentgroup.md)
  Defines grouping of text formatting components in view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontroller/configuration-swift.class)*
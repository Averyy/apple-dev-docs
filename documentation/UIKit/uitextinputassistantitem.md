# UITextInputAssistantItem

**Framework**: Uikit  
**Kind**: class

An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class UITextInputAssistantItem
```

#### Overview

Use a [`UITextInputAssistantItem`](uitextinputassistantitem.md) object to add app-specific actions to the shortcuts bar on iPad. The center of the shortcuts bar displays typing suggestions for the user. You can install custom bar button items that lead or trail the typing suggestions.

> **Note**:  You can add custom items to the shortcuts bar on iPad only. On iPhone, the text input system ignores the contents of the [`UITextInputAssistantItem`](uitextinputassistantitem.md) object.

You don’t create instances of this class directly. Instead, you get an input assistant from the [`inputAssistantItem`](uiresponder/inputassistantitem.md) property of the responder object whose keyboard you want to modify. When the keyboard is onscreen, UIKit automatically searches the responder chain for a text-input assistant object. Typically, you assign the text-input assistant to the object that becomes the first responder. However, you can also assign it to a parent responder object to share a set of shortcuts among multiple children.

Organize the bar button items you create for the shortcuts bar into groups. A [`UIBarButtonItemGroup`](uibarbuttonitemgroup.md) object manages each group of items, and each group may contain a single item or several items. UIKit displays as many items as possible based on the available space. When there’s not enough space for all of the items, UIKit collapses each group of items down to a single representative item.

The following code configures the items of the shortcuts bar. After creating the bar button items, this code creates a group and assigns that group to the [`leadingBarButtonGroups`](uitextinputassistantitem/leadingbarbuttongroups.md) property. The resulting items appear before the typing suggestions.

To hide shortcuts altogether, set the [`leadingBarButtonGroups`](uitextinputassistantitem/leadingbarbuttongroups.md) and [`trailingBarButtonGroups`](uitextinputassistantitem/trailingbarbuttongroups.md) properties to empty arrays. Doing so hides only the shortcuts and doesn’t hide the typing suggestions. For information on managing the typing suggestions, see [`autocorrectionType`](uitextinputtraits/autocorrectiontype.md).

## Topics

### Configuring the shortcuts bar
- [var leadingBarButtonGroups: [UIBarButtonItemGroup]](uitextinputassistantitem/leadingbarbuttongroups.md)
  The array of button item groups to display before the typing suggestions.
- [var trailingBarButtonGroups: [UIBarButtonItemGroup]](uitextinputassistantitem/trailingbarbuttongroups.md)
  The array of button item groups to display after the typing suggestions.
- [var allowsHidingShortcuts: Bool](uitextinputassistantitem/allowshidingshortcuts.md)
  A Boolean value that indicates whether the user can hide the shortcuts bar.
### Instance Properties
- [var keyboardAction: UIBarButtonItem?](uitextinputassistantitem/keyboardaction.md)
  A button that appears next to the text preview in the keyboard in visionOS.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UITextInput](uitextinput.md)
  A set of methods for interacting with the text input system and enabling features in documents.
- [protocol UITextInputDelegate](uitextinputdelegate.md)
  An intermediary between a document and the text input system.
- [protocol UIKeyInput](uikeyinput.md)
  A set of methods a responder uses to implement simple text entry.
- [protocol UITextInputTraits](uitextinputtraits.md)
  A set of methods that defines features for keyboard input to a text object.
- [class UITextInputContext](uitextinputcontext.md)
  An object that reports the type of input your app receives.
- [class UITextInputMode](uitextinputmode.md)
  The current text input mode.
- [class UIDictationPhrase](uidictationphrase.md)
  An object that represents the textual interpretation of a spoken phrase that the user dictates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uitextinputassistantitem)*
# UITextFormattingCoordinator

**Framework**: UIKit  
**Kind**: class

An object that coordinates text formatting using the standard Mac font panel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextFormattingCoordinator
```

## Topics

### Creating a Text-Formatting Coordinator
- [convenience init(for: UIWindowScene)](uitextformattingcoordinator/init(for:).md)
  Creates a text-formatting coordinator for the specified window scene.
- [init(windowScene: UIWindowScene)](uitextformattingcoordinator/init(windowscene:).md)
  Initializes and returns a new text-formatting coordinator for the specified window scene.
### Showing the Font Panel
- [class var isFontPanelVisible: Bool](uitextformattingcoordinator/isfontpanelvisible.md)
  A Boolean value that indicates whether the font panel is visible.
- [class func toggleFontPanel(Any)](uitextformattingcoordinator/togglefontpanel(_:).md)
  Toggles the visibility of the font panel.
### Configuring the Font Panel
- [func setSelectedAttributes([NSAttributedString.Key : Any], isMultiple: Bool)](uitextformattingcoordinator/setselectedattributes(_:ismultiple:).md)
  Configures the initial display state of the font panel with the attributes of the selected text.
### Applying Updated Text Attributes
- [var delegate: (any UITextFormattingCoordinatorDelegate)?](uitextformattingcoordinator/delegate.md)
  The delegate of the text-formatting coordinator.
- [protocol UITextFormattingCoordinatorDelegate](uitextformattingcoordinatordelegate.md)
  The methods that delegates of text-formatting coordinators implement to apply font panel settings to the currently selected text.

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
- [UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md)

## See Also

- [typealias UITextAttributesConversionHandler](uitextattributesconversionhandler.md)
  A handler for updating text with current font panel settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingcoordinator)*
# UITextFormattingCoordinator

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UITextFormattingCoordinator : NSObject
```

## Topics

### Creating a Text-Formatting Coordinator
- [convenience init(for: UIWindowScene)](./uitextformattingcoordinator/init%28for%29.md)
  Creates a text-formatting coordinator for the specified window scene.
- [init(windowScene: UIWindowScene)](./uitextformattingcoordinator/init%28windowscene%29.md)
  Initializes and returns a new text-formatting coordinator for the specified window scene.
### Showing the Font Panel
- [class var isFontPanelVisible: Bool](./uitextformattingcoordinator/isfontpanelvisible.md)
  A Boolean value that indicates whether the font panel is visible.
- [class func toggleFontPanel(Any)](./uitextformattingcoordinator/togglefontpanel%28_%29.md)
  Toggles the visibility of the font panel.
### Configuring the Font Panel
- [func setSelectedAttributes([NSAttributedString.Key : Any], isMultiple: Bool)](./uitextformattingcoordinator/setselectedattributes%28_,ismultiple%29.md)
  Configures the initial display state of the font panel with the attributes of the selected text.
### Applying Updated Text Attributes
- [var delegate: (any UITextFormattingCoordinatorDelegate)?](./uitextformattingcoordinator/delegate.md)
  The delegate of the text-formatting coordinator.
- [protocol UITextFormattingCoordinatorDelegate](./uitextformattingcoordinatordelegate.md)
  The methods that delegates of text-formatting coordinators implement to apply font panel settings to the currently selected text.
### Initializers
- [convenience init(forWindowScene: UIWindowScene)](./uitextformattingcoordinator/init%28forwindowscene%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UIFontPickerViewControllerDelegate](./uifontpickerviewcontrollerdelegate.md)

## See Also

### Text formatting
- [typealias UITextAttributesConversionHandler](./uitextattributesconversionhandler.md)
  A handler for updating text with current font panel settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingcoordinator)*
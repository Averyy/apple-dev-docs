# UITextFormattingViewController

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A view controller that manages the interface for common text formatting options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
class UITextFormattingViewController
```

```objc
@interface UITextFormattingViewController : UIViewController
```

## Topics

### Classes
- [UITextFormattingViewController.Component](./uitextformattingviewcontroller/component.md)
  Defines text formatting view component.
- [UITextFormattingViewController.ComponentGroup](./uitextformattingviewcontroller/componentgroup.md)
  Defines grouping of text formatting components in view.
- [UITextFormattingViewController.Configuration](./uitextformattingviewcontroller/configuration-swift.class.md)
  Text formatting view controller configuration object.
- [UITextFormattingViewControllerChangeValue](./uitextformattingviewcontrollerchangevalue.md)
  Describes text formatting change that is a result of user action. Contains type of change, any associated value that may be applicable to that change.
- [UITextFormattingViewControllerFormattingDescriptor](./uitextformattingviewcontrollerformattingdescriptor.md)
  Object that represents current text formatting state. This can apply to formatting state of some selected range of text or currently applicable input formatting.
- [UITextFormattingViewControllerFormattingStyle](./uitextformattingviewcontrollerformattingstyle.md)
  Type that defines formatting style presented in text formatting view.
### Global variables
- [static let fontAttributes: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/fontattributes.md)
- [static let fontPicker: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/fontpicker.md)
- [static let fontPointSize: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/fontpointsize.md)
- [static let fontSize: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/fontsize.md)
- [static let formattingStyles: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/formattingstyles.md)
- [static let highlight: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/highlight.md)
- [static let highlightPicker: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/highlightpicker.md)
- [static let lineHeight: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/lineheight.md)
- [static let listStyles: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/liststyles.md)
- [static let textAlignment: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/textalignment.md)
- [static let textAlignmentAndJustification: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/textalignmentandjustification.md)
- [static let textColor: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/textcolor.md)
- [static let textIndentation: UITextFormattingViewController.ComponentKey](./uitextformattingviewcontroller/componentkey/textindentation.md)
- [static let blue: UITextFormattingViewController.Highlight](./uitextformattingviewcontroller/highlight/blue.md)
- [static let `default`: UITextFormattingViewController.Highlight](./uitextformattingviewcontroller/highlight/default.md)
- [static let mint: UITextFormattingViewController.Highlight](./uitextformattingviewcontroller/highlight/mint.md)
- [static let orange: UITextFormattingViewController.Highlight](./uitextformattingviewcontroller/highlight/orange.md)
- [static let pink: UITextFormattingViewController.Highlight](./uitextformattingviewcontroller/highlight/pink.md)
- [static let purple: UITextFormattingViewController.Highlight](./uitextformattingviewcontroller/highlight/purple.md)
- [static let center: UITextFormattingViewController.TextAlignment](./uitextformattingviewcontroller/textalignment/center.md)
- [static let justified: UITextFormattingViewController.TextAlignment](./uitextformattingviewcontroller/textalignment/justified.md)
- [static let left: UITextFormattingViewController.TextAlignment](./uitextformattingviewcontroller/textalignment/left.md)
- [static let natural: UITextFormattingViewController.TextAlignment](./uitextformattingviewcontroller/textalignment/natural.md)
- [static let right: UITextFormattingViewController.TextAlignment](./uitextformattingviewcontroller/textalignment/right.md)
- [static let decimal: UITextFormattingViewController.TextList](./uitextformattingviewcontroller/textlist/decimal.md)
- [static let disc: UITextFormattingViewController.TextList](./uitextformattingviewcontroller/textlist/disc.md)
- [static let hyphen: UITextFormattingViewController.TextList](./uitextformattingviewcontroller/textlist/hyphen.md)
- [static let other: UITextFormattingViewController.TextList](./uitextformattingviewcontroller/textlist/other.md)
### Protocols
- [UITextFormattingViewController.Delegate](./uitextformattingviewcontroller/delegate-swift.protocol.md)
- [UITextFormattingViewControllerDelegate](./uitextformattingviewcontrollerdelegate.md)
### Structures
- [UITextFormattingViewController.FormattingDescriptor](./uitextformattingviewcontroller/formattingdescriptor-swift.struct.md)
- [UITextFormattingViewController.FormattingStyle](./uitextformattingviewcontroller/formattingstyle.md)
### Initializers
- [init()](./uitextformattingviewcontroller/init%28%29.md)
- [init(configuration: UITextFormattingViewController.Configuration)](./uitextformattingviewcontroller/init%28configuration%29.md)
### Instance Properties
- [var configuration: UITextFormattingViewController.Configuration](./uitextformattingviewcontroller/configuration-swift.property.md)
  Current text formatting configuration object.
- [var delegate: (any UITextFormattingViewController.Delegate)?](./uitextformattingviewcontroller/delegate-52zfw.md)
- [var formattingDescriptor: UITextFormattingViewController.FormattingDescriptor?](./uitextformattingviewcontroller/formattingdescriptor-9sir9.md)
- [delegate](./uitextformattingviewcontroller/delegate-1mkbi.md)
- [formattingDescriptor](./uitextformattingviewcontroller/formattingdescriptor-7nlvc.md)
### Enumerations
- [UITextFormattingViewController.ChangeValue](./uitextformattingviewcontroller/changevalue.md)

## Relationships

### Inherits From
- [UIViewController](./uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](./uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](./uiappearancecontainer.md)
- [UIContentContainer](./uicontentcontainer.md)
- [UIFocusEnvironment](./uifocusenvironment.md)
- [UIPasteConfigurationSupporting](./uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](./uiresponderstandardeditactions.md)
- [UIStateRestoring](./uistaterestoring.md)
- [UITraitChangeObservable](./uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](./uitraitenvironment.md)
- [UIUserActivityRestoring](./uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextformattingviewcontroller)*
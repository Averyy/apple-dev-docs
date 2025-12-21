# ControlInfo

**Framework**: WidgetKit  
**Kind**: struct

A structure that contains information about user-configured controls.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ControlInfo
```

## Topics

### Instance Properties
- [let kind: String](controlinfo/kind.md)
  The string specified during creation of the control’s configuration.
- [var pushInfo: ControlPushInfo?](controlinfo/pushinfo.md)
  Push information about a control, if present.
### Instance Methods
- [func configurationIntent<Intent>(of: Intent.Type) -> Intent?](controlinfo/configurationintent(of:).md)
  Gets the associated App Intent.
### Default Implementations
- [Identifiable Implementations](controlinfo/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md)
  Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md)
  Customize the way controls display across the system and offer people the ability to configure them.
- [struct StaticControlConfiguration](staticcontrolconfiguration.md)
  The description of a control that has no user-configurable options.
- [struct AppIntentControlConfiguration](appintentcontrolconfiguration.md)
  The description of a control that uses a custom app intent to provide user-configurable options.
- [class ControlCenter](controlcenter.md)
  An object you use to access configuration information for controls and reload them.
- [struct ControlWidgetButton](controlwidgetbutton.md)
  A control template representing a button.
- [struct ControlWidgetToggle](controlwidgettoggle.md)
  A control template representing a toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlinfo)*
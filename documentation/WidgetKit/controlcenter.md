# ControlCenter

**Framework**: WidgetKit  
**Kind**: class

An object you use to access configuration information for controls and reload them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class ControlCenter
```

#### Overview

ControlCenter provides information about user-configured controls, such as their push information.

For additional information about offering controls that allow people to perform app actions; – for example, in Control Center on iPhone – refer to [`Creating controls to perform actions across the system`](creating-controls-to-perform-actions-across-the-system.md). For more information about offering user-configured controls, refer to [`Add configuration to a control`](adding-refinements-and-configuration-to-controls#Add-configuration-to-a-control.md).

##### Access Configured Control Information

To get a list of user-configured controls, use [`currentControls()`](controlcenter/currentcontrols().md). This property provides an array of [`ControlInfo`](controlinfo.md) objects containing the following information:

```swift
struct ControlInfo {
    public let kind: String
    public func configurationIntent<Intent: ControlConfigurationIntent>(of intentType: Intent.Type = Intent.self) -> Intent?
    public var pushInfo: ControlPushInfo?
}
```

The `kind` string matches the parameter you use when defining the control type. If your control uses a [`AppIntentControlConfiguration`](appintentcontrolconfiguration.md), the [`configurationIntent(of:)`](controlinfo/configurationintent(of:).md) function provides the custom intent containing the user-customized values for each individual control. If your control receives push notification updates, [`pushInfo`](controlinfo/pushinfo.md) returns the push token you use to update it.

For more information about updating controls with WidgetKit push notifications, refer to [`Updating controls locally and remotely`](updating-controls-locally-and-remotely.md).

##### Request a Reload of Your Controls

Changes in your app’s state may affect a control’s state. When this happens, you can tell `ControlCenter` to reload the template for either a specific kind of control or all controls. For example, someone might press a button in your app that changes state shared by a control. The app should reload that control for its display to reflect the new state.

You don’t need to reload controls in response to push notifications. The system reloads any controls that receive push notification updates on your behalf.

If you only need to reload a certain kind of control, you can request a reload for only that kind. For example, in response to the user toggling an appliance on or off, you could request a reload for only the appliance widgets:

```swift
ControlCenter.shared.reloadControls(ofKind: "com.myhome.appliancepower")
```

To request a reload for all of your controls:

```swift
ControlCenter.shared.reloadAllControls()
```

## Topics

### Instance Methods
- [func currentControls() async throws -> [ControlInfo]](controlcenter/currentcontrols.md)
  Retrieves information about user-configured controls.
- [func reloadAllControls()](controlcenter/reloadallcontrols.md)
  Reloads the templates for all configured controls belonging to the containing app.
- [func reloadControls(ofKind: String)](controlcenter/reloadcontrols(ofkind:).md)
  Reloads the templates for all controls of a particular kind.
### Type Properties
- [static let shared: ControlCenter](controlcenter/shared.md)

## See Also

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md)
  Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md)
  Customize the way controls display across the system and offer people the ability to configure them.
- [struct StaticControlConfiguration](staticcontrolconfiguration.md)
  The description of a control that has no user-configurable options.
- [struct AppIntentControlConfiguration](appintentcontrolconfiguration.md)
  The description of a control that uses a custom app intent to provide user-configurable options.
- [struct ControlInfo](controlinfo.md)
  A structure that contains information about user-configured controls.
- [struct ControlWidgetButton](controlwidgetbutton.md)
  A control template representing a button.
- [struct ControlWidgetToggle](controlwidgettoggle.md)
  A control template representing a toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlcenter)*
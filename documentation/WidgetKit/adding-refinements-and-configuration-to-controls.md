# Adding refinements and configuration to controls

**Framework**: Widgetkit

Customize the way controls display across the system and offer people the ability to configure them.

#### Overview

You can use controls to allow people to enhance Control Center, the Lock Screen, and the Action button with actions from your app. Each system space displays controls differently, adding or removing information where needed: for example, people can resize controls in Control Center. Depending on the size, the title and value text aren’t always visible. Refine controls to display in different system spaces and provide people with the information they need.

Controls perform an action, and can provide configuration options to allow someone to customize what the action does, such as choosing which light to turn on and off. Consider if configuration is a good choice for your control.

##### Customize Your Controls Name and Description

By default, the name of your app displays as the name for your control when the control appears in the controls gallery, and control toggles display in their inactive state. Customize your control’s name if your app offers multiple controls or to provide more context about what your control does. Customize the name of your control using the [`displayName(_:)`](https://developer.apple.com/documentation/SwiftUI/ControlWidgetConfiguration/displayName(_:)) modifier. Localize your control’s name, if applicable.

The control’s configuration view displays a localizable description for a control. Add a description, using the [`description(_:)`](https://developer.apple.com/documentation/SwiftUI/ControlWidgetConfiguration/description(_:)) modifier, to give additional information about what the control does.

The following code adds a name and description to the control that gives people more insight about what it does:

```swift
struct TimerToggle: ControlWidget {
	static let kind: String = "com.example.MyApp.TimerToggle"

	var body: some ControlWidgetConfiguration {
		StaticControlConfiguration(
			...
		) {
			ControlWidgetToggle(
				...
			)
		}
		.displayName("Productivity Timer")
		.description("Start and stop a productivity timer.")
	}
}
```

##### Enforce Security and Privacy for Controls

Controls can require a device to be authenticated to allow the control to perform its action or to display its current state and information. Set the `authenticationPolicy` in the control’s app intent to refine what level of authentication is necessary to perform the action.

The following code sets the [`authenticationPolicy`](https://developer.apple.com/documentation/AppIntents/AppIntent/authenticationPolicy-1r9kh) to [`IntentAuthenticationPolicy.requiresAuthentication`](https://developer.apple.com/documentation/AppIntents/IntentAuthenticationPolicy/requiresAuthentication) to require device authentication to unlock a door:

```swift
struct UnlockDoor: AppIntent {
	static let title: LocalizedStringResource = "Unlock the door"
	static let authenticationPolicy = .requiresAuthentication
	...
}
```

Use the [`privacySensitive(_:)`](https://developer.apple.com/documentation/SwiftUI/ControlWidgetTemplate/privacySensitive(_:)) modifier on a [`ControlWidgetTemplate`](https://developer.apple.com/documentation/SwiftUI/ControlWidgetTemplate) type to redact the active or inactive state of a control while the device isn’t authenticated.

The following code adds the `privacySensitive()` modifier to a control toggle. The modifier redacts the state and information in the control that displays whether a door is open or closed:

```swift
struct DoorOpener: ControlWidget {
	var body: some ControlWidgetConfiguration {
		StaticControlConfiguration(...) {
			ControlWidgetToggle(...) {
				Label(
					isOpen ? "Open" : "Closed",
					systemImage: isOpen ? "door.open" : "door.closed"
				)
			}
			.privacySensitive()
		}
	}
}
```

You may use the `privacySensitive()` modifier on a control’s value or label individually to redact that information when a device isn’t authenticated, but the control’s active or inactive state will still be visible.

Require authentication if a control performing its action would be problematic if done unintentionally or not by the device owner. Redact information if a control displays personally identifiable or security-related information or state.

##### Refine Action Button Hint Text

The Action button gives quick and easy access to controls and system functionality. Provide hint text to people to help give context to the action the control performs. The text set with the `displayName` modifier on the [`StaticControlConfiguration`](staticcontrolconfiguration.md) or [`AppIntentControlConfiguration`](appintentcontrolconfiguration.md) provides text to the system to display a hint. The default hint text is different for buttons, toggles, and buttons that have an [`OpenIntent`](https://developer.apple.com/documentation/AppIntents/OpenIntent) action to launch an app.

The following code shows the default hint text for a button:

```swift
// Hint Text: "Hold for 'Perform Action'"
struct PerformActionButton: ControlWidget {
	var body: some ControlWidgetConfiguration {
		StaticControlConfiguration(...) {
			...
		}
		.displayName("Perform Action")
	}
}
```

The following code shows the default hint text for a button with an `OpenIntent` action:

```swift
// Hint Text: "Hold to Open MyApp"
struct MyAppLauncher: ControlWidget {
	var body: some ControlWidgetConfiguration {
		StaticControlConfiguration(...) {
			ControlWidgetButton(
				action: OpenMyAppIntent(),
				...
			)
		}
		.displayName("MyApp")    
	}
}
```

Hint text for a toggle prepends with “Hold to Turn On…” and “Hold to Turn Off…” The following code shows the default hint text for a toggle:

```swift
// Hint Text: "Hold to Turn On 'Lightswitch'" / "Hold to Turn Off 'Lightswitch'"
struct LightswitchToggle: ControlWidget {
	var body: some ControlWidgetConfiguration {
		StaticControlConfiguration(...) {
			...
		}
		.displayName("Lightswitch")
	}
}
```

Use [`Label`](https://developer.apple.com/documentation/SwiftUI/Label) and the [`controlWidgetActionHint(_:)`](https://developer.apple.com/documentation/SwiftUI/View/controlWidgetActionHint(_:)) modifier in your control content to create fully custom hint text. Begin the  `controlWidgetActionHint` with a verb, similar to [`accessibilityHint(_:isEnabled:)`](https://developer.apple.com/documentation/SwiftUI/View/accessibilityHint(_:isEnabled:)).

When you customize hint text for button controls, the hint text prepends with “Hold to…” The following code shows custom hint text for a button:

```swift
// Hint Text: "Hold to Perform the Action"
ControlWidgetButton(...) {
	Label("Perform Action", systemName: "checkmark.circle")
		.controlWidgetActionHint("Perform the Action")
}
```

The following code shows custom hint text for a button with an `OpenIntent` action. The hint text is the same as a button, but when executed, this action launches the app:

```swift
// Hint Text: "Hold to Perform the Action"
ControlWidgetButton(...) {
	Image(systemName: "checkmark.circle")
		.controlWidgetActionHint("Perform the Action")
}
```

Customize toggles using custom value text or a custom action hint. Custom hint text using custom value text prepends with “Hold for…” Custom hint text using a custom action hint prepends with “Hold to…”

The following code shows custom hint text for a toggle using custom value text:

```swift
// Hint Text: "Hold for Lights On" / "Hold for Lights Off"
ControlWidgetToggle(...) { isOn in
	Label(
		isOn ? "Lights On" : "Lights Off",
		systemImage: isOn ? "lightbulb.max" : "lightbulb"
	)
}
```

The following code uses the `controlWidgetActionHint` modifier to display custom hint text:

```swift
// Hint Text: "Hold to Turn on Lights" / "Hold to Turn off Lights"
ControlWidgetToggle(...) { isOn in
	Label(
		isOn ? "On" : "Off",
		systemImage: isOn ? "lightbulb.max" : "lightbulb"
	)
	.controlWidgetActionHint(isOn ? "Turn on Lights" : "Turn off Lights")
}
```

> **Note**: `controlsWidgetActionHint` takes precedence over custom value text `Label` provides.

##### Add Control Center Status Text

Use the [`controlWidgetStatus(_:)`](https://developer.apple.com/documentation/SwiftUI/View/controlWidgetStatus(_:)) modifier to display momentary status text in Control Center when a control’s action is performed. Status text conveys additional information about the control’s state or the duration of effectiveness of the state. For example, status text might display the time a car idles before turning off after being remotely started.

Use status text sparingly and only in situations where important information isn’t conveyed by the control.

##### Add Configuration to a Control

Make a control configurable to enable people to use multiple controls and to set them up to perform different actions, such as selecting a productivity timer instead of a reading timer.

To make a control configurable, use an [`AppIntentControlConfiguration`](appintentcontrolconfiguration.md) and conform your value provider to [`AppIntentControlValueProvider`](appintentcontrolvalueprovider.md). This step tells the system you provide the ability for someone to configure the control when they long press the control, in edit mode, in Control Center, on the Lock Screen, and when they configure the control for the Action button.

The following code creates a control toggle that starts and stops a timer. Someone can configure the control and select their desired type of timer. The control uses `AppIntentControlConfiguration` and sets the name of the control to the name of the configured timer. `ToggleTimerIntent` acts on the selected timer. The control has a provider that uses `AppIntentControlValueProvider` and has a custom app intent, `SelectTimerIntent`, that provides the type of timer choices:

```swift
struct TimerToggle: ControlWidget {
	static let kind: String = "com.example.MyApp.TimerToggle"

	var body: some ControlWidgetConfiguration {
		AppIntentControlConfiguration(
			kind: Self.kind,
			provider: ConfigurableProvider()
		) { timerState in
			ControlWidgetToggle(
				timerState.timer.name,
				isOn: timerState.isRunning,
				action: ToggleTimerIntent(timer: timerState.timer),
				valueLabel: { isOn in
					Label(isOn ? "Running" : "Stopped", systemImage: "timer")
				}
			)
		}
		.displayName("Productivity Timer")
		.description("Start and stop a productivity timer.")
	}
}

extension TimerToggle {
	struct ConfigurableProvider: AppIntentControlValueProvider {
		func previewValue(configuration: SelectTimerIntent) -> TimerState {
			return TimerState(timer: configuration.timer, isRunning: false)
		}

		func currentValue(configuration: SelectTimerIntent) async throws -> TimerState {b
			let timer = configuration.timer
			let isRunning = try await TimerManager.shared.fetchTimerRunning(timer: timer)
			
			return TimerState(timer: timer, isRunning: isRunning)
		}
	}
}
```

A control that requires configuration to be functional can use the `promptsForUserConfiguration` modifier to have the system automatically prompt someone for configuration when they add it to Control Center or the Lock Screen, or configure it for the Action button.

The following code uses the [`promptsForUserConfiguration()`](https://developer.apple.com/documentation/SwiftUI/ControlWidgetConfiguration/promptsForUserConfiguration()) modifier on the `AppIntentControlConfiguration` to prompt someone to configure the control when they choose it:

```swift
struct TimerToggle: ControlWidget {
	static let kind: String = "com.example.MyApp.TimerToggle"

	var body: some ControlWidgetConfiguration {
		AppIntentControlConfiguration(
			...
		) { timerState in
			ControlWidgetToggle(
				...
			)
		}
		.promptsForUserConfiguration()
	}
}
```

## See Also

- [Creating controls to perform actions across the system](creating-controls-to-perform-actions-across-the-system.md)
  Perform your app’s actions from Control Center, the Lock Screen, and the Action button.
- [struct ControlWidgetToggle](controlwidgettoggle.md)
  A control template representing a toggle.
- [struct ControlWidgetButton](controlwidgetbutton.md)
  A control template representing a button.
- [class ControlCenter](controlcenter.md)
  An object that contains a list of user-configured controls and is used for reloading controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WidgetKit/adding-refinements-and-configuration-to-controls)*
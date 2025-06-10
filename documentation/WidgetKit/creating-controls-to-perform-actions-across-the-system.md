# Creating controls to perform actions across the system

**Framework**: WidgetKit

Perform your app’s actions from Control Center, the Lock Screen, and the Action button.

#### Overview

A control allows your app to execute an action, launch your app to a specific view, or launch a locked camera capture extension from Control Center, the Lock Screen, or by using the Action button. Customers configure these system spaces with your app’s controls.

Controls can be buttons or toggles: buttons perform an action, and toggles perform an action and switch between two states. Configure a control using SwiftUI views and modifiers that define strings and icons that the system uses to display the control. Anticipate people using controls from different places throughout the system, and provide appropriate configuration details for the best experience. For added privacy, require device authentication before a control performs its action, as well as redact the text in a control when the device is locked.

Create your control’s icon using a symbol image, such as one from [`SF Symbols`](https://developer.apple.com/design/Human-Interface-Guidelines/sf-symbols). Using symbols allows the system to dynamically apply tint color, weight, scale, and other stylistic traits. While Apple platforms include thousands of symbols, you can also build custom symbols. To learn more, read [`Creating custom symbol images for your app`](https://developer.apple.com/documentation/UIKit/creating-custom-symbol-images-for-your-app).

Make controls configurable to allow someone to choose what it does. This ability is helpful in cases where a control can be configured with a list of options, such as which light to turn on or off.

##### Understand the Control Lifecycle

The system loads a control when someone adds it to a system space from the controls gallery. A control updates when someone interacts with it, when the app asks to reload it using the shared [`ControlCenter`](controlcenter.md), or when the system receives a remote push notification from the Apple Push Notification service (APNs). When the system loads or reloads a control, it runs the body of the control from the widget extension and asks for the control’s current value and content for the current state. The system updates the displayed control with these values.

Controls provide their values to the system using a [`ControlValueProvider`](controlvalueprovider.md) or an [`AppIntentControlValueProvider`](appintentcontrolvalueprovider.md). Providers require two functions: [`previewValue`](controlvalueprovider/previewvalue.md) and [`currentValue()`](controlvalueprovider/currentvalue().md). `previewValue` prepares a canned synchronous value to show people when the control displays in the controls gallery. The controls gallery displays controls using their preview value and in their inactive state. The system fetches the `currentValue()` when the control renders. The system fetches this value asynchronously, and gives you the opportunity to fetch the value from a shared data source or a server. Use a custom intent with `AppIntentControlValueProvider` to provide options for a configurable control.

When someone interacts with a control, it performs its action using an app intent you specify. Use [`AppIntent`](https://developer.apple.com/documentation/AppIntents/AppIntent) or [`OpenIntent`](https://developer.apple.com/documentation/AppIntents/OpenIntent) for control buttons and [`SetValueIntent`](https://developer.apple.com/documentation/AppIntents/SetValueIntent) for control toggles. The app intent requires a [`perform()`](https://developer.apple.com/documentation/AppIntents/AppIntent/perform()) function  in which you carry out actions. The system queries for the state of a control when `perform()` returns; finish all actions and save all state data before it returns.

You may pass additional data into the app intent to ensure it successfully performs its action. The system preserves the data and makes it available in the `perform()` function inside the app intent. Annotate additional data you pass in with `@Parameter`. For more information on `AppIntent`, refer to [`AppIntent`](https://developer.apple.com/documentation/AppIntents/AppIntent).

The system populates the value parameter of a `SetValueIntent` with the value that reflects the new state of the control toggle. Don’t set or manage the value parameter. Update the internal state or model data to this value to remain consistent with the appearance of the control.

##### Add a Control Toggle to Your App

The Widget Extension template provides all you need to start building your control. The template creates a widget extension target that contains a [`ControlWidgetToggle`](controlwidgettoggle.md).

1. Open your app project in Xcode and choose File > New > Target.
2. From the Application Extension group, select Widget Extension, and click Next.
3. Enter the name of your extension.
4. Select the Include Control checkbox.
5. Click Finish.

> **Note**: Live Activities use WidgetKit and share many aspects of their design and implementation with the widgets in your app. If your app would benefit from Live Activities, consider implementing them at the same time you add controls or widgets. For more information about Live Activities, read [`Displaying live data with Live Activities`](https://developer.apple.com/documentation/ActivityKit/displaying-live-data-with-live-activities).

The widget extension template provides an initial implementation of a `ControlWidgetToggle`, a [`ControlWidgetTemplate`](https://developer.apple.com/documentation/SwiftUI/ControlWidgetTemplate) type that starts and stops a timer. The body property determines if a control is static or configurable. Controls use a [`StaticControlConfiguration`](staticcontrolconfiguration.md) for the body property by default. Provide people with the ability to configure a control by using [`AppIntentControlConfiguration`](appintentcontrolconfiguration.md).

The following code creates a nonconfigurable control toggle that starts and stops a timer. The `kind` is the control’s unique identifier and the action of the `ControlWidgetToggle` executes the app intent specified:

```swift
struct TimerToggle: ControlWidget {
	static let kind: String = "com.example.MyApp.TimerToggle"

	var body: some ControlWidgetConfiguration {
		StaticControlConfiguration(
			kind: Self.kind,
			provider: Provider()
		) { value in
			ControlWidgetToggle(
				"Productivity Timer",
				isOn: value,
				action: ToggleTimerIntent(),
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
	struct Provider: ControlValueProvider {
		var previewValue: Bool {
			false
		}

		func currentValue() async throws -> Bool {
			let isRunning = true // Check if the timer is running
			return isRunning
		}
	}
}

struct ToggleTimerIntent: SetValueIntent {
	static var title: LocalizedStringResource = "Productivity Timer"

	@Parameter(title: "Timer is running")
	var value: Bool

	func perform() async throws -> some IntentResult {
		// Start / stop the timer based on `value`.
		return .result()
	}
}
```

##### Create a Button Control

A control button performs an action from your app. For example, the button can launch a locked camera capture extension, start a live activity, or take someone to a specific area of your app.

The following code creates a nonconfigurable [`ControlWidgetButton`](controlwidgetbutton.md) that uses an app intent to perform an action:

```swift
struct PerformActionButton: ControlWidget {
	var body: some ControlWidgetConfiguration {
		StaticControlConfiguration(
			kind: "com.example.myApp.performActionButton"
		) {
			ControlWidgetButton(action: PerformAction()) {
                Label("Perform Action", systemImage: "checkmark.circle")
			}
		}
		.displayName("Perform Action")
		.description("An example control that performs an action.")
	}
}

struct PerformAction: AppIntent {
	static let title: LocalizedStringResource = "Perform action"

	func perform() async throws -> some IntentResult {
		// Code that performs the action...
		return .result()
	}
}
```

##### Open Your App with a Control

Set your control’s action to an app intent that conforms to [`OpenIntent`](https://developer.apple.com/documentation/AppIntents/OpenIntent) to open your app when someone uses a control. Using `OpenIntent` allows you to take someone to a specific area of your app when a control performs its action.

The system requires the Target Membership of the app intent to be set to both the app and the widget extension to open the app.

The following code uses an app intent to launch the app to a specific screen when a `ControlWidgetButton` performs its action:

```swift
import AppIntents

struct LaunchAppIntent: OpenIntent {
    static var title: LocalizedStringResource = "Launch App"
    @Parameter(title: "Target")
    var target: LaunchAppEnum
}

enum LaunchAppEnum: String, AppEnum {
    case timer
    case history

    static var typeDisplayRepresentation = TypeDisplayRepresentation("Productivity Timer's app screens")
    static var caseDisplayRepresentations = [
        LaunchAppEnum.timer : DisplayRepresentation("Timer"),
        LaunchAppEnum.history : DisplayRepresentation("History")
    ]
}
```

> **Note**: Use a control button to launch a locked camera capture extension. For more information about creating a locked camera capture extension, refer to [`Creating a camera experience for the Lock Screen`](https://developer.apple.com/documentation/LockedCameraCapture/Creating-a-camera-experience-for-the-Lock-Screen).

##### Add Controls to Your Widget Bundle

The [`WidgetBundle`](https://developer.apple.com/documentation/SwiftUI/WidgetBundle) in the Widget extension provides controls and widgets to the system from your app. List all controls and widgets inside the `WidgetBundle`. The order of controls and widgets in the `WidgetBundle` defines the order that the controls gallery and widgets gallery will display them in.

```swift
@main
struct MyControlsAndWidgetsBundle: WidgetBundle {
	var body: some Widget {
		PerformActionButton()
		MyAppWidget()
		MyAppControlToggle()
	}
}
```

## See Also

- [Adding refinements and configuration to controls](adding-refinements-and-configuration-to-controls.md)
  Customize the way controls display across the system and offer people the ability to configure them.
- [struct ControlWidgetToggle](controlwidgettoggle.md)
  A control template representing a toggle.
- [class ControlCenter](controlcenter.md)
  An object that contains a list of user-configured controls and is used for reloading controls.
- [struct ControlWidgetButton](controlwidgetbutton.md)
  A control template representing a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/creating-controls-to-perform-actions-across-the-system)*
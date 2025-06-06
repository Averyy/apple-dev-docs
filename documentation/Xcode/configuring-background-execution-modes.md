# Configuring background execution modes

**Framework**: Xcode

Indicate the background services your app requires to continue executing in the background in iOS, iPadOS, tvOS, visionOS, and watchOS.

#### Overview

Typically, an app is in a suspended state when it’s in the background. However, there are a limited number of background execution modes your app can support that enable it to run when in the background, such as playing audio, receiving location updates, or processing scheduled tasks. For apps that adopt one or more of these modes, the system launches or resumes the app, in the background, and affords it time to process any related events.

Use background execution modes sparingly because overuse can negatively impact device performance and battery life. If an alternative to executing in the background exists, use the alternative instead. For example, apps can use the significant-change location service to receive location events as an alternative to using the Location updates background mode.

Before you can select the background execution modes your app requires, follow the steps in [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) to add the Background Modes capability to your app’s target.

![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from Background Modes to Game Center, and the Background Modes capability is in a selected state. The text on the information pane explains that, with Background Modes, your app can provide specific background services that need to continue running while in the background. It also advises using Background Modes sparingly and only by apps that provide the indicated services. And when alternatives exist for running in the background, to use those alternatives instead.](https://docs-assets.developer.apple.com/published/849e64816dc2de3392eef76c9f619038/background-modes%402x.png)

The background execution modes that appear after you add the capability depend on the target’s platform. For watchOS apps with separate WatchKit extensions, you need to add the capability to the WatchKit Extension target.

> **Note**: The Background Modes capability isn’t available for macOS apps.

The Background Modes capability isn’t available for macOS apps.

##### Specify the Background Modes Your App Requires

Before your app can leverage one or more background execution modes, you need to declare the modes it requires by performing the following:

1. Select your project in Xcode’s Project navigator.
2. Select the app’s target in the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Background Modes capability.
5. Select one or more background execution modes using the corresponding checkboxes.
6. For watchOS apps, choose the appropriate session type from the pop-up menu. For more information, see [`Using extended runtime sessions`](https://developer.apple.com/documentation/WatchKit/using-extended-runtime-sessions).

![A screenshot of the Background Modes capability after you add it to a target. The list of available modes includes Audio, AirPlay, and Picture in Picture; Location Updates; Voice over IP; External accessory communication; Uses Bluetooth LE accessories; Acts as a Bluetooth LE accessory; Background fetch; Remote notifications; Background processing; Uses Nearby Interaction; and Push to Talk. The checkbox for the Background fetch mode is selected.](https://docs-assets.developer.apple.com/published/7bf683d304b6e6c322c31bdf47d06b83/modes%402x.png)

Xcode adds the [`UIBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIBackgroundModes) array to your app’s `Info.plist` file, if it isn’t already present, and uses the modes you select to populate the array with the necessary values.

Apple’s platforms support these background execution modes:

| Mode | Value | Description | Platforms |
| --- | --- | --- | --- |
| Audio, AirPlay, and Picture in Picture | `audio` | The app plays audible content in the background. For more information, see [`Configuring your app for media playback`](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback). | iOS, iPadOS, tvOS, visionOS |
| Audio | `audio` | The app plays audible content in the background. For more information, see [`Playing Background Audio`](https://developer.apple.com/documentation/WatchKit/playing-background-audio). | watchOS |
| Location updates | `location` | The app provides location-based information and requires the use of the platform’s standard location service. For more information, see [`Configuring your app to use location services`](https://developer.apple.com/documentation/CoreLocation/configuring-your-app-to-use-location-services). | iOS, iPadOS, watchOS |
| Voice over IP | `voip` | The app provides Voice over IP services. For more information, see the [`CallKit`](https://developer.apple.com/documentation/CallKit) framework. | iOS, iPadOS, visionOS, watchOS |
| External accessory communication | `external-accessory` | The app communicates with an accessory that delivers data at regular intervals. For more information, see the [`External Accessory`](https://developer.apple.com/documentation/ExternalAccessory) framework. | iOS, iPadOS |
| Uses Bluetooth LE accessories | `bluetooth-central` | The app communicates with a Bluetooth accessory while in the background. For more information, see the [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth) framework. | iOS, iPadOS, visionOS |
| Acts as a Bluetooth LE accessory | `bluetooth-peripheral` | The app uses peripheral mode to communicate with a Bluetooth accessory. For more information, see the [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth) framework. | iOS, iPadOS |
| Background fetch | `fetch` | The app requires new content from the network at regular intervals. For more information, see [`Using background tasks to update your app`](https://developer.apple.com/documentation/UIKit/using-background-tasks-to-update-your-app). | iOS, iPadOS, tvOS, visionOS |
| Remote notifications | `remote-notification` | The app uses push notifications as a signal that new content is available to download. For more information, see [`Pushing background updates to your App`](https://developer.apple.com/documentation/UserNotifications/pushing-background-updates-to-your-app). | iOS, iPadOS, tvOS, visionOS, watchOS |
| Background processing | `processing` | The app executes scheduled tasks while in the background. For more information, see [`BGTaskScheduler`](https://developer.apple.com/documentation/BackgroundTasks/BGTaskScheduler). | iOS, iPadOS, tvOS, visionOS |
| Workout processing | `workout-processing` | The app uses a workout session to track a user’s activity on Apple Watch. For more information, see [`Running workout sessions`](https://developer.apple.com/documentation/HealthKit/running-workout-sessions). | watchOS |
| Uses Nearby Interaction | `nearby-interaction` | The app locates and interacts with nearby devices. For more information, see the [`Nearby Interaction`](https://developer.apple.com/documentation/NearbyInteraction) framework. | iOS, iPadOS |
| Push to Talk | `push-to-talk` | The app launches in response to a push notification and plays audible content in the background. For more information, see the [`Push to Talk`](https://developer.apple.com/documentation/PushToTalk) framework. | iOS, iPadOS |

## See Also

- [Configuring custom fonts](configuring-custom-fonts.md)
  Register your app as a provider or consumer of systemwide custom fonts.
- [Configuring game controllers](configuring-game-controllers.md)
  Enhance gameplay input by enabling the discovery, configuration, and use of physical game controllers.
- [Configuring Maps support](configuring-maps-support.md)
  Register your iOS routing app to provide point-to-point directions to Maps and other apps.
- [Configuring Siri support](configuring-siri-support.md)
  Enable your app and its Intents extension to resolve, confirm, and handle user-driven Siri requests for your app’s services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-background-execution-modes)*
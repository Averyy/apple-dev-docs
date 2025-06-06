# watchOS apps

**Framework**: Watchos Apps

Build watchOS apps that combine complications, notifications, and Siri to create a personal experience on Apple Watch.

#### Overview

Apple Watch provides easy access to vital information on someone’s wrist. The watchOS experience focuses on quick actions that achieve useful tasks through brief, punctuated interactions.

![An illustration showing an Apple Watch surrounded by icons representing common features, including creating user interfaces, playing background audio, and displaying custom notifications.](https://docs-assets.developer.apple.com/published/338a988aa783dd6f74046d0101407df4/WatchKit-1%402x.png)

On Apple Watch, keep interactions as short as possible. Provide vital information at a glance, encouraging the wearer to respond with just a few taps, and then drop their wrist and move on. They don’t need to wait to see if the action succeeds; instead, the watchOS app automatically notifies them of any important updates.

For watchOS, expect to spend more time planning, designing, and refining your app’s experience than writing the actual code. For design guidance, see [`Designing for watchOS`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/platforms/designing-for-watchos/).

When designing a watchOS app, mix a combination of the following technologies to create a richer experience.

#### The Watchos App

The main app serves as the foundation for your watchOS app experience. Anyone can launch and interact with your app directly. However, the app’s interface isn’t necessarily the primary way people interact with your app. Many may prefer to interact through complications or notifications, and may never explicitly launch your app.

![An illustration of a watch face showing four watchOS app icons.](https://docs-assets.developer.apple.com/published/c54dd895f3e9d547684408b76e0e797e/app%402x.png)

#### Complications

Complications provide small glimpses into your app’s data directly on the watch face. People can add complications to most watch faces, but space is limited. Design complications to show information that is timely, up to date, and useful. People can also launch the watchOS app quickly and easily by tapping a complication.

![An illustration of a watch face with the corners highlighted to represent corner complications.](https://docs-assets.developer.apple.com/published/a9fbf6cf8c536511a2692372542da3b5/complications%402x.png)

#### Notifications

Use notifications to alert people of significant events. You can also provide actions so that people can respond immediately without opening your app. You can use either local or remote notifications to communicate, even when your app isn’t running.

![An illustration of a watch face showing a notification icon and two bars representing notification text.](https://docs-assets.developer.apple.com/published/68f83998b0e0117749ab87023203291c/notification%402x.png)

#### Siri

Use SiriKit and App intents to expand the ways people can interact with your app. If your app uses domains like messaging or media, use [`SiriKit`](https://developer.apple.com/documentation/SiriKit) to add Siri support to your app. For other features, use [`App Intents`](https://developer.apple.com/documentation/AppIntents) to expose your app’s functionality to system services like Siri and the Shortcuts app.

![An illustration of a watch face showing the Siri icon and the text What can I help you with?](https://docs-assets.developer.apple.com/published/55a6be7ce63438fdc13d04ae6b715a30/siri%402x.png)

## Topics

### Essentials
- [Creating an intuitive and effective UI in watchOS 10](creating-an-intuitive-and-effective-ui-in-watchos-10.md)
  Provide an even more streamlined, consistent, and glanceable user experience with new design features.
- [Updating your app and widgets for watchOS 10](updating-your-app-and-widgets-for-watchos-10.md)
  Integrate SwiftUI elements and watch-specific features, and build widgets for the Smart Stack.
- [Building a watchOS app](building_a_watchos_app.md)
  Set up your app’s life cycle and create its user interface with SwiftUI.
- [watchOS updates](../Updates/watchos.md)
  Learn about important changes to watchOS.
### App experience
- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [Creating independent watchOS apps](creating-independent-watchos-apps.md)
  Set up a watchOS app that installs and runs without a companion iOS app.
- [Keeping your watchOS content up to date](keeping-your-watchos-app-s-content-up-to-date.md)
  Ensure that your app’s content is relevant and up to date.
- [Updating watchOS apps with timelines](updating-watchos-apps-with-timelines.md)
  Seamlessly schedule updates to your user interface, even while it’s inactive.
- [Authenticating users on Apple Watch](authenticating-users-on-apple-watch.md)
  Create an account sign-up and sign-in strategy for your app.
- [Responding to the Action button on Apple Watch Ultra](../AppIntents/ActionButtonArticle.md)
  Use App Intents to register actions for your app.
- [Enabling the double-tap gesture on Apple Watch](enabling-double-tap.md)
  Customize your app’s response to the double-tap gesture on Apple Watch.
### Accessibility
- [Create accessible experiences for watchOS](create-accessible-experiences-for-watchos.md)
  Learn how to make your watchOS app more accessible.
### User interface
- [Building a productivity app for Apple Watch](building-a-productivity-app-for-apple-watch.md)
  Create a watch app to manage and share a task list and visualize the status with a chart.
- [Supporting multiple watch sizes](supporting-multiple-watch-sizes.md)
  Customize the layout of your user interface to support all Apple Watch sizes.
- [Designing your app for the Always On state](designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.
- [Setting the app’s accent color](setting-the-app-s-accent-color.md)
  Set your app’s accent color.
### Complications
- [Creating accessory widgets and watch complications](../WidgetKit/Creating-accessory-widgets-and-watch-complications.md)
  Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [Migrating ClockKit complications to WidgetKit](../WidgetKit/Converting-A-ClockKit-App.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
- [Creating a widget extension](../WidgetKit/Creating-a-Widget-Extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](../WidgetKit/Keeping-a-Widget-Up-To-Date.md)
  Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Increasing the visibility of widgets in Smart Stacks](../WidgetKit/Widget-Suggestions-In-Smart-Stacks.md)
  Donate intents and indicate relevance to automatically show your widget in Smart Stacks when it has useful information to display.
### Notifications
- [Notifications](notifications.md)
  Communicate with users even when your app isn’t running.
### Siri
- [Making actions and content discoverable and widely available](../AppIntents/Making-actions-and-content-discoverable-and-widely-available.md)
  Adopt App Intents to make your app discoverable with Spotlight, controls, widgets, and the Action button.
- [Creating an Intents App Extension](../SiriKit/creating-an-intents-app-extension.md)
  Add and configure an Intents app extension in your Xcode project.
### Health and fitness
- [Setting up HealthKit](../HealthKit/setting-up-healthkit.md)
  Set up and configure your HealthKit store.
- [Authorizing access to health data](../HealthKit/authorizing-access-to-health-data.md)
  Request permission to read and share data in your app.
- [Saving data to HealthKit](../HealthKit/saving-data-to-healthkit.md)
  Create and share HealthKit samples.
- [Reading data from HealthKit](../HealthKit/reading-data-from-healthkit.md)
  Use queries to request sample data from HealthKit.
- [Build a workout app for Apple Watch](../HealthKit/build-a-workout-app-for-apple-watch.md)
  Create your own workout app, quickly and easily, with HealthKit and SwiftUI.
### Runtime management
- [Background execution](../WatchKit/background-execution.md)
  Manage background sessions and tasks.
- [Life cycles](../WatchKit/life-cycles.md)
  Receive and respond to life-cycle notifications.
- [Using extended runtime sessions](../WatchKit/using-extended-runtime-sessions.md)
  Create an extended runtime session that continues running your app after the user stops interacting with it.
- [Interacting with Bluetooth peripherals during background app refresh](../WatchKit/interacting-with-bluetooth-peripherals-during-background-app-refresh.md)
  Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.
### Network requests
- [Making default and ephemeral requests](making-default-and-ephemeral-requests.md)
  Send requests from your app when it’s running in the foreground.
- [Making background requests](making-background-requests.md)
  Send requests from your app when it’s running in the background.
### Unit tests
- [Setting up tests for your watchOS app](setting-up-tests-for-your-watchos-app.md)
  Configure your watch-only project with unit tests and user interface tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchOS-Apps)*
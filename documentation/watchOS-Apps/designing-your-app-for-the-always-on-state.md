# Designing your app for the Always On state

**Framework**: watchOS apps

Customize your watchOS app’s user interface for continuous display.

#### Overview

The launch of watchOS 6 introduced the Always On state. Supported devices continued to display the time, even when the user isn’t actively interacting with the watch; however, when running an app, the system blurs the app’s user interface and displays the time over it.

In watchOS 8, Always On expands to include your apps. Apple Watch continues to display your app’s user interface as long as it’s either the frontmost app or running a background session. To preserve battery life, the system updates the user interface at a much lower frequency than when running in the foreground. It also dims the watch.

Even though your app is inactive or running in the background, the system continues to update and monitor many of the user interface elements. For example, when displaying dates and times, using [`Text.DateStyle`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle) values like [`relative`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle/relative), [`offset`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle/offset), and [`timer`](https://developer.apple.com/documentation/SwiftUI/Text/DateStyle/timer), the system automatically updates the [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) view while in Always On.

Additionally, any controls in the user interface remain interactive. Users can tap buttons, toggle switches, or select items from a list. When the user interacts with a control, the system runs the associated action and transitions your app back to the active state.

> **Note**: Always On isn’t available on Apple Watch SE or Apple Watch Series 4 and earlier. For these devices, the screen turns off when the app transitions to the background or inactive states.

Apps compiled for watchOS 8 and later have Always On enabled by default. You can disable this feature by setting the [`WKSupportsAlwaysOnDisplay`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKSupportsAlwaysOnDisplay) key to [`false`](https://developer.apple.com/documentation/swift/false) in the WatchKit Extension’s `Info.plist` file. Users can also disable Always On for the entire device or on a per-app basis by choosing Settings > Display & Brightness > Always On.

##### Understand Frontmost App Behavior

By default, when the user lowers their wrist or stops interacting with their watch, your app transitions to the inactive state. The system continues to display your app’s user interface as long as your app remains the frontmost app (usually two minutes) before transitioning to the background and becoming suspended. If the user dismisses the app (for example, by pressing the Digital Crown or by covering the screen), the app transitions immediately to the background and doesn’t become the frontmost app.

Users can set the amount of time that apps remain the frontmost app by changing the settings at Settings > General > Wake Screen > Return to Clock. They can also specify a custom time for individual apps from the Wake Screen. In watchOS 8 and later, apps can remain in the frontmost app state for a maximum of 1 hour.

When the app is inactive, the user interface doesn’t update by default. However, you can use a [`TimelineView`](https://developer.apple.com/documentation/SwiftUI/TimelineView) to schedule periodic updates. For more information, see [`Updating watchOS apps with timelines`](updating-watchos-apps-with-timelines.md).

##### Update the Display During Background Sessions

Apps running a background session, such as a workout session or background audio session, remain onscreen as long as the session is active. Unlike frontmost apps, apps running a background session can continue to update their user interface; however, to save battery life, the system reduces the update frequency.

For the best user experience when the app transitions to the background, pause any animation and show the final state (or a good static image), and remove any subsecond updates. For example, when the workout app is running in the foreground, the duration shows hundredths of a second, and the BPM row shows an animated heart beat. When it transitions to the background, the app displays a static heart image and the duration only shows time to the nearest second.

For animation or updates driven by a [`TimelineView`](https://developer.apple.com/documentation/SwiftUI/TimelineView), check the view’s cadence and update the appearance to match. For more information on timelines, see [`Updating watchOS apps with timelines`](updating-watchos-apps-with-timelines.md).

```swift
TimelineView(PeriodicTimelineSchedule(from: Date(), by: 1.0/60.0)) { context in
    switch context.cadence {
    case .live:
        // Display up to 60 updates per second.
    case .seconds:
        // Only show items that update approximately once per second.
    case .minutes:
        // Only show items that update approximately once per minute.
    @unknown default:
       fatalError("*** Received an unknown cadence: \(context.cadence) ***")
    }
}
```

For other views, monitor the app’s [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment variable, and hide or stop subsecond updates when it becomes [`ScenePhase.inactive`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/inactive) or [`ScenePhase.background`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/background).

```swift
@Environment(\.scenePhase) private var scenePhase

var body: some View {
    if scenePhase == .active {
        // Animation and subsecond updates here.
    } else {
        // Low-frequency updates here.
    }
}
```

##### Hide Sensitive Information

Because displayed information may be visible to casual observers, be sure to hide any sensitive data while your app is in Always On. Add the [`privacySensitive(_:)`](https://developer.apple.com/documentation/SwiftUI/View/privacySensitive(_:)) view modifier to blur out specific user interface elements during Always On.

```swift
Text("Account Number:")
    .font(.headline)
Text(accountNumber)
    .privacySensitive()
```

Or access the [`redactionReasons`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/redactionReasons) environment variable.

```swift
@Environment(\.redactionReasons) var redactionReasons
```

Check if this variable contains the [`privacy`](https://developer.apple.com/documentation/SwiftUI/RedactionReasons/privacy) value. If it does, eliminate or obscure any sensitive data.

```swift
if !redactionReasons.contains(.privacy) {
    Text("Balance:")
        .font(.headline)
    Text(balance)
}
```

The resulting user interface displays the private data while the app is running in the foreground.

![A foreground watchOS app showing the user’s name, account number, and balance.](https://docs-assets.developer.apple.com/published/cae695c8e57f164a8eaf6823deb31092/designing-your-app-for-the-always-on-state-1%402x.png)

But the interface obscures sensitive data, such as the account number and balance, when the app is in the Always On state.

![A watchOS app in Always On, with the account number obscured and the balance removed.](https://docs-assets.developer.apple.com/published/75e8f4d37a5c71aa03b288c6927a8dc5/designing-your-app-for-the-always-on-state-2%402x.png)

To protect the user’s privacy, always hide any highly sensitive information, such as financial information or health data. For information that may or may not be sensitive, such as incoming messages or appointments, default to showing the information. If the user has any concerns, they can disable Always On on a per-app basis.

##### Customize the Reduced Luminance Appearance

To preserve battery life, the system dims the screen during Always On. The system determines the screen’s overall luminance by comparing the ratio of lit pixels to dark pixels. It then reduces the overall brightness to an appropriate level.

Many system controls also automatically update their appearance during Always On. For example, the [`List`](https://developer.apple.com/documentation/SwiftUI/List) view automatically dims the background for the [`CarouselListStyle`](https://developer.apple.com/documentation/SwiftUI/CarouselListStyle).

Many apps can use the system’s default Always On appearance. For example, if your view is mostly black and uses system controls, you may not need to change anything. However, you can customize the appearance during Always On to highlight glanceable, important information in your user interface.

For example, you may consider replacing large blocks of bright content with stroked outlines and dimmed interiors, as shown on the Numerals Duo watch face.

![The Numerals Duo watch face in Always On, showing strong outlines and dimmed fills for the large numbers.](https://docs-assets.developer.apple.com/published/fb0e5a0dcb82d33d5868cccc258298b6/designing-your-app-for-the-always-on-state-3%402x.png)

You can also dim or remove nonessential information. To customize your interface, use the [`isLuminanceReduced`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/isLuminanceReduced) environment variable.

```swift
@Environment(\.isLuminanceReduced) var isLuminanceReduced
```

You can then use this value to modify your user interface, as needed.

```swift
Text("Hello!")
    .font(.title)
    .fontWeight(.bold)
    .opacity(isLuminanceReduced ? 0.5 : 1.0)
```

The resulting interface displays the title text at full brightness when active.

![A watchOS app running in the foreground. It shows a large, white title, status text, and a button.](https://docs-assets.developer.apple.com/published/1c499385710a6262baf912402d45c286/designing-your-app-for-the-always-on-state-4%402x.png)

Then it dims the title in Always On. Because the ratio of lit to dark pixels is low, the system doesn’t need to make any other changes to the view.

![A watchOS app running in Always On. The app dims the title, but the appearance of the status text and button don’t changed.](https://docs-assets.developer.apple.com/published/a35de826853db88aca3c819f9ef5b4fb/designing-your-app-for-the-always-on-state-5%402x.png)

##### Preview Both Interfaces in Xcode

You can preview both the regular and Always On interfaces in Xcode. To see the Always On interface, set the [`isLuminanceReduced`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/isLuminanceReduced) and [`redactionReasons`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/redactionReasons) environment variables in the preview.

```swift
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            ContentView()
            ContentView()
                .environment(\.isLuminanceReduced, true)
                .environment(\.redactionReasons, [.privacy])
        }
    }
}
```

The resulting preview shows both the regular and the Always On interfaces.

![The regular and Always On previews in Xcode’s canvas.](https://docs-assets.developer.apple.com/published/f1eb718ab4fcd800ebc884ca2c913af9/designing-your-app-for-the-always-on-state-6%402x.png)

> **Note**: The system doesn’t automatically dim the user interface when previewing in Xcode. To see how the system automatically dims the user interface, you must test it on a device or in the simulator.

##### Test Always on in the Simulator

Xcode supports Always On in the simulator. Simply click the Toggle Always On button in the status bar to test.

![A screenshot of a 44 mm watch face in the Xcode simulator. The Toggle Always On button is highlighted in the tool bar above the image of the watch face.](https://docs-assets.developer.apple.com/published/45acf539e733ef9462c45fe47b89cb3c/designing-your-app-for-the-always-on-state-7%402x.png)

You can view any changes to your user interface related to privacy, reduced luminance, or transitioning to an inactive state.

## See Also

- [WKSupportsAlwaysOnDisplay](../BundleResources/Information-Property-List/WKSupportsAlwaysOnDisplay.md)
  A Boolean value that determines whether the system displays the app in the Always On state.
- [Building a productivity app for Apple Watch](building-a-productivity-app-for-apple-watch.md)
  Create a watch app to manage and share a task list and visualize the status with a chart.
- [Supporting multiple watch sizes](supporting-multiple-watch-sizes.md)
  Customize the layout of your user interface to support all Apple Watch sizes.
- [Setting the app’s accent color](setting-the-app-s-accent-color.md)
  Set your app’s accent color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state)*
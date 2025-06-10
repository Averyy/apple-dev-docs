# Updating watchOS apps with timelines

**Framework**: watchOS apps

Seamlessly schedule updates to your user interface, even while it’s inactive.

#### Overview

When you schedule periodic updates to your user interface with [`TimelineView`](https://developer.apple.com/documentation/SwiftUI/TimelineView), updates continue to run even when your app is in the [`ScenePhase.background`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/background) or [`ScenePhase.inactive`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/inactive) state, making this an ideal choice for keeping a watchOS app up-to-date while in the Always On state. Additionally, you can use a `TimelineView` to drive other changes — such as animation — when your app is running in the foreground.

##### Set Up the Timeline

Specify the part of your user interface that receives periodic updates using a `TimelineView`.

```swift
var body: some View {
    VStack {

        // Use a timeline to recalculate the value every minute.
        `TimelineView`(EveryMinuteTimelineSchedule()) { context in
            // Display the current amount of caffeine in the user's body.
            Text(coffeeData.mgCaffeineString(atDate: context.date) + " mg")
                .font(.body)
                .fontWeight(.bold)
                .foregroundColor(colorForCaffeineDose())
        }

        // Lay out static views here.
        Text("Current Caffeine Dose")
            .font(.footnote)

        Divider()
        ...
}
```

The `TimelineView` structure takes a schedule that determines when the system makes updates. It also takes a [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) that defines the updatable content. The system then calls the view builder, passing the context for each update.

The [`TimelineView.Context`](https://developer.apple.com/documentation/SwiftUI/TimelineView/Context) instance contains both the time and the current [`TimelineView.Context.Cadence`](https://developer.apple.com/documentation/SwiftUI/TimelineView/Context/Cadence-swift.enum) for the updates. When creating the updatable content for the `TimelineView`, use the time from the context, not the current system time. When in Always On, the system may request views up to 5 minutes in the future.

The cadence also indicates the current maximum rate for updates that the `TimelineView` receives:

The cadence can change from update to update. Always check the current value and hide information that isn’t relevant. For example, a timer app may show the time remaining in minutes, seconds, and hundredths of a second when it receives updates at the `TimelineView.Context.Cadence.live` frequency. It can also play animation at that frequency.

When the updates drop to the `TimelineView.Context.Cadence.seconds` frequency, the app hides the hundredths of seconds and swaps the animation for a static image. The countdown only shows minutes and seconds.

If the frequency drops to `TimelineView.Context.Cadence.minutes`, the app also hides the seconds and only shows the time remaining to the nearest minute.

##### Specify the Schedule

When you create a `TimelineView`, you must specify the update schedule, which is an instance that adopts the [`TimelineSchedule`](https://developer.apple.com/documentation/SwiftUI/TimelineSchedule) protocol. While you can create your own custom schedules, SwiftUI provides schedules for many common use cases.

The system attempts to trigger updates based on the schedule, but it can delay or defer an update based on the system’s current state. Additionally, if the schedule is more frequent than the current cadence, the system throttles the updates to the cadence.

Common schedules include:

##### Update During Always on

You can use timeline views to update your watchOS app while it’s in the Always On state; however, you must be able to specify the view’s contents given a `Date` instance for a time in the future. To improve performance, the system may ask for views up to 5 minutes in the future. For example, an egg timer could use a `TimelineView` to display the time remaining during Always On because it can calculate the amount of time remaining given any arbitrary time in the future.

When your app is active and in the foreground, the timeline schedule runs in the [`TimelineScheduleMode.normal`](https://developer.apple.com/documentation/SwiftUI/TimelineScheduleMode/normal) mode, and your `TimelineView` can receive updates at the `TimelineView.Context.Cadence.live` cadence. When your app transitions into Always On, the timeline schedule also transitions into the [`TimelineScheduleMode.lowFrequency`](https://developer.apple.com/documentation/SwiftUI/TimelineScheduleMode/lowFrequency) mode, the cadence generally drops, and the system may batch-load future updates.

> **Note**: In the Always On state, apps running a background session may not need to use a `TimelineView` to update their user interface. Any changes the app makes while running in the background continue to update its interface; however, to preserve battery life, the system only refreshes the user interface about once per second. For more information, see [`Designing your app for the Always On state`](designing-your-app-for-the-always-on-state.md).

While the actual cadence can vary depending on the requested schedule and the current state of the system, apps generally receive an update frequency based on whether they have background runtime or are inactive, frontmost apps.

Apps with background runtime receive updates at the `TimelineView.Context.Cadence.seconds` frequency. This would include apps with an active background session (like workout or background audio apps) or apps executing a background refresh task.

Inactive apps receive updates as long as they remain in the frontmost state, generally at the `TimelineView.Context.Cadence.minutes` frequency. However, if you request a short burst of updates at the `TimelineView.Context.Cadence.seconds` frequency, the system provides that cadence if possible.

For example, an egg timer could use an `ExplicitTimelineSchedule` to set up per-minute updates for most of the countdown, and switch to per-second updates for the last minute. If conditions permit, the system provides `TimelineView.Context.Cadence.seconds` updates for the last minute.

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [Creating independent watchOS apps](creating-independent-watchos-apps.md)
  Set up a watchOS app that installs and runs without a companion iOS app.
- [Keeping your watchOS content up to date](keeping-your-watchos-app-s-content-up-to-date.md)
  Ensure that your app’s content is relevant and up to date.
- [Authenticating users on Apple Watch](authenticating-users-on-apple-watch.md)
  Create an account sign-up and sign-in strategy for your app.
- [Responding to the Action button on Apple Watch Ultra](../AppIntents/ActionButtonArticle.md)
  Use App Intents to register actions for your app.
- [Enabling the double-tap gesture on Apple Watch](enabling-double-tap.md)
  Customize your app’s response to the double-tap gesture on Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/updating-watchos-apps-with-timelines)*
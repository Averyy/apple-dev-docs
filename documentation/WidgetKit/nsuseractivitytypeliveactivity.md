# NSUserActivityTypeLiveActivity

**Framework**: WidgetKit  
**Kind**: var

A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
let NSUserActivityTypeLiveActivity: String
```

#### Discussion

In many cases, you use  [`widgetURL(_:)`](https://developer.apple.com/documentation/SwiftUI/View/widgetURL(_:)) to allow users to tap a Live Activity and open a screen in the app with functionality that best fits the Live Activity. If you don’t use the `widgetURL(_:)` modifier to provide a URL, the system launches your app and passes `NSUserActivityTypeLiveActivity` as the [`activityType`](https://developer.apple.com/documentation/Foundation/NSUserActivity/activityType) of [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) upon launch. Check for this value on launch to open a screen in your app that fits the context of the active Live Activity.

## See Also

- [Displaying live data with Live Activities](../ActivityKit/displaying-live-data-with-live-activities.md)
  Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [ActivityKit](../ActivityKit/ActivityKit.md)
  Share live updates from your app as Live Activities on iPhone, iPad, Apple Watch, and the Mac.
- [Creating a widget extension](creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [struct ActivityConfiguration](activityconfiguration.md)
  An object that describes the content of a Live Activity.
- [struct DynamicIsland](dynamicisland.md)
  The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [enum ActivityPreviewViewKind](activitypreviewviewkind.md)
  Values that represent Live Activity presentations for use in Xcode previews.
- [enum ActivityFamily](activityfamily.md)
  A family that defines the Live Activity’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/nsuseractivitytypeliveactivity)*
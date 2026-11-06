# Live Activities

**Framework**: WidgetKit  
**Role**: API Collection

Let people track updates from your app with Live Activities.

## Overview

Live Activities display up-to-date content from your app, such as event and task information on the Lock Screen or in the Dynamic Island. Additionally, Live Activities appear in CarPlay, on a paired Apple Watch, and in the menu bar of a Mac. A Mac mirrors Live Activities from a nearby iPhone, and Mac apps can also create them directly. To create Live Activities, you use WidgetKit together with [ActivityKit](../ActivityKit/ActivityKit.md).

## Topics

### Essentials
- [Developing a WidgetKit strategy](./developing-a-widgetkit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [Creating a widget extension](./creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
### Live Activity setup
- [Displaying live data with Live Activities](../ActivityKit/displaying-live-data-with-live-activities.md)
  Display up-to-date data and offer quick interactions in highly visible places like the Dynamic Island, the menu bar, a paired Apple Watch, or in CarPlay.
- [ActivityKit](../ActivityKit/ActivityKit.md)
  Share live updates from your app as Live Activities that appear in the Dynamic Island and other highly visible locations.
- [Creating a widget extension](./creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](./emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [struct ActivityConfiguration](./activityconfiguration.md)
  An object that describes the content of a Live Activity.
- [struct DynamicIsland](./dynamicisland.md)
  The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [let NSUserActivityTypeLiveActivity: String](./nsuseractivitytypeliveactivity.md)
  A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [enum ActivityPreviewViewKind](./activitypreviewviewkind.md)
  Values that represent Live Activity presentations for use in Xcode previews.
- [enum ActivityFamily](./activityfamily.md)
  A family that defines the Live Activity’s size.

## See Also

### System experiences
- [Widgets and watch complications](./widgets-and-complications-collection.md)
  Allow people to personalize their devices, view relevant information, and perform interactions with widgets and watch complications.
- [Controls](./controls-collection.md)
  Offer controls that people place in Control Center, on the Lock Screen, and on the Action button to quickly perform an action from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/liveactivities-collection)*
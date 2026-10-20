# ActivityConfiguration

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

An object that describes the content of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
@MainActor
@preconcurrency struct ActivityConfiguration<Attributes> where Attributes : ActivityAttributes
```

## Mentions

- [Creating a widget extension](./creating-a-widget-extension.md)

#### Overview

To learn more about offering Live Activities for your app, see [ActivityKit](../ActivityKit/ActivityKit.md).

## Topics

### Creating a Live Activity configuration
- [struct ActivityViewContext](./activityviewcontext.md)
  A structure that describes the view context for creating the views of a Live Activity.
- [init<Content>(for: Attributes.Type, content: (ActivityViewContext<Attributes>) -> Content, dynamicIsland: (ActivityViewContext<Attributes>) -> DynamicIsland)](./activityconfiguration/init%28for,content,dynamicisland%29.md)
  Creates a configuration object for a Live Activity.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [WidgetConfiguration](../SwiftUI/widgetconfiguration.md)

## See Also

### Live Activity setup
- [Displaying live data with Live Activities](../ActivityKit/displaying-live-data-with-live-activities.md)
  Display up-to-date data and offer quick interactions in the Dynamic Island, on the Lock Screen, in CarPlay, and on a paired Mac or Apple Watch.
- [ActivityKit](../ActivityKit/ActivityKit.md)
  Share live updates from your app as Live Activities on iPhone, iPad, Apple Watch, and the Mac.
- [Creating a widget extension](./creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](./emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [struct DynamicIsland](./dynamicisland.md)
  The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [let NSUserActivityTypeLiveActivity: String](./nsuseractivitytypeliveactivity.md)
  A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [enum ActivityPreviewViewKind](./activitypreviewviewkind.md)
  Values that represent Live Activity presentations for use in Xcode previews.
- [enum ActivityFamily](./activityfamily.md)
  A family that defines the Live Activity’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/activityconfiguration)*
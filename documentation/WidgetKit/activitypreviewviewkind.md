# ActivityPreviewViewKind

**Framework**: WidgetKit  
**Kind**: enum

Values that represent Live Activity presentations for use in Xcode previews.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
@preconcurrency
enum ActivityPreviewViewKind
```

## Topics

### Live Activity preview types
- [ActivityPreviewViewKind.content](activitypreviewviewkind/content.md)
  The Live Activity presentation that appears on the Lock Screen and as a banner on devices that don’t support the Dynamic Island.
- [case dynamicIsland(ActivityPreviewViewKind.DynamicIslandPreviewViewState)](activitypreviewviewkind/dynamicisland(_:).md)
  The Live Activity presentation that appears in the Dynamic Island.
- [ActivityPreviewViewKind.DynamicIslandPreviewViewState](activitypreviewviewkind/dynamicislandpreviewviewstate.md)
  Values that represent the different presentations of a Live Activity in the Dynamic Island for use in Xcode previews.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [let NSUserActivityTypeLiveActivity: String](nsuseractivitytypeliveactivity.md)
  A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [enum ActivityFamily](activityfamily.md)
  A family that defines the Live Activity’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/activitypreviewviewkind)*
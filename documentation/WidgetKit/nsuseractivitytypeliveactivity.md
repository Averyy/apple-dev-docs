# NSUserActivityTypeLiveActivity

**Framework**: Widgetkit  
**Kind**: var

A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
let NSUserActivityTypeLiveActivity: String
```

#### Discussion

In many cases, you use  [`widgetURL(_:)`](https://developer.apple.com/documentation/SwiftUI/View/widgetURL(_:)) to allow users to tap a Live Activity and open a screen in the app with functionality that best fits the Live Activity. If you don’t use the `widgetURL(_:)` modifier to provide a URL, the system launches your app and passes `NSUserActivityTypeLiveActivity` as the [`activityType`](https://developer.apple.com/documentation/foundation/nsuseractivity/1409611-activitytype) of [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) upon launch. Check for this value on launch to open a screen in your app that fits the context of the active Live Activity.

## See Also

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
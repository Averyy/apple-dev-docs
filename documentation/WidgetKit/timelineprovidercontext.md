# TimelineProviderContext

**Framework**: WidgetKit  
**Kind**: struct

An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
struct TimelineProviderContext
```

#### Overview

When requesting timelines for a widget, WidgetKit passes the [`TimelineProvider`](timelineprovider.md) a context object that includes details about how the widget appears. These details include:

- The [`WidgetFamily`](widgetfamily.md); for example, [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) and  [`WidgetFamily.systemMedium`](widgetfamily/systemmedium.md).
- The size, in points, of the widget.
- Variants of the environments where the widget might appear.
- Whether the widget appears as a preview in the widget gallery.

If your widget uses assets that take time to generate or depend on the specific environment they’re rendered in, you can use the environment variants to generate those assets in advance. Some of the common environment properties to consider include:

- [`colorScheme`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/colorScheme), where you use different assets for light and dark schemes.
- [`displayScale`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/displayScale), where your widget might appear in both @1x and @2x displays on macOS devices.

To be responsive when the environment changes, WidgetKit may render the widget’s view in advance. For example, WidgetKit renders both light and dark versions of the widget so that if the color scheme changes, the correct version is immediately available.

## Topics

### Preparing Preview Content
- [let isPreview: Bool](timelineprovidercontext/ispreview.md)
  A Boolean value that indicates when the widget appears in the widget gallery.
### Accessing Size Attributes
- [let family: WidgetFamily](timelineprovidercontext/family.md)
  The user-configured family of the widget: small, medium, or large.
- [let displaySize: CGSize](timelineprovidercontext/displaysize.md)
  The size, in points, of the widget.
### Accessing Environment Variations
- [let environmentVariants: TimelineProviderContext.EnvironmentVariants](timelineprovidercontext/environmentvariants-swift.property.md)
  All environment values that might be set when a widget appears.
- [TimelineProviderContext.EnvironmentVariants](timelineprovidercontext/environmentvariants-swift.struct.md)
  A structure containing all varieties of environments where a widget could appear.

## See Also

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md)
  Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [protocol TimelineProvider](timelineprovider.md)
  A type that advises WidgetKit when to update a widget’s display.
- [protocol AppIntentTimelineProvider](appintenttimelineprovider.md)
  A type that advises WidgetKit when to update a user-configurable widget’s display.
- [protocol IntentTimelineProvider](intenttimelineprovider.md)
  A type that advises WidgetKit when to update a user-configurable widget’s display.
- [protocol TimelineEntry](timelineentry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [struct Timeline](timeline.md)
  An object that specifies a date for WidgetKit to update a widget’s view.
- [class WidgetCenter](widgetcenter.md)
  An object that contains a list of user-configured widgets and is used for reloading widget timelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovidercontext)*
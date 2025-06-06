# Preview macros

**Framework**: Widgetkit

Use Swift macros to create widget previews in Xcode.

## Topics

### Providing a widget preview
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:widget:timelineprovider:).md)
  Preview a widget with a static configuration, using the specified timeline provider.
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:using:widget:timelineprovider:)-4ljg1.md)
  Preview a widget with an app intent configuration, using the specified timeline provider.
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:using:widget:timelineprovider:)-3df1l.md)
  Preview a widget with an intent configuration, using the specified timeline provider.
- [macro Preview<Widget>(String?, as: WidgetFamily, widget: () -> Widget, timeline: () async -> [any TimelineEntry])](preview(_:as:widget:timeline:).md)
  Preview a timeline-style widget.
### Generating a Live Activity preview
- [macro Preview<Widget, Attributes>(String?, as: ActivityPreviewViewKind, using: Attributes, widget: () -> Widget, contentStates: () async -> [Attributes.ContentState])](preview(_:as:using:widget:contentstates:).md)
  Preview a widget with an activity configuration, using the specified attributes and content states.
### Generated structures
- [struct PreviewActivityBuilder](previewactivitybuilder.md)
- [struct PreviewTimelineBuilder](previewtimelinebuilder.md)

## See Also

- [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md)
  Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [Debugging Widgets](debugging-widgets.md)
  Set environment variables in Xcode to control your widget’s configuration in the debugger.
- [struct WidgetPreviewContext](widgetpreviewcontext.md)
  A specification for the context of a widget preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/preview-macros)*
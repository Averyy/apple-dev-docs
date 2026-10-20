# Preview macros

**Framework**: WidgetKit  
**Role**: API Collection

Use Swift macros to create widget previews in Xcode.

## Topics

### Generating a widget preview
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, widget: () -> Widget, timelineProvider: () -> Provider)](./preview%28_,as,widget,timelineprovider%29.md)
  Preview a widget with a static configuration, using the specified timeline provider.
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> Widget, timelineProvider: () -> Provider)](./preview%28_,as,using,widget,timelineprovider%29-4ljg1.md)
  Preview a widget with an app intent configuration, using the specified timeline provider.
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> Widget, timelineProvider: () -> Provider)](./preview%28_,as,using,widget,timelineprovider%29-3df1l.md)
  Preview a widget with an intent configuration, using the specified timeline provider.
- [macro Preview<Widget>(String?, as: WidgetFamily, widget: () -> Widget, timeline: () async -> [any TimelineEntry])](./preview%28_,as,widget,timeline%29.md)
  Preview a timeline-style widget.
- [macro Preview<Widget, Entry>(String?, widget: () -> Widget, relevanceEntries: () async -> [Entry])](./preview%28_,widget,relevanceentries%29.md)
  Preview a relevance configuration widget.
- [macro Preview<Widget, Provider>(String?, widget: () -> Widget, relevanceProvider: () -> Provider)](./preview%28_,widget,relevanceprovider%29.md)
  Preview a widget with a relevance configuration, using the specified relevance provider.
- [macro Preview<Widget, Provider>(String?, widget: () -> Widget, relevanceProvider: () -> Provider, relevance: () async -> WidgetRelevance<Provider.Configuration>)](./preview%28_,widget,relevanceprovider,relevance%29.md)
  Preview a widget with a relevance configuration, using the specified relevances.
### Generating a Live Activity preview
- [macro Preview<Widget, Attributes>(String?, as: ActivityPreviewViewKind, using: Attributes, widget: () -> Widget, contentStates: () async -> [Attributes.ContentState])](./preview%28_,as,using,widget,contentstates%29.md)
  Preview a widget with an activity configuration, using the specified attributes and content states.
### Generated structures
- [struct PreviewActivityBuilder](./previewactivitybuilder.md)
- [struct PreviewRelevanceEntryBuilder](./previewrelevanceentrybuilder.md)
  A builder that allows you to construct a list of relevance entries to preview your widget.
- [struct PreviewTimelineBuilder](./previewtimelinebuilder.md)

## See Also

### Previews and debugging
- [Previewing widgets and Live Activities in Xcode](./previewing-widgets-and-live-activities-in-xcode.md)
  Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [struct WidgetPreviewContext](./widgetpreviewcontext.md)
  A specification for the context of a widget preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/preview-macros)*
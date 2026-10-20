# Preview(_:widget:relevanceProvider:)

**Framework**: WidgetKit  
**Kind**: macro  
**Role**: Macro

Preview a widget with a relevance configuration, using the specified relevance provider.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview<Widget, Provider>(_ name: String? = nil, widget: @escaping @MainActor () -> Widget, relevanceProvider: @escaping @MainActor () -> Provider) where Widget : Widget, Provider : RelevanceEntriesProvider
```

#### Overview

Use sample data for your relevance provider and use it to step through the entries in the Xcode proview canvas.

> **Note**: The relevance provider must be of the type that the widget expects.

## Parameters

- `name`: An optional display name for the preview that appears in the Xcode preview canvas.
- `widget`: A closure producing the widget to be previewed.
- `relevanceProvider`: A closure producing the relevance provider that generates the preview’s relevances and entries.

## See Also

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
- [macro Preview<Widget, Provider>(String?, widget: () -> Widget, relevanceProvider: () -> Provider, relevance: () async -> WidgetRelevance<Provider.Configuration>)](./preview%28_,widget,relevanceprovider,relevance%29.md)
  Preview a widget with a relevance configuration, using the specified relevances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/preview(_:widget:relevanceprovider:))*
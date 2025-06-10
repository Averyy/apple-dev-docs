# RelevanceEntriesProvider

**Framework**: WidgetKit  
**Kind**: protocol

A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.

**Availability**:
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol RelevanceEntriesProvider
```

## Mentions

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)

## Topics

### Generating relevance entries
- [func entry(configuration: Self.Configuration, context: Self.Context) async throws -> Self.Entry](relevanceentriesprovider/entry(configuration:context:).md)
  Provides the entry used to render a widget for a specific relevance configuration.
- [func relevance() async -> WidgetRelevance<Self.Configuration>](relevanceentriesprovider/relevance.md)
  Provides a collection of conditions under which a specific widget could be relevant.
- [func placeholder(context: Self.Context) -> Self.Entry](relevanceentriesprovider/placeholder(context:).md)
  Provides the entry representing a placeholder version of the widget.
- [struct RelevanceEntriesProviderContext](relevanceentriesprovidercontext.md)
  An object that contains details about how a widget is rendered, including its size.
### Associated Types
- [associatedtype Configuration : WidgetConfigurationIntent](relevanceentriesprovider/configuration.md)
  The type of configuration associated with a specific relevance.
- [associatedtype Entry : RelevanceEntry](relevanceentriesprovider/entry.md)
  A type that specifies the information to render a widget at a specific relevance configuration.
### Type Aliases
- [RelevanceEntriesProvider.Context](relevanceentriesprovider/context.md)
  An object that contains details about how a widget is rendered.

## See Also

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
  Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [struct TimelineEntryRelevance](timelineentryrelevance.md)
  An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [struct RelevanceConfiguration](relevanceconfiguration.md)
  A type that describes the content of a widget that uses relevance clues.
- [protocol RelevanceEntry](relevanceentry.md)
  A type that specifies the information to render a widget at a specific relevance configuration.
- [struct WidgetRelevance](widgetrelevance.md)
  A type collecting the relevances for a widget kind.
- [struct WidgetRelevanceAttribute](widgetrelevanceattribute.md)
  A type describing when a specific widget could be relevant.
- [struct WidgetRelevanceGroup](widgetrelevancegroup.md)
  A type for configuring widget behavior in the watchOS Smart Stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/relevanceentriesprovider)*
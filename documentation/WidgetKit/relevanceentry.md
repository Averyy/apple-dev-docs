# RelevanceEntry

**Framework**: WidgetKit  
**Kind**: protocol

A type that specifies the information to render a widget at a specific relevance configuration.

**Availability**:
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol RelevanceEntry : Sendable
```

## Mentions

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
  Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [struct TimelineEntryRelevance](timelineentryrelevance.md)
  An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [struct RelevanceConfiguration](relevanceconfiguration.md)
  A type that describes the content of a widget that uses relevance clues.
- [protocol RelevanceEntriesProvider](relevanceentriesprovider.md)
  A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [struct WidgetRelevance](widgetrelevance.md)
  A type collecting the relevances for a widget kind.
- [struct WidgetRelevanceAttribute](widgetrelevanceattribute.md)
  A type describing when a specific widget could be relevant.
- [struct WidgetRelevanceGroup](widgetrelevancegroup.md)
  A type for configuring widget behavior in the watchOS Smart Stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/relevanceentry)*
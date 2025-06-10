# WidgetRelevance

**Framework**: WidgetKit  
**Kind**: struct

A type collecting the relevances for a widget kind.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 26.0+ (Beta)
- watchOS 11.0+

## Declaration

```swift
struct WidgetRelevance<Configuration>
```

#### Overview

Return this type from the `relevance()` requirement of your [`TimelineProvider`](timelineprovider.md), [`AppIntentTimelineProvider`](appintenttimelineprovider.md), or [`IntentTimelineProvider`](intenttimelineprovider.md) to inform the system of when a widget might be relevant and in which configuration.

Make sure to return the relevances ordered by priority because the system might decide to utilize only a subset of the provided relevances.

## Topics

### Initializers
- [init([WidgetRelevanceAttribute<Configuration>])](widgetrelevance/init(_:).md)
  Creates a type collecting the relevances for a widget kind.

## See Also

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
  Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [struct TimelineEntryRelevance](timelineentryrelevance.md)
  An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [struct RelevanceConfiguration](relevanceconfiguration.md)
  A type that describes the content of a widget that uses relevance clues.
- [protocol RelevanceEntriesProvider](relevanceentriesprovider.md)
  A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [protocol RelevanceEntry](relevanceentry.md)
  A type that specifies the information to render a widget at a specific relevance configuration.
- [struct WidgetRelevanceAttribute](widgetrelevanceattribute.md)
  A type describing when a specific widget could be relevant.
- [struct WidgetRelevanceGroup](widgetrelevancegroup.md)
  A type for configuring widget behavior in the watchOS Smart Stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrelevance)*
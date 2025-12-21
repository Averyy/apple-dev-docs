# RelevanceConfiguration

**Framework**: WidgetKit  
**Kind**: struct

A type that describes the content of a widget that uses relevance clues.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct RelevanceConfiguration<Content> where Content : View
```

## Mentions

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
- [Creating a widget extension](creating-a-widget-extension.md)

#### Overview

In watchOS, widgets can provide the system with relevance clues to indicate that the widget is relevant to a person and should appear prominently in the Smart Stack. To provide relevance clues to watchOS, use `RelevanceConfiguration` or implement the `relevance()` requirement in your timeline provider.

For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](widget-suggestions-in-smart-stacks.md).

## Topics

### Creating a relevance configuration
- [init<Provider>(kind: String, provider: Provider, content: (Provider.Entry) -> Content)](relevanceconfiguration/init(kind:provider:content:).md)
  Creates a configuration for a widget that provides relevance clues to the system.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [WidgetConfiguration](../SwiftUI/WidgetConfiguration.md)

## See Also

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
  Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [struct TimelineEntryRelevance](timelineentryrelevance.md)
  An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [protocol RelevanceEntriesProvider](relevanceentriesprovider.md)
  A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [protocol RelevanceEntry](relevanceentry.md)
  A type that specifies the information to render a widget at a specific relevance configuration.
- [struct WidgetRelevance](widgetrelevance.md)
  A type collecting the relevances for a widget kind.
- [struct WidgetRelevanceAttribute](widgetrelevanceattribute.md)
  A type that describes when a specific widget could be relevant.
- [struct WidgetRelevanceGroup](widgetrelevancegroup.md)
  A type for configuring widget behavior in the watchOS Smart Stack.
- [struct AppIntentRecommendation](appintentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.
- [struct IntentConfiguration](intentconfiguration.md)
  An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [struct IntentRecommendation](intentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/relevanceconfiguration)*
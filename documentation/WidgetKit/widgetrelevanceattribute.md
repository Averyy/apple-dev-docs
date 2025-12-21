# WidgetRelevanceAttribute

**Framework**: WidgetKit  
**Kind**: struct

A type that describes when a specific widget could be relevant.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 26.0+
- watchOS 11.0+

## Declaration

```swift
struct WidgetRelevanceAttribute<Configuration>
```

#### Overview

Use the relevance attribute’s `RelevantContext` to describe when a specific widget might be relevant.

## Topics

### Initializers
- [init(configuration: Configuration, context: RelevantContext)](widgetrelevanceattribute/init(configuration:context:)-8325r.md)
  Creates a new widget relevance for a specific configuration that is relevant in a specific context.
- [init(configuration: Configuration, context: RelevantContext)](widgetrelevanceattribute/init(configuration:context:)-8jxhs.md)
  Creates a new widget relevance for a specific configuration that is relevant in a specific context.
- [init(configuration: Configuration, group: WidgetRelevanceGroup)](widgetrelevanceattribute/init(configuration:group:)-5yh17.md)
  Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.
- [init(configuration: Configuration, group: WidgetRelevanceGroup)](widgetrelevanceattribute/init(configuration:group:)-93jm5.md)
  Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.
- [init(context: RelevantContext)](widgetrelevanceattribute/init(context:).md)
  Creates a new widget relevance that is relevant in a specific context.
- [init(group: WidgetRelevanceGroup)](widgetrelevanceattribute/init(group:).md)
  Associates the widget kind with a group. When multiple widgets are in the same group, the system only suggests one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.

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
- [struct WidgetRelevance](widgetrelevance.md)
  A type collecting the relevances for a widget kind.
- [struct WidgetRelevanceGroup](widgetrelevancegroup.md)
  A type for configuring widget behavior in the watchOS Smart Stack.
- [struct AppIntentRecommendation](appintentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.
- [struct IntentConfiguration](intentconfiguration.md)
  An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [struct IntentRecommendation](intentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrelevanceattribute)*
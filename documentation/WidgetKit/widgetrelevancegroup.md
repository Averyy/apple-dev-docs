# WidgetRelevanceGroup

**Framework**: WidgetKit  
**Kind**: struct

A type for configuring widget behavior in the watchOS Smart Stack.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 26.0+ (Beta)
- watchOS 11.0+

## Declaration

```swift
struct WidgetRelevanceGroup
```

#### Overview

Use `WidgetRelevanceGroup` alongside [`WidgetRelevanceAttribute`](widgetrelevanceattribute.md) to tell the system how it should group your widgets in the watchOS Smart Stack. The system may provide a default grouping mechanism for widgets in the Smart Stack; for example, per-app grouping. Creating a relevance group and choosing the `.ungrouped` option opts out of default grouping behavior. For additional information about widgets in Smart Stacks, refer to [`Increasing the visibility of widgets in Smart Stacks`](widget-suggestions-in-smart-stacks.md).

## Topics

### Type Properties
- [static let automatic: WidgetRelevanceGroup](widgetrelevancegroup/automatic.md)
  Specifies that the widget group should use the automatic grouping behavior provided the system.
- [static let ungrouped: WidgetRelevanceGroup](widgetrelevancegroup/ungrouped.md)
  Don’t use the system’s default behavior for grouping widgets.
### Type Methods
- [static func named(String) -> WidgetRelevanceGroup](widgetrelevancegroup/named(_:).md)
  Creates a group with the provided name.

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
- [struct WidgetRelevanceAttribute](widgetrelevanceattribute.md)
  A type describing when a specific widget could be relevant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrelevancegroup)*
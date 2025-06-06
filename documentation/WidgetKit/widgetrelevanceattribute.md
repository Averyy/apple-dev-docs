# WidgetRelevanceAttribute

**Framework**: Widgetkit  
**Kind**: struct

A type describing when a specific widget could be relevant.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
struct WidgetRelevanceAttribute<Configuration>
```

#### Overview

You use `RelevantContext` as way to describe when a specific widget can be relevant.

## Topics

### Initializers
- [init(configuration: Configuration, context: RelevantContext)](widgetrelevanceattribute/init(configuration:context:)-4nd5m.md)
  Creates a new widget relevance for a specific configuration that is relevant in a specific context.
- [init(configuration: Configuration, context: RelevantContext)](widgetrelevanceattribute/init(configuration:context:)-8b5x2.md)
  Creates a new widget relevance for a specific configuration that is relevant in a specific context.
- [init(configuration: Configuration, group: WidgetRelevanceGroup)](widgetrelevanceattribute/init(configuration:group:)-5yh17.md)
  Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.
- [init(configuration: Configuration, group: WidgetRelevanceGroup)](widgetrelevanceattribute/init(configuration:group:)-93jm5.md)
  Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.
- [init(context: RelevantContext)](widgetrelevanceattribute/init(context:).md)
  Creates a new widget relevance that is relevant in a specific context.
- [init(group: WidgetRelevanceGroup)](widgetrelevanceattribute/init(group:).md)
  Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrelevanceattribute)*
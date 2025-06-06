# WidgetRelevanceGroup

**Framework**: Widgetkit  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
struct WidgetRelevanceGroup
```

## Topics

### Type Properties
- [static let automatic: WidgetRelevanceGroup](widgetrelevancegroup/automatic.md)
  Specifies that the widget should use the automatic grouping behavior provided the system.
- [static let ungrouped: WidgetRelevanceGroup](widgetrelevancegroup/ungrouped.md)
  The system may provide a default grouping mechanism, such as per-app grouping, by default.Utilizing the `.ungrouped` option opts out of the default group.
### Type Methods
- [static func named(String) -> WidgetRelevanceGroup](widgetrelevancegroup/named(_:).md)
  Creates a group with the provided name. Widgets in the same group will not be suggested by the system simultaneously in contexts where both are visible. Named groups are namespaced to the containing app, and won’t be impacted by other apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrelevancegroup)*
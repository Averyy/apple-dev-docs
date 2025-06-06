# TimelineReloadPolicy

**Framework**: Widgetkit  
**Kind**: struct

A type that indicates the earliest date WidgetKit requests a new timeline from the widget’s provider.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
struct TimelineReloadPolicy
```

## Topics

### Reload Policies
- [static let atEnd: TimelineReloadPolicy](timelinereloadpolicy/atend.md)
  A policy that specifies that WidgetKit requests a new timeline after the last date in a timeline passes.
- [static func after(Date) -> TimelineReloadPolicy](timelinereloadpolicy/after(_:).md)
  A policy that specifies a future date for WidgetKit to request a new timeline.
- [static let never: TimelineReloadPolicy](timelinereloadpolicy/never.md)
  A policy that specifies that the app prompts WidgetKit when a new timeline is available.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [let entries: [EntryType]](timeline/entries.md)
  An array of timeline entries.
- [let policy: TimelineReloadPolicy](timeline/policy.md)
  The policy that determines the earliest date and time WidgetKit requests a new timeline from a timeline provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelinereloadpolicy)*
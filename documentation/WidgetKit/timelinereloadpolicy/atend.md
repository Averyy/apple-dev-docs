# atEnd

**Framework**: Widgetkit  
**Kind**: property

A policy that specifies that WidgetKit requests a new timeline after the last date in a timeline passes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
static let atEnd: TimelineReloadPolicy
```

## See Also

- [static func after(Date) -> TimelineReloadPolicy](timelinereloadpolicy/after(_:).md)
  A policy that specifies a future date for WidgetKit to request a new timeline.
- [static let never: TimelineReloadPolicy](timelinereloadpolicy/never.md)
  A policy that specifies that the app prompts WidgetKit when a new timeline is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelinereloadpolicy/atend)*
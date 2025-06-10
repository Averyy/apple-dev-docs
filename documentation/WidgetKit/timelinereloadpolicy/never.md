# never

**Framework**: WidgetKit  
**Kind**: property

A policy that specifies that the app prompts WidgetKit when a new timeline is available.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
static let never: TimelineReloadPolicy
```

## See Also

- [static let atEnd: TimelineReloadPolicy](timelinereloadpolicy/atend.md)
  A policy that specifies that WidgetKit requests a new timeline after the last date in a timeline passes.
- [static func after(Date) -> TimelineReloadPolicy](timelinereloadpolicy/after(_:).md)
  A policy that specifies a future date for WidgetKit to request a new timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelinereloadpolicy/never)*
# after(_:)

**Framework**: WidgetKit  
**Kind**: method

A policy that specifies a future date for WidgetKit to request a new timeline.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
static func after(_ date: Date) -> TimelineReloadPolicy
```

## Mentions

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md)

## See Also

- [static let atEnd: TimelineReloadPolicy](timelinereloadpolicy/atend.md)
  A policy that specifies that WidgetKit requests a new timeline after the last date in a timeline passes.
- [static let never: TimelineReloadPolicy](timelinereloadpolicy/never.md)
  A policy that specifies that the app prompts WidgetKit when a new timeline is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelinereloadpolicy/after(_:))*
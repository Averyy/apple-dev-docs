# never

**Framework**: WidgetKit  
**Kind**: property  
**Role**: Type Property

A policy that specifies that the app prompts WidgetKit when a new timeline is available.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
static let never: TimelineReloadPolicy
```

## See Also

### Reload Policies
- [static let atEnd: TimelineReloadPolicy](./atend.md)
  A policy that specifies that WidgetKit requests a new timeline after the last date in a timeline passes.
- [static func after(Date) -> TimelineReloadPolicy](./after%28_%29.md)
  A policy that specifies a future date for WidgetKit to request a new timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelinereloadpolicy/never)*
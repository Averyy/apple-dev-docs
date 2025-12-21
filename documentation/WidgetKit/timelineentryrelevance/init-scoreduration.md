# init(score:duration:)

**Framework**: WidgetKit  
**Kind**: init

Creates an object that represents the importance of a widget and the length of time for WidgetKit to consider it for rotation to the top of the stack.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
init(score: Float, duration: TimeInterval = 0.0)
```

## Parameters

- `score`: A value on a scale of your choosing, indicating the   importance of an entry compared to other entries in the same   timeline.
- `duration`: The number of seconds following an entry’s date that   WidgetKit may rotate the widget to the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineentryrelevance/init(score:duration:))*
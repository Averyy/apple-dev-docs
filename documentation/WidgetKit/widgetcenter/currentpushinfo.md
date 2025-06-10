# currentPushInfo

**Framework**: WidgetKit  
**Kind**: property

Provides the current push information for widget reloads and relevance refreshes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var currentPushInfo: WidgetPushInfo? { get async }
```

#### Discussion

May be nil if the token has not completed generation, or if no widgets have been configured for push.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetcenter/currentpushinfo)*
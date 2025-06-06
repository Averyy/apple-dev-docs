# relevance()

**Framework**: Widgetkit  
**Kind**: method  
**Required**: Yes

Provides an object containing attributes that describe when a specific widget could be relevant.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
func relevance() async -> WidgetRelevance<Void>
```

#### Discussion

The system can use the relevance to show this widget when the condition for the relevance matches the current state.

By default, this methods returns no relevances. You can implement this requirement to provide a list of configuration and relevances pair where your widget would become relevant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovider/relevance())*
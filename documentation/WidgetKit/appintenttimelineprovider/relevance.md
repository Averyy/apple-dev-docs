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
func relevance() async -> WidgetRelevance<Self.Intent>
```

#### Discussion

The system can use the relevance to show this widget when the condition for the relevance matches the current state.

By default, this methods returns no relevances. You can implement this requirement to provide a list of configuration and relevances pair where your widget would become relevant.

You can return multiple entries with the same configuration, but having different attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/relevance())*
# relevance()

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Provides an object containing attributes that describe when a specific widget is relevant.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 26.0+ (Beta)
- watchOS 11.0+

## Declaration

```swift
func relevance() async -> WidgetRelevance<Void>
```

## Mentions

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
- [Keeping a widget up to date](keeping-a-widget-up-to-date.md)

#### Return Value

The object that contains attributes that describe when a specific widget is relevant.

#### Discussion

The system can use the relevance to show this widget in the Smart Stack when the provided relevance matches a person’s context. For example, if you indicate relevance at a specific location, the system could show the widget when a person is at or close to the location.

By default, this method returns no relevances. Implement this requirement to tell the system that your widget is relevant.

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](widget-suggestions-in-smart-stacks.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovider/relevance())*
# invalidateRelevance(ofKind:)

**Framework**: WidgetKit  
**Kind**: method

Mark the relevance for a kind as invalid.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 26.0+
- watchOS 11.0+

## Declaration

```swift
func invalidateRelevance(ofKind kind: String)
```

#### Discussion

Call this function when the relevance returned for a widget has changed and needs to be reloaded.

Marking relevance as invalid causes the system to call, at a later time, the `relevance` function on the timeline provider that matches the specified kind.

## Parameters

- `kind`: A string that identifies the widget and matches the   value you used when you created the widget’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetcenter/invalidaterelevance(ofkind:))*
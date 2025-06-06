# init(for:content:dynamicIsland:)

**Framework**: Widgetkit  
**Kind**: init

Creates a configuration object for a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
@MainActor
@preconcurrency init<Content>(for attributesType: Attributes.Type, @ViewBuilder content: @escaping (ActivityViewContext<Attributes>) -> Content, dynamicIsland: @escaping (ActivityViewContext<Attributes>) -> DynamicIsland) where Content : View
```

## Parameters

- `attributesType`: The type that describes the content of the Live Activity.
- `content`: A closure that creates the view for the Live Activity that appears on the Lock Screen.   This view also appears as a banner on the Home Screen of devices that don’t support the   Dynamic Island when you alert a person about updated Live Activity content.
- `dynamicIsland`: A closure that builds the Live Activity that appears in the Dynamic Island.

## See Also

- [struct ActivityViewContext](activityviewcontext.md)
  A structure that describes the view context for creating the views of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/activityconfiguration/init(for:content:dynamicisland:))*
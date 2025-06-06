# ActivityViewContext

**Framework**: Widgetkit  
**Kind**: struct

A structure that describes the view context for creating the views of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct ActivityViewContext<Attributes> where Attributes : ActivityAttributes
```

## Topics

### Describing a Live Activity
- [let attributes: Attributes](activityviewcontext/attributes.md)
  A set of attributes that describe a Live Activity and its content at the time of its creation.
- [let state: Attributes.ContentState](activityviewcontext/state.md)
  The dynamic content of a Live Activity at the time of its creation.
- [let isStale: Bool](activityviewcontext/isstale.md)
  A Boolean value that describes whether the Live Activity is out of date.
- [let activityID: String](activityviewcontext/activityid.md)
  A unique identifier for the Live Activity.

## See Also

- [init<Content>(for: Attributes.Type, content: (ActivityViewContext<Attributes>) -> Content, dynamicIsland: (ActivityViewContext<Attributes>) -> DynamicIsland)](activityconfiguration/init(for:content:dynamicisland:).md)
  Creates a configuration object for a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/activityviewcontext)*
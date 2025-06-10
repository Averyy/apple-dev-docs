# init(group:)

**Framework**: WidgetKit  
**Kind**: init

Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 26.0+ (Beta)
- watchOS 11.0+

## Declaration

```swift
init(group: WidgetRelevanceGroup)
```

#### Discussion

Multiple groups can be associated with the same widget by providing multiple `WidgetRelevanceAttribute` instances with different groups.

## Parameters

- `group`: The group to associate the widget with


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrelevanceattribute/init(group:))*
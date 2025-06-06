# init(intent:description:)

**Framework**: Widgetkit  
**Kind**: init

Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
init<S>(intent: T, description: S) where S : StringProtocol
```

#### Discussion

> **Note**: On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `IntentRecommendation` is inactive.

## Parameters

- `intent`: The intent that represents the recommended   configuration.
- `description`: A description that helps the user   understand the value of the preconfigured configuration option.   For example, if the configuration represents a location in a weather   app, the description may be the name of one of the user’s favorite   cities, such as  .

## See Also

- [init(intent: T, description: LocalizedStringKey)](intentrecommendation/init(intent:description:)-1zh33.md)
  Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets with a localized description.
- [init(intent: T, description: Text)](intentrecommendation/init(intent:description:)-4epo2.md)
  Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intentrecommendation/init(intent:description:)-6v7dj)*
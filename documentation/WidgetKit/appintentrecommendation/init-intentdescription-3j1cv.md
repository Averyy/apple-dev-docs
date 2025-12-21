# init(intent:description:)

**Framework**: WidgetKit  
**Kind**: init

Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets with a localized description.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
init(intent: Intent, description: LocalizedStringResource)
```

#### Discussion

> **Note**: On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `AppIntentRecommendation` is inactive.

## Parameters

- `intent`: The intent that represents the recommended   configuration.
- `description`: A localized string in your bundle   that helps the user understand the value of the preconfigured   configuration option. For example, if the configuration represents a   location in a weather app, the description may be the name of one   of the user’s favorite cities, such as  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentrecommendation/init(intent:description:)-3j1cv)*
# init(intent:description:)

**Framework**: WidgetKit  
**Kind**: init

Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
init(intent: Intent, description: Text)
```

#### Discussion

> **Note**: On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `AppIntentRecommendation` is inactive.

## Parameters

- `intent`: The intent that represents the recommended   configuration.
- `description`: A description that helps the user   understand the value of the preconfigured configuration option.   For example, if the configuration represents a location in a weather   app, the description may be the name of one of the user’s favorite   cities, such as  .

## See Also

- [init(intent: Intent, description: LocalizedStringKey)](appintentrecommendation/init(intent:description:)-2p4dh.md)
  Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets with a localized description.
- [init(intent: Intent, description: some StringProtocol)](appintentrecommendation/init(intent:description:)-7zn32.md)
  Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentrecommendation/init(intent:description:)-65igj)*
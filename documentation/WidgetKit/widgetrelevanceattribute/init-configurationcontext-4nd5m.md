# init(configuration:context:)

**Framework**: Widgetkit  
**Kind**: init

Creates a new widget relevance for a specific configuration that is relevant in a specific context.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
init(configuration: Configuration, context: RelevantContext)
```

#### Discussion

For example, a weather widget could specify that a configuration for a specific location is relevant for a the relevant context at that specific location.

## Parameters

- `configuration`: The specific configuration
- `context`: The relevant context where this widget is relevant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrelevanceattribute/init(configuration:context:)-4nd5m)*
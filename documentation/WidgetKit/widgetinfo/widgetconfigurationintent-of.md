# widgetConfigurationIntent(of:)

**Framework**: Widgetkit  
**Kind**: method

Gets the associated App Intent.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- watchOS 10.0+

## Declaration

```swift
func widgetConfigurationIntent<Intent>(of intentType: Intent.Type = Intent.self) -> Intent? where Intent : WidgetConfigurationIntent
```

## Mentions

- [Making a configurable widget](making-a-configurable-widget.md)

#### Return Value

An App Intent that contains the user-edited values or nil if there is no associated App Intent or the type does not match `intentType`.

## Parameters

- `intentType`: The expected type for the App Intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetinfo/widgetconfigurationintent(of:))*
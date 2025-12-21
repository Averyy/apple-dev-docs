# configurationIntent(of:)

**Framework**: WidgetKit  
**Kind**: method

Gets the associated App Intent.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func configurationIntent<Intent>(of intentType: Intent.Type = Intent.self) -> Intent? where Intent : ControlConfigurationIntent
```

#### Return Value

An App Intent that contains the user-edited values or nil if there is no associated App Intent or the type does not match `intentType`.

## Parameters

- `intentType`: The expected type for the App Intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlinfo/configurationintent(of:))*
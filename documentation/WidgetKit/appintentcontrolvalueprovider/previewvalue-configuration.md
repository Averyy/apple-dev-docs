# previewValue(configuration:)

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

A value to be shown while previewing the control in the add sheet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func previewValue(configuration: Self.Configuration) -> Self.Value
```

#### Discussion

This value should be generated quickly and cheaply. Calculate more expensive and accurate values in [`currentValue(configuration:)`](appintentcontrolvalueprovider/currentvalue(configuration:).md).

## Parameters

- `configuration`: The intent containing user-editable parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentcontrolvalueprovider/previewvalue(configuration:))*
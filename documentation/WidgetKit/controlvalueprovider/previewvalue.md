# previewValue

**Framework**: WidgetKit  
**Kind**: property  
**Required**: Yes

A value to be shown while previewing the control in the add sheet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var previewValue: Self.Value { get }
```

#### Discussion

This value should be generated quickly and cheaply. Calculate more expensive and accurate values in [`currentValue()`](controlvalueprovider/currentvalue().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlvalueprovider/previewvalue)*
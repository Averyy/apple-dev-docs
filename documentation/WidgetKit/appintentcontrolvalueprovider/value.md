# Value

**Framework**: WidgetKit  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of value provided to the template.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
associatedtype Value
```

## Discussion

When you create a custom provider, Swift infers this type from your implementation of the required [`previewValue(configuration:)`](./previewvalue%28configuration%29.md) and [`currentValue(configuration:)`](./currentvalue%28configuration%29.md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentcontrolvalueprovider/value)*
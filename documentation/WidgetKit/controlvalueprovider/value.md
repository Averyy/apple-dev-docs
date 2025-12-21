# Value

**Framework**: WidgetKit  
**Kind**: associatedtype  
**Required**: Yes

The type of value provided to the template.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
associatedtype Value
```

#### Discussion

When you create a custom provider, Swift infers this type from your implementation of the required [`previewValue`](controlvalueprovider/previewvalue.md) property and [`currentValue()`](controlvalueprovider/currentvalue().md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlvalueprovider/value)*
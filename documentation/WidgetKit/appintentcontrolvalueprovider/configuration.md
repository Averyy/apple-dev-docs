# Configuration

**Framework**: Widgetkit  
**Kind**: associatedtype  
**Required**: Yes

The type of intent used to prepare the value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
associatedtype Configuration : ControlConfigurationIntent
```

#### Discussion

When you create a custom provider, Swift infers this type from your implementation of the required `ValueProvider/previewValue(configuration:)` and `ValueProvider/currentValue(configuration:)` methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentcontrolvalueprovider/configuration)*
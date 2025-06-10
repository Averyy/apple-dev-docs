# subscript(dynamicMember:)

**Framework**: WidgetKit  
**Kind**: subscript

Returns the widget environment variants for a key path to an environment values instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: WritableKeyPath<EnvironmentValues, T>) -> [T]? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovidercontext/environmentvariants-swift.struct/subscript(dynamicmember:))*
# subscript(dynamicMember:)

**Framework**: Widgetkit  
**Kind**: subscript

Returns the widget environment variants for a key path to an environment values instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: WritableKeyPath<EnvironmentValues, T>) -> [T]? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovidercontext/environmentvariants-swift.struct/subscript(dynamicmember:))*
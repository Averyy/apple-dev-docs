# value(as:)

**Framework**: USDKit  
**Kind**: method

Returns the wrapped value if it is of type `T`, otherwise `nil`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func value<T>(as type: T.Type = T.self) -> T? where T : USDValueProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/value(as:))*
# value(as:)

**Framework**: USDKit  
**Kind**: method

Returns the wrapped value if it is of type `T`, otherwise `nil`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func value<T>(as type: T.Type = T.self) -> T? where T : USDValueProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/value(as:))*
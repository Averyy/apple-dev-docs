# init(_:)

**Framework**: USDKit  
**Kind**: init

Creates a value wrapping `value`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init<T>(_ value: T) where T : USDValueProtocol
```

## Parameters

- `value`: A value of any type that conforms to [`USDValueProtocol`](usdvalueprotocol.md).

## See Also

- [init()](usdvalue/init.md)
  Creates an empty value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/init(_:))*
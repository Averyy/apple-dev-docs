# isHolding(_:)

**Framework**: USDKit  
**Kind**: method

Returns whether this value holds a value of type `T`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func isHolding<T>(_ type: T.Type) -> Bool where T : USDValueProtocol
```

## See Also

- [func get<T>() -> T?](usdvalue/get.md)
  Returns the wrapped value if it is of type `T`, otherwise `nil`.
- [func uncheckedGet<T>() -> T](usdvalue/uncheckedget.md)
  Returns the wrapped value as `T` without checking the dynamic type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/isholding(_:))*
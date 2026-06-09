# uncheckedGet()

**Framework**: USDKit  
**Kind**: method

Returns the wrapped value as `T` without checking the dynamic type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func uncheckedGet<T>() -> T where T : USDValueProtocol
```

#### Discussion

> ❗ **Important**: The behaviour is undefined when `T` does not match the stored type. Prefer [`get()`](usdvalue/get().md) unless you have already confirmed the type with [`isHolding(_:)`](usdvalue/isholding(_:).md).

## See Also

- [func get<T>() -> T?](usdvalue/get.md)
  Returns the wrapped value if it is of type `T`, otherwise `nil`.
- [func isHolding<T>(T.Type) -> Bool](usdvalue/isholding(_:).md)
  Returns whether this value holds a value of type `T`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/uncheckedget())*
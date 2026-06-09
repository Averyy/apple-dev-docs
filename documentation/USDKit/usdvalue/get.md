# get()

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
func get<T>() -> T? where T : USDValueProtocol
```

## See Also

- [func uncheckedGet<T>() -> T](usdvalue/uncheckedget.md)
  Returns the wrapped value as `T` without checking the dynamic type.
- [func isHolding<T>(T.Type) -> Bool](usdvalue/isholding(_:).md)
  Returns whether this value holds a value of type `T`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/get())*
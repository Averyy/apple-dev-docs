# unsafeValue(assumingType:)

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
func unsafeValue<T>(assumingType type: T.Type = T.self) -> T where T : USDValueProtocol
```

#### Discussion

> ❗ **Important**: The behaviour is undefined when `T` does not match the stored type. Prefer [`value(as:)`](usdvalue/value(as:).md) unless you have already confirmed the type with [`isHolding(_:)`](usdvalue/isholding(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/unsafevalue(assumingtype:))*
# unsafeValue(assumingType:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns the wrapped value as `T` without checking the dynamic type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func unsafeValue<T>(assumingType type: T.Type = T.self) -> T where T : USDValueProtocol
```

#### Discussion

> ❗ **Important**: The behaviour is undefined when `T` does not match the stored type. Prefer [`value(as:)`](./value%28as%29.md) unless you have already confirmed the type with [`isHolding(_:)`](./isholding%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdvalue/unsafevalue(assumingtype:))*
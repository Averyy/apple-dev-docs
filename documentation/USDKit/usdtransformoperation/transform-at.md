# transform(at:)

**Framework**: USDKit  
**Kind**: method

Computes the transformation matrix at the specified time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func transform(at time: USDStage.TimeCode) -> USDValue.Matrix4d
```

#### Return Value

The transformation matrix.

## Parameters

- `time`: The time at which to evaluate the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdtransformoperation/transform(at:))*
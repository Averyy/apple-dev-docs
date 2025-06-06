# setValue(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the slider’s current value, allowing you to animate the change visually.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setValue(_ value: Float, animated: Bool)
```

#### Discussion

If you specify a value that is beyond the minimum or maximum values, the slider limits the value to the minimum or maximum. For example, if the minimum value is 0.0 and you specify -1.0, the slider sets the [`value`](uislider/value.md) property to 0.0.

## Parameters

- `value`: The new value to assign to the   property
- `animated`: Specify   to animate the change in value; otherwise, specify   to update the slider’s appearance immediately. Animations are performed asynchronously and do not block the calling thread.

## See Also

- [var value: Float](uislider/value.md)
  The slider’s current value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/setvalue(_:animated:))*
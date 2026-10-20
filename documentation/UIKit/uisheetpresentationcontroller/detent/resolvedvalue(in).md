# resolvedValue(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Resolves a detent to its value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
@preconcurrency func resolvedValue(in context: any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?
```

#### Return Value

A [`CGFloat`](../../../CoreFoundation/cgfloat-swift.struct.md) that represents the value of the detent, or `nil` if the detent is inactive in the provided context.

#### Discussion

You can use this method to get the values of the system [`medium`](./identifier-swift.struct/medium.md) and [`large`](./identifier-swift.struct/large.md) detents, or the value of a custom detent. Use this method inside [`custom(identifier:resolver:)`](./custom%28identifier,resolver%29.md) to construct a custom detent according to the values of known detents.

## Parameters

- `context`: A context for resolving custom detent values. This context is available in the `resolver` closure of [`custom(identifier:resolver:)`](./custom%28identifier,resolver%29.md).

## See Also

### Creating a custom detent
- [static func custom(identifier: UISheetPresentationController.Detent.Identifier?, resolver: (any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?) -> UISheetPresentationController.Detent](./custom%28identifier,resolver%29.md)
  Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [protocol UISheetPresentationControllerDetentResolutionContext](../../uisheetpresentationcontrollerdetentresolutioncontext.md)
  A context for resolving custom detent values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detent/resolvedvalue(in:))*
# addTransformOperation(type:)

**Framework**: USDKit  
**Kind**: method

Adds a transform operation of the given kind to this prim’s transform stack.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func addTransformOperation(type: USDTransformOperation.Kind)
```

#### Discussion

Creates the corresponding `xformOp:*` attribute and appends its name to the prim’s `xformOpOrder`.

## See Also

- [func applyAPISchema(USDToken) throws](usdprim/applyapischema(_:).md)
  Applies a single-apply API schema to this prim.
- [func applyAPISchema(USDToken, instanceName: USDToken) throws](usdprim/applyapischema(_:instancename:).md)
  Applies a multi-apply API schema to this prim with the given instance name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/addtransformoperation(type:))*
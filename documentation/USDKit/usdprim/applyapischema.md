# applyAPISchema(_:)

**Framework**: USDKit  
**Kind**: method

Applies a single-apply API schema to this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func applyAPISchema(_ schemaIdentifier: USDToken) throws
```

#### Discussion

> **Note**: An error if the schema cannot be applied.

## Parameters

- `schemaIdentifier`: The identifier of the API schema to apply.

## See Also

- [func applyAPISchema(USDToken, instanceName: USDToken) throws](usdprim/applyapischema(_:instancename:).md)
  Applies a multi-apply API schema to this prim with the given instance name.
- [func addTransformOperation(type: USDTransformOperation.Kind)](usdprim/addtransformoperation(type:).md)
  Adds a transform operation of the given kind to this prim’s transform stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/applyapischema(_:))*
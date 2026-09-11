# applyAPISchema(_:instanceName:)

**Framework**: USDKit  
**Kind**: method

Applies a multi-apply API schema to this prim with the given instance name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func applyAPISchema(_ schemaIdentifier: USDToken, instanceName: USDToken) throws
```

#### Discussion

> **Note**: An error if the schema cannot be applied.

## Parameters

- `schemaIdentifier`: The identifier of the API schema to apply.
- `instanceName`: The name of the schema instance to apply.

## See Also

- [func applyAPISchema(USDToken) throws](usdprim/applyapischema(_:).md)
  Applies a single-apply API schema to this prim.
- [func addTransformOperation(type: USDTransformOperation.Kind)](usdprim/addtransformoperation(type:).md)
  Adds a transform operation of the given kind to this prim’s transform stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/applyapischema(_:instancename:))*
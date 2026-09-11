# removeAPISchema(_:instanceName:)

**Framework**: USDKit  
**Kind**: method

Removes a multi-apply API schema from this prim with the given instance name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func removeAPISchema(_ schemaIdentifier: USDToken, instanceName: USDToken) throws
```

#### Discussion

> **Note**: An error if the schema cannot be removed.

## Parameters

- `schemaIdentifier`: The identifier of the API schema to remove.
- `instanceName`: The name of the schema instance to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/removeapischema(_:instancename:))*
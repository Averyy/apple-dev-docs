# removeAPISchema(_:instanceName:)

**Framework**: USDKit  
**Kind**: method

Removes a multi-apply API schema from this prim with the given instance name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
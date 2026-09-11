# add(_:position:)

**Framework**: USDKit  
**Kind**: method

Adds an existing payload arc to the prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func add(_ payload: USDPrim.Payload, position: USDPrim.ListPosition = .backOfPrependList) throws
```

#### Discussion

> **Note**: An error if the payload cannot be added.

## Parameters

- `payload`: The payload to add.
- `position`: Where to insert the payload in the prim’s payload list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/payloadcollection/add(_:position:))*
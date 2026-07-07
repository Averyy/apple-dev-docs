# add(_:position:)

**Framework**: USDKit  
**Kind**: method

Adds an existing payload arc to the prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
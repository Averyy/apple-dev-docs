# add(_:position:)

**Framework**: USDKit  
**Kind**: method

Adds an existing reference arc to the prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func add(_ reference: USDPrim.Reference, position: USDPrim.ListPosition = .backOfPrependList) throws
```

#### Discussion

> **Note**: An error if the reference cannot be added.

## Parameters

- `reference`: The reference to add.
- `position`: Where to insert the reference in the prim’s reference list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/referencecollection/add(_:position:))*
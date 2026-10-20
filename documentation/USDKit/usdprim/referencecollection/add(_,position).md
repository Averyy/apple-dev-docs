# add(_:position:)

**Framework**: USDKit  
**Kind**: method

Adds an existing reference arc to the prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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
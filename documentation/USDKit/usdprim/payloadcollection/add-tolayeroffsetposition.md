# add(to:layerOffset:position:)

**Framework**: USDKit  
**Kind**: method

Adds an internal payload arc that targets a prim in the same layer stack.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func add(to primPath: USDLayer.Path, layerOffset: USDLayer.TimeOffset = .init(), position: USDPrim.ListPosition = .backOfPrependList) throws
```

#### Discussion

> **Note**: An error if the payload cannot be added.

## Parameters

- `primPath`: The path of the target prim within the same layer stack.
- `layerOffset`: Time offset and scale to apply during composition.
- `position`: Where to insert the payload in the prim’s payload list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/payloadcollection/add(to:layeroffset:position:))*
# add(_:position:)

**Framework**: USDKit  
**Kind**: method

Adds an inherit arc to the prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func add(_ primPath: USDLayer.Path, position: USDPrim.ListPosition = .backOfPrependList) throws
```

#### Discussion

> **Note**: An error if the inherit cannot be added.

## Parameters

- `primPath`: The path of the prim to inherit from.
- `position`: Where to insert the inherit in the prim’s inherit list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/inheritcollection/add(_:position:))*
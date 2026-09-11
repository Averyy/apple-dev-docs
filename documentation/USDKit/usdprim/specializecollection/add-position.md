# add(_:position:)

**Framework**: USDKit  
**Kind**: method

Adds a specializes arc to the prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func add(_ primPath: USDLayer.Path, position: USDPrim.ListPosition = .backOfPrependList) throws
```

#### Discussion

> **Note**: An error if the specializes cannot be added.

## Parameters

- `primPath`: The path of the prim to specialize.
- `position`: Where to insert the specializes in the prim’s specializes list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/specializecollection/add(_:position:))*
# takeMeshUpdate(id:)

**Framework**: USDKit  
**Kind**: method

Consumes and returns the [`USDPlayer.MeshData.Update`](usdplayer/meshdata/update.md) for the given mesh delta update.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func takeMeshUpdate(id: USDPlayer.MeshID) -> USDPlayer.MeshData.Update?
```

#### Discussion

Returns `nil` if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/frameupdate/takemeshupdate(id:))*
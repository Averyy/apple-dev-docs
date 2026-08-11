# takeMaterialUpdate(id:)

**Framework**: USDKit  
**Kind**: method

Consumes and returns the [`USDPlayer.MaterialData.Update`](usdplayer/materialdata/update.md) for the given material delta update.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func takeMaterialUpdate(id: USDPlayer.MaterialID) -> USDPlayer.MaterialData.Update?
```

#### Discussion

Returns `nil` if not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdplayer/frameupdate/takematerialupdate(id:))*
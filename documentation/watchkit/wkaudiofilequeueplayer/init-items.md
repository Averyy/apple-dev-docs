# init(items:)

**Framework**: Watchkit  
**Kind**: init

Creates and returns a player initialized with an array of items.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(items: [WKAudioFilePlayerItem])
```

#### Return Value

An initialized player object.

#### Discussion

The contents of the `items` property represent the initial items to play but you may add items to this queue later.

## Parameters

- `items`: An array of   objects representing the assets to play. The order of the objects queue corresponds to the playback order of the assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer/init(items:))*
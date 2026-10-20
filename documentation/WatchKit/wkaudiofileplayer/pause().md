# pause()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Pauses playback of the associated item.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
func pause()
```

```objc
- (void) pause;
```

#### Discussion

This method sets the value of the [`rate`](./rate.md) property to `0.0`.

## See Also

### Configuring and Controlling Playback
- [func play()](./play%28%29.md)
  Begins playback of the current item.
- [var rate: Float](./rate.md)
  The current rate of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/pause())*
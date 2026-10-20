# play()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Begins playback of the current item.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
func play()
```

```objc
- (void) play;
```

#### Discussion

This method sets the value of the [`rate`](./rate.md) property to `1.0`.

## See Also

### Configuring and Controlling Playback
- [func pause()](./pause%28%29.md)
  Pauses playback of the associated item.
- [var rate: Float](./rate.md)
  The current rate of playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/play())*
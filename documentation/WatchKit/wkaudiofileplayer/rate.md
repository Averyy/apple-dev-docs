# rate

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The current rate of playback.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var rate: Float { get set }
```

```objc
@property (nonatomic) float rate;
```

#### Discussion

The playback rate refers to the playback speed. A value of `0.0` indicates that playback is paused while a value of `1.0` indicates playback is proceeding at the natural rate of the item. Rates other than `0.0` and `1.0` let you play the audio faster or slower than the natural rate of the item. Negative values let you play the audio in reverse.

## See Also

### Configuring and Controlling Playback
- [func play()](./play%28%29.md)
  Begins playback of the current item.
- [func pause()](./pause%28%29.md)
  Pauses playback of the associated item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/rate)*
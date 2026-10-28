# setStateFromPause(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the extension to a previously saved state.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func setStateFromPause(_ pausedState: [AnyHashable : Any]!)
```

```objc
- (void) setStateFromPause:(NSDictionary *) pausedState;
```

## Discussion

The Compressor app calls this method before resuming an encoding job. The Compressor app provides attributes an extension requires to resume an encoding job from the point at which the encoding stopped. These attributes are the ones the extension passed to the Compressor app while pausing an encoder job. If the attributes dictionary is empty, the extension restarts the encoding job from the beginning. See [`cancel(forPause:)`](./cancel%28forpause%29.md).

The Compressor app resumes the encoding job by calling the [`runTranscode(for:start:duration:toFile:startTimeCode:)`](./runtranscode%28for,start,duration,tofile,starttimecode%29.md) method.

## Parameters

- `pausedState`: A set of attributes specifying the extension’s previously saved state information.

## See Also

### Canceling or Pausing the Encoding Process
- [func cancel(forPause: Bool) -> [AnyHashable : Any]!](./cancel%28forpause%29.md)
  Pauses or cancels an encoding job.
- [func percentLostOnPause() -> Double](./percentlostonpause%28%29.md)
  Returns the percentage of the encoding job lost on pausing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/setstatefrompause(_:))*
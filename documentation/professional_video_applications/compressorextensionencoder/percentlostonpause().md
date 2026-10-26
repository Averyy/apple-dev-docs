# percentLostOnPause()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the percentage of the encoding job lost on pausing.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func percentLostOnPause() -> Double
```

```objc
- (double) percentLostOnPause;
```

#### Discussion

When a user requests to pause an encoding job, the Compressor app displays a value between 0 and 100 to indicate the percentage of the encoding job lost on pausing.

## See Also

### Canceling or Pausing the Encoding Process
- [func cancel(forPause: Bool) -> [AnyHashable : Any]!](./cancel%28forpause%29.md)
  Pauses or cancels an encoding job.
- [func setStateFromPause([AnyHashable : Any]!)](./setstatefrompause%28_%29.md)
  Sets the extension to a previously saved state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/percentlostonpause())*
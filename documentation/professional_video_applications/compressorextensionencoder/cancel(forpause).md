# cancel(forPause:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Pauses or cancels an encoding job.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
func cancel(forPause: Bool) -> [AnyHashable : Any]!
```

```objc
- (NSDictionary *) cancelForPause:(BOOL) forPause;
```

#### Return Value

`nil` if the extension does not support resuming a job where it left off. Otherwise, it returns a dictionary with attributes defining the extension’s paused state.

#### Discussion

Implement this method to pause or cancel an encoding job when the Compressor app requests to do so. If the extension supports resuming from a paused state, return the extension’s current state to the Compressor app. If the extension returns `nil`, an encoding job starts from the beginning when it resumes at a later point.

## Parameters

- `forPause`: When set to true, pauses an encoding job. When set to false, cancels the job.

## See Also

### Canceling or Pausing the Encoding Process
- [func setStateFromPause([AnyHashable : Any]!)](./setstatefrompause%28_%29.md)
  Sets the extension to a previously saved state.
- [func percentLostOnPause() -> Double](./percentlostonpause%28%29.md)
  Returns the percentage of the encoding job lost on pausing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/compressorextensionencoder/cancel(forpause:))*
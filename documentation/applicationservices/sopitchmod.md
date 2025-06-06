# soPitchMod

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soPitchMod: OSType { get }
```

#### Discussion

Get or set a speech channel’s pitch modulation.The `speechInfo` parameter isa pointer to a variable of type `Fixed`.Pitch modulation is also expressed as a fixed-point value in therange of 0.000 to 127.000. These values correspond to MIDI notevalues, where 60.000 is equal to middle C on a piano scale. Themost useful speech pitches fall in the range of 40.000 to 55.000.A pitch modulation value of 0.000 corresponds to a monotone in whichall speech is generated at the frequency corresponding to the speech pitch.Given a speech pitch value of 46.000, a pitch modulation of 2.000 wouldmean that the widest possible range of pitches corresponding tothe actual frequency of generated text would be 44.000 to 48.000.

This selector works with both the `GetSpeechInfo` and `SetSpeechInfo` functions.

> **Note**: The change in pitch modulation may not be noticeable until the next sentence or paragraph is spoken.

The change in pitch modulation may not be noticeable until the next sentence or paragraph is spoken.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sopitchmod)*
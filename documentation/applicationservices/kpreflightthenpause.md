# kPreflightThenPause

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var kPreflightThenPause: Int32 { get }
```

#### Discussion

Computes speech without generating.The `kPreflightThenPause` flagbit is used to minimize the latency experienced when the speechsynthesizer is attempting to speak. Ordinarily, whenever a callto `SpeakString`, `SpeakText`, or `SpeakBuffer` ismade, the speech synthesizer must perform a certain amount of initialprocessing before speech output is heard. This startup latency canvary from a few milliseconds to several seconds depending upon whichspeech synthesizer is being used. Recognizing that larger startupdelays might be detrimental to certain applications, a mechanism existsto allow the synthesizer to perform any necessary computations at noncriticaltimes. Once the computations have been completed, the speech isable to start instantly. When the `kPreflightThenPause` flagbit is set, the speech synthesizer will process the input text asnecessary to the point where it is ready to begin producing speechoutput. At this point, the synthesizer will enter a paused stateand return to the caller. When the application is ready to producespeech, it should call the `ContinueSpeech` functionto begin speaking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kpreflightthenpause)*
# soNumberMode

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soNumberMode: OSType { get }
```

#### Discussion

Get or set the speech channel’s current number-processingmode. Two `OSType` constantsare currently defined, [`modeNormal`](modenormal.md) and [`modeLiteral`](modeliteral.md).When the number-processing mode is `modeNormal`,the synthesizer assembles digits into numbers (so that “12” is spokenas “twelve”). When the mode is `modeLiteral`,each digit is spoken literally (so that “12” is spoken as “one, two”).The `speechInfo` parameteris a pointer to a variable of type `OSType`, whichspecifies the number-processing mode.

This selector works with both the `GetSpeechInfo` and `SetSpeechInfo` functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sonumbermode)*
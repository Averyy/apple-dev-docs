# soCharacterMode

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soCharacterMode: OSType { get }
```

#### Discussion

Get or set the speech channel’s character-processingmode. Two constants are currently defined for the processing mode, [`modeNormal`](modenormal.md) and [`modeLiteral`](modeliteral.md). Whenthe character-processing mode is `modeNormal`,input characters are spoken as you would expect to hear them. Whenthe mode is `modeLiteral`, eachcharacter is spoken literally, so that the word “cat” wouldbe spoken “C–A–T”. The `speechInfo` parameterpoints to a variable of type `OSType`, whichis the character-processing mode.

This selector works with the `GetSpeechInfo` and `SetSpeechInfo` functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/socharactermode)*
# soCharacterMode

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
soCharacterMode = 'char'
```

## Discussion

Get or set the speech channel’s character-processingmode. Two constants are currently defined for the processing mode, [`modeNormal`](../api-1552256-speech-channel_modes/modenormal.md) and [`modeLiteral`](../api-1552256-speech-channel_modes/modeliteral.md). Whenthe character-processing mode is `modeNormal`,input characters are spoken as you would expect to hear them. Whenthe mode is `modeLiteral`, eachcharacter is spoken literally, so that the word “cat” wouldbe spoken “C–A–T”. The `speechInfo` parameterpoints to a variable of type `OSType`, whichis the character-processing mode.

This selector works with the `GetSpeechInfo` and `SetSpeechInfo` functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552228-speech-channel_information_constants/socharactermode)*
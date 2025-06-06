# soSynthType

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soSynthType: OSType { get }
```

#### Discussion

Get a speech version information structurefor the speech synthesizer being used on the specified speech channel.The `speechInfo` parameteris a pointer to a speech version information structure, describedin [`SpeechVersionInfo`](speechversioninfo.md).

This selector works with the `GetSpeechInfo` function. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sosynthtype)*
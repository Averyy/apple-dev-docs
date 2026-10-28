# soPhonemeSymbols

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
soPhonemeSymbols = 'phsy'
```

## Discussion

Get a list of phoneme symbols and example wordsdefined for the speech channel’s synthesizer. Your applicationmight use this information to show the user what symbols to usewhen entering phonemic text directly. The `speechInfo` parameteris a pointer to a variable of type Handle that, on exit from the `GetSpeechInfo` function,is a handle to a phoneme descriptor structure, described in [`PhonemeDescriptor`](../phonemedescriptor.md).

This selector works with the `GetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552228-speech-channel_information_constants/sophonemesymbols)*
# soPhonemeOptions

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

Get or set options for the generation of phonetic output. See [Phoneme Generation Options](../api-1552233-phoneme_generation_options.md) for a complete list of options.

**Availability**:
- macOS 10.6+

## Declaration

```c
soPhonemeOptions = 'popt'
```

## Discussion

The `speechInfo` parameter is a pointer to a long value that represents the phoneme generation value.

This selector works with both the `GetSpeechInfo` and `SetSpeechInfo` functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552228-speech-channel_information_constants/sophonemeoptions)*
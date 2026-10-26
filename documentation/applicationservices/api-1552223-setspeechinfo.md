# SetSpeechInfo

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Changes a setting of a particular speech channel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr SetSpeechInfo(SpeechChannel chan, OSType selector, const void *speechInfo);
```

#### Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

#### Discussion

The `SetSpeechInfo` functionchanges the type of setting indicated by the `selector` parameterin the speech channel specified by the `chan` parameter,based on the data your application provides via the `speechInfo` parameter.

The format of the data structure specified by the `speechInfo` parameterdepends on the selector you choose. Ordinarily, a selector requiresthat `speechInfo` be apointer to a data structure that specifies a new setting for thespeech channel. 

## Parameters

- `chan`: The speech channel for which your application wishes to change a setting.
- `selector`: A speech information selector that indicates the type of information being changed.

  For a complete list of speech information selectors, see [Speech-Channel Information Constants](./api-1552228-speech-channel_information_constants.md). This list indicates how your application should set the `speechInfo` parameter for each selector.
- `speechInfo`: A pointer whose meaning depends on the speech information selector specified in the `selector` parameter. 

## See Also

### Changing Speech Attributes
- [SetSpeechProperty](./api-1459256-setspeechproperty.md)
  Sets the value of the specified speech-channel property.
- [SetSpeechPitch](./api-1462674-setspeechpitch.md)
  Sets the speech pitch on a designated speech channel.
- [SetSpeechRate](./api-1459896-setspeechrate.md)
  Sets the speech rate of a designated speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552223-setspeechinfo)*
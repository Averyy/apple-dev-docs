# GetSpeechInfo

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Gets information about a designated speech channel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr GetSpeechInfo(SpeechChannel chan, OSType selector, void *speechInfo);
```

## Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

## Discussion

The `GetSpeechInfo` functionreturns, in the data structure pointed to by the `speechInfo` parameter,the type of information requested by the `selector` parameteras it applies to the speech channel specified in the `chan` parameter.

The format of the data structure specified by the `speechInfo` parameterdepends on the selector you choose. For example, a selector mightrequire that your application allocate a block of memory of a certainsize and pass a pointer to that block. Another selector might requirethat `speechInfo` be setto the address of a handle variable. In this case, the `GetSpeechInfo` functionwould allocate a relocatable block of memory and change the handlevariable specified to reference the block. 

## Parameters

- `chan`: The speech channel about which information is being requested.
- `selector`: A speech information selector that indicates the type of information being requested.

  For a complete list of speech information selectors, see [Speech-Channel Information Constants](./api-1552228-speech-channel_information_constants.md). This list indicates how your application should set the `speechInfo` parameter for each selector.
- `speechInfo`: A pointer whose meaning depends on the speech information selector specified in the `selector` parameter. 

## See Also

### Obtaining Information About Speech and Speech Channels
- [CopySpeechProperty](./api-1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [GetSpeechPitch](./api-1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [GetSpeechRate](./api-1460797-getspeechrate.md)
  Gets a speech channel’s current speech rate.
- [SpeechBusy](./api-1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [SpeechBusySystemWide](./api-1460113-speechbusysystemwide.md)
  Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.
- [SpeechManagerVersion](./api-1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552220-getspeechinfo)*
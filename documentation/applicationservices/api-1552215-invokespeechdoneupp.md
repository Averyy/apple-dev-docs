# InvokeSpeechDoneUPP

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Invokes your speech-done callback function.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
void InvokeSpeechDoneUPP(SpeechChannel chan, SRefCon refCon, SpeechDoneUPP userUPP);
```

## Discussion

You should not need to call the `InvokeSpeechDoneUPP` function,because the system calls your speech-done callback function for you.

## See Also

### Creating, Invoking, and Disposing Universal Procedure Pointers
- [DisposeSpeechDoneUPP](./api-1552237-disposespeechdoneupp.md)
  Disposes of a universal procedure pointer (UPP) to a speech-donecallback function.
- [DisposeSpeechErrorUPP](./api-1552245-disposespeecherrorupp.md)
  Disposes of a universal procedure pointer (UPP) to anerror callback function.
- [DisposeSpeechPhonemeUPP](./api-1552226-disposespeechphonemeupp.md)
  Disposes of a universal procedure pointer (UPP) to a phonemecallback function.
- [DisposeSpeechSyncUPP](./api-1552219-disposespeechsyncupp.md)
  Disposes of a universal procedure pointer (UPP) to a synchronizationcallback function.
- [DisposeSpeechTextDoneUPP](./api-1552229-disposespeechtextdoneupp.md)
  Disposes of a universal procedure pointer (UPP) to a text-donecallback function. 
- [DisposeSpeechWordUPP](./api-1552222-disposespeechwordupp.md)
  Disposes of a universal procedure pointer (UPP) to a wordcallback function.
- [InvokeSpeechErrorUPP](./api-1552214-invokespeecherrorupp.md)
  Invokes your error callback function.
- [InvokeSpeechPhonemeUPP](./api-1552234-invokespeechphonemeupp.md)
  Invokes your phoneme callback function.
- [InvokeSpeechSyncUPP](./api-1552243-invokespeechsyncupp.md)
  Invokes your synchronization callback function.
- [InvokeSpeechTextDoneUPP](./api-1552249-invokespeechtextdoneupp.md)
  Invokes your text-done callback function.
- [InvokeSpeechWordUPP](./api-1552227-invokespeechwordupp.md)
  Invokes your word callback function.
- [NewSpeechDoneUPP](./api-1552218-newspeechdoneupp.md)
  Creates a new universal procedure pointer (UPP) to a speech-donecallback function.
- [NewSpeechErrorUPP](./api-1552224-newspeecherrorupp.md)
  Creates a new universal procedure pointer to an errorcallback function.
- [NewSpeechPhonemeUPP](./api-1552225-newspeechphonemeupp.md)
  Disposes of a universal procedure pointer (UPP) to a phonemecallback function.
- [NewSpeechSyncUPP](./api-1552244-newspeechsyncupp.md)
  Creates a new universal procedure pointer (UPP) to a synchronizationcallback function.
- [NewSpeechTextDoneUPP](./api-1552247-newspeechtextdoneupp.md)
  Creates a new universal procedure pointer (UPP) to a text-donecallback function.
- [NewSpeechWordUPP](./api-1552230-newspeechwordupp.md)
  Creates a new universal procedure pointer (UPP) to a wordcallback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552215-invokespeechdoneupp)*
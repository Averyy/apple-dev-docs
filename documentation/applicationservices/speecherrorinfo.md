# SpeechErrorInfo

**Framework**: Application Services  
**Kind**: struct

Defines a speech error information structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SpeechErrorInfo
```

#### Overview

By calling the [`GetSpeechInfo`](1552220-getspeechinfo.md) function with the `soErrors` selector, you can obtain a speech error information structure, which shows what Speech Synthesis Manager errors occurred while processing a text buffer on a given speech channel.

Speech error information structures never include errors that are returned by Speech Synthesis Manager functions. Instead, they reflect only errors encountered directly in the processing of text, and, in particular, in the processing of commands embedded within text.

The speech error information structure keeps track of only the most recent error and the first error that occurred after the previous call to the `GetSpeechInfo` function with the `soErrors` selector. If your application needs to keep track of all errors, then you should install an error callback function, [`SpeechErrorProcPtr`](speecherrorprocptr.md). 

## Topics

### Initializers
- [init()](speecherrorinfo/1463016-init.md)
- [init(count: Int16, oldest: OSErr, oldPos: Int, newest: OSErr, newPos: Int)](speecherrorinfo/1464795-init.md)
### Instance Properties
- [var count: Int16](speecherrorinfo/1459251-count.md)
  The number of errors that have occurred in processing the current text buffer since the last call to the `GetSpeechInfo` function with the `soErrors` selector. Of these errors, you can find information about only the first and last error that occurred.
- [var newPos: Int](speecherrorinfo/1464494-newpos.md)
  The character position within the text buffer being processed of the most recent error.
- [var newest: OSErr](speecherrorinfo/1461434-newest.md)
  The error code of the most recent error.
- [var oldPos: Int](speecherrorinfo/1460065-oldpos.md)
  The character position within the text buffer being processed of the first error that occurred after the previous call to the `GetSpeechInfo` function with the `soErrors` selector.
- [var oldest: OSErr](speecherrorinfo/1463962-oldest.md)
  The error code of the first error that occurred after the previous call to the `GetSpeechInfo` function with the `soErrors` selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speecherrorinfo)*
# inputBytesLeft

**Framework**: Application Services  
**Kind**: structp

The number of input bytes of the text that the speech channel must still process. When `inputBytesLeft` is 0, the buffer of input text passed to one of the `SpeakText` or `SpeakBuffer` functions may be disposed of. When you call the `SpeakString` function, the Speech Synthesis Manager stores a duplicate of the string to be spoken in an internal buffer; thus, you may delete the original string immediately after calling `SpeakString`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var inputBytesLeft: Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speechstatusinfo/1461214-inputbytesleft)*
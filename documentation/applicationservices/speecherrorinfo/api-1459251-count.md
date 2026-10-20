# count

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

The number of errors that have occurred in processing the current text buffer since the last call to the `GetSpeechInfo` function with the `soErrors` selector. Of these errors, you can find information about only the first and last error that occurred.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var count: Int16
```

```c
SInt16 count;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speecherrorinfo/1459251-count)*
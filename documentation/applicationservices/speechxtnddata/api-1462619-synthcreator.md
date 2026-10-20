# synthCreator

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

The synthesizer’s creator ID, identical to the value stored in the `synthManufacturer` field of a speech version information structure. You should set this field to the appropriate value before calling `GetSpeechInfo` or `SetSpeechInfo`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var synthCreator: OSType
```

```c
OSType synthCreator;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speechxtnddata/1462619-synthcreator)*
# soRefCon

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soRefCon: OSType { get }
```

#### Discussion

Set a speech channel’s reference constantvalue. The reference constant value is passed to application-definedcallback functions and might contain any value convenient for theapplication. The `speechInfo` parameteris a long integer containing the reference constant value. In contrastwith other selectors, this selector does not require that the `speechInfo` parameter’s valuebe a pointer value. Typically, however, an application does usethis selector to pass a pointer or handle value to callback functions.

This selector works with the `SetSpeechInfo` function. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sorefcon)*
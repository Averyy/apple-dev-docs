# kSpeechRefConProperty

**Framework**: Application Services  
**Kind**: data

Set a speech channel’s reference constant value.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechRefConProperty: CFString
```

#### Discussion

The reference constant value is passed to application-defined callback functions and might contain any value convenient for the application. The value associated with this property is a `CFNumber` object that contains an integer value. For example, an application might set the value of the `CFNumber` object to an address in memory that contains a reference to an object or a pointer to a function.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechrefconproperty)*
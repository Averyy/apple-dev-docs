# kSpeechPitchBaseProperty

**Framework**: Applicationservices  
**Kind**: data

Get or set the speech channel’s baseline speech pitch.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechPitchBaseProperty: CFString
```

#### Discussion

The value associated with this property is a `CFNumber` object that specifies the speech channel’s baseline speech pitch. 

Typical voice frequencies range from around 90 hertz for a low-pitched male voice to perhaps 300 hertz for a high-pitched child’s voice. These frequencies correspond to approximate pitch values in the ranges of 30.000 to 40.000 and 55.000 to 65.000, respectively.

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) and [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) functions.

> **Note**: The change in speech pitch may not be noticeable until the next sentence or paragraph is spoken.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechpitchbaseproperty)*
# kSpeechRateProperty

**Framework**: Application Services  
**Kind**: data

Get or set a speech channel’s speech rate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechRateProperty: CFString
```

#### Discussion

The value associated with this property is a `CFNumber` object that specifies the speech channel’s speaking rate. 

The range of supported rates is not predefined by the Speech Synthesis Manager; each speech synthesizer provides its own range of speech rates. Average human speech occurs at a rate of 180 to 220 words per minute.

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) and [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechrateproperty)*
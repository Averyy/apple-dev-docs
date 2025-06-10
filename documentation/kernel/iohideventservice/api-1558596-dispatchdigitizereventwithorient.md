# dispatchDigitizerEventWithOrientation

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.12.2+ - Deprecated in 10.15.1

## Declaration

```swift
void dispatchDigitizerEventWithOrientation(AbsoluteTime timeStamp, UInt32 transducerID, DigitizerTransducerType type, bool inRange, UInt32 buttonState, IOFixed x, IOFixed y, IOFixed z, IOFixed tipPressure, IOFixed auxPressure, IOFixed twist, DigitizerOrientationType orientationType, IOFixed *orientationParams, UInt32 orientationParamCount, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohideventservice/1558596-dispatchdigitizereventwithorient)*
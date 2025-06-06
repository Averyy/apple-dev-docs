# ScrollWheelEventCallback

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.3+

## Declaration

```swift
typedef void (*ScrollWheelEventCallback)(OSObject *target, short deltaAxis1, short deltaAxis2, short deltaAxis3, IOFixed fixedDelta1, IOFixed fixedDelta2, IOFixed fixedDelta3, SInt32 pointDelta1, SInt32 pointDelta2, SInt32 pointDelta3, SInt32 options, AbsoluteTime ts, OSObject *sender, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scrollwheeleventcallback)*
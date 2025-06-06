# AbsolutePointerEventCallback

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.3+

## Declaration

```swift
typedef void (*AbsolutePointerEventCallback)(OSObject *target, int buttons, IOGPoint *newLoc, IOGBounds *bounds, bool proximity, int pressure, int stylusAngle, AbsoluteTime ts, OSObject *sender, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/absolutepointereventcallback)*
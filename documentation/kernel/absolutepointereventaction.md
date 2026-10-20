# AbsolutePointerEventAction

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef void (*AbsolutePointerEventAction)(OSObject *target, int buttons, IOGPoint *newLoc, IOGBounds *bounds, bool proximity, int pressure, int stylusAngle, AbsoluteTime ts);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/absolutepointereventaction)*
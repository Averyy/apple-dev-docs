# CMLabColor

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains a color value expressed in the L*a*b* color space.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMLabColor {
    ...
} CMLabColor;
```

#### Overview

A color expressed in the L*a*b* color space is composed of `L`, `a`, and `b` component values. 

## Topics

### Instance Properties
- [L](./cmlabcolor/api-1560318-l.md)
  A numeric value within the range of 0 to 65535, which maps to 0 to 100 inclusive. Note that this encoding is slightly different from the 0 to 65280 encoding of the L channel defined in the ICC specification for PCS L*a*b values.
- [a](./cmlabcolor/api-1560358-a.md)
  A value that ranges from 0 to 65535, and maps to –128 to 127.996 inclusive. 
- [b](./cmlabcolor/api-1560421-b.md)
  A value that ranges from 0 to 65535, and maps to –128 to 127.996 inclusive. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmlabcolor)*
# CMLuvColor

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains a color value expressed in the L*u*v* color space.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMLuvColor {
    ...
} CMLuvColor;
```

#### Overview

A color value expressed in the L*u*v* color space is composed of `L`, `u`, and `v` component values. 

## Topics

### Instance Properties
- [L](./cmluvcolor/api-1560662-l.md)
  A numeric value within the range of 0 to 65535 that maps to 0 to 100 inclusive.
- [u](./cmluvcolor/api-1560134-u.md)
  A numeric value within the range of 0 to 65535 that maps to –128 to 127.996 inclusive.
- [v](./cmluvcolor/api-1560109-v.md)
  A numeric value within the range of 0 to 65535 that maps to –128 to 127.996 inclusive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmluvcolor)*
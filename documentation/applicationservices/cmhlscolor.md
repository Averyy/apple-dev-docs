# CMHLSColor

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains a color value expressed in the HLS color space.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMHLSColor {
    ...
} CMHLSColor;
```

#### Overview

A color value expressed in the HLS color space is composed of `hue`, `lightness`, and `saturation` component values. Each color component is expressed as a numeric value within the range of 0 to 65535 inclusive. 

## Topics

### Instance Properties
- [hue](./cmhlscolor/api-1560211-hue.md)
  A hue value that represents a fraction of a circle in which red is positioned at 0. .
- [lightness](./cmhlscolor/api-1560497-lightness.md)
  A lightness value.
- [saturation](./cmhlscolor/api-1560611-saturation.md)
  A saturation value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmhlscolor)*
# kIOHIDElementCalibrationGranularityKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

The scale or level of detail returned in a calibrated element value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOHIDElementCalibrationGranularityKey
```

## Discussion

Values are rounded off such that if granularity=0.1, values after calibration are 0, 0.1, 0.2, 0.3, etc.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiohidelementcalibrationgranularitykey)*
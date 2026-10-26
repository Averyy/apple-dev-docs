# IOPSLowBatteryWarningLevel

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

The battery can provide no more than 10 minutes of runtime.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
typedef enum IOPSLowBatteryWarningLevel : unsigned int {
    ...
} IOPSLowBatteryWarningLevel;
```

#### Overview

macOS makes no guarantees that the system shall remain in Final Warning for 10 minutes. Batteries are frequently calibrated differently and may provide runtime for more, or less, than the estimated 10 minutes.

## Topics

### Constants
- [kIOPSLowBatteryWarningNone](./iopslowbatterywarninglevel/kiopslowbatterywarningnone.md)
- [kIOPSLowBatteryWarningEarly](./iopslowbatterywarninglevel/kiopslowbatterywarningearly.md)
- [kIOPSLowBatteryWarningFinal](./iopslowbatterywarninglevel/kiopslowbatterywarningfinal.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopslowbatterywarninglevel)*
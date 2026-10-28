# kIOSystemLoadAdvisoryCombinedLevelKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Key for dictionary returned by IOCopySystemLoadAdvisoryDetailed

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOSystemLoadAdvisoryCombinedLevelKey
```

## Discussion

Provides a combined level based on UserLevel, BatteryLevel, and ThermalLevels; the combined level is the minimum of these levels. In the future, this combined level may represent new levels as well. The combined level is identical to the value returned by IOGetSystemLoadAdvisory().


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiosystemloadadvisorycombinedlevelkey)*
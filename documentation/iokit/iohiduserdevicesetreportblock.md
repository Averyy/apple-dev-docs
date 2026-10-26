# IOHIDUserDeviceSetReportBlock

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```c
typedef IOReturn (^IOHIDUserDeviceSetReportBlock)(IOHIDReportType type, uint32_t reportID, const uint8_t *report, CFIndex reportLength);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiduserdevicesetreportblock)*
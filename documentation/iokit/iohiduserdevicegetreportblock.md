# IOHIDUserDeviceGetReportBlock

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```c
typedef IOReturn (^IOHIDUserDeviceGetReportBlock)(IOHIDReportType type, uint32_t reportID, uint8_t *report, CFIndex *reportLength);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiduserdevicegetreportblock)*
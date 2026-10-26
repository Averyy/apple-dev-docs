# IOHIDReportWithTimeStampCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.10+

## Declaration

```c
typedef void (*IOHIDReportWithTimeStampCallback)(void *context, IOReturn result, void *sender, IOHIDReportType type, uint32_t reportID, uint8_t *report, CFIndex reportLength, uint64_t timeStamp);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidreportwithtimestampcallback)*
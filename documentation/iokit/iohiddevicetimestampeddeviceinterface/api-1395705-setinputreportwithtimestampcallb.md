# setInputReportWithTimeStampCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.10+

## Declaration

```c
IOReturn (*setInputReportWithTimeStampCallback)(void *self, uint8_t *report, CFIndex reportLength, IOHIDReportWithTimeStampCallback callback, void *context, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetimestampeddeviceinterface/1395705-setinputreportwithtimestampcallb)*
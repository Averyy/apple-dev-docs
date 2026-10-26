# getReport

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.10+

## Declaration

```c
IOReturn (*getReport)(void *self, IOHIDReportType reportType, uint32_t reportID, uint8_t *report, CFIndex *pReportLength, uint32_t timeout, IOHIDReportCallback callback, void *context, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicetimestampeddeviceinterface/1395735-getreport)*
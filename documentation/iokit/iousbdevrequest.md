# IOUSBDevRequest

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
typedef struct IOUSBDevRequest {
    ...
} IOUSBDevRequest;
```

## Overview

Parameter block for control requests, using a simple pointer for the data to be transferred.

## Topics

### Instance Properties
- [bRequest](./iousbdevrequest/api-1425442-brequest.md)
- [bmRequestType](./iousbdevrequest/api-1425959-bmrequesttype.md)
- [pData](./iousbdevrequest/api-1425983-pdata.md)
- [wIndex](./iousbdevrequest/api-1425343-windex.md)
- [wLenDone](./iousbdevrequest/api-1425789-wlendone.md)
- [wLength](./iousbdevrequest/api-1425950-wlength.md)
- [wValue](./iousbdevrequest/api-1425618-wvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdevrequest)*
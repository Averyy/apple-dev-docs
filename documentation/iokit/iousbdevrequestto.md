# IOUSBDevRequestTO

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
typedef struct IOUSBDevRequestTO {
    ...
} IOUSBDevRequestTO;
```

## Overview

Parameter block for control requests with timeouts, using a simple pointer for the data to be transferred. Same as a IOUSBDevRequest except for the two extra timeout fields.

## Topics

### Instance Properties
- [bRequest](./iousbdevrequestto/api-1425588-brequest.md)
- [bmRequestType](./iousbdevrequestto/api-1425926-bmrequesttype.md)
- [completionTimeout](./iousbdevrequestto/api-1425449-completiontimeout.md)
- [noDataTimeout](./iousbdevrequestto/api-1425759-nodatatimeout.md)
- [pData](./iousbdevrequestto/api-1425494-pdata.md)
- [wIndex](./iousbdevrequestto/api-1426031-windex.md)
- [wLenDone](./iousbdevrequestto/api-1425675-wlendone.md)
- [wLength](./iousbdevrequestto/api-1426024-wlength.md)
- [wValue](./iousbdevrequestto/api-1425335-wvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdevrequestto)*
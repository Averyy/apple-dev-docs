# wLenDone

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The number of data bytes that the system actually transferred.

**Availability**:
- macOS 10.1+

## Declaration

```c
UInt32 wLenDone;
```

## See Also

### Getting the Properties
- [bmRequestType](./api-1546443-bmrequesttype.md)
  The type of the request.
- [bRequest](./api-1546099-brequest.md)
  The request code.
- [wValue](./api-1546109-wvalue.md)
  The 16-bit parameter for the request.
- [wIndex](./api-1545920-windex.md)
  The 16-bit parameter for the request.
- [wLength](./api-1546286-wlength.md)
  The length of the data part of the request.
- [pData](./api-1546044-pdata.md)
  The pointer to the data for the request.
- [pipeRef](./api-1546157-piperef.md)
  A reference to the USB pipe.
- [completionTimeout](./api-1546368-completiontimeout.md)
  The value of the completion timeout in milliseconds.
- [noDataTimeout](./api-1546132-nodatatimeout.md)
  The value of the completion timeout in milliseconds if there’s no data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevreqoolto/1546113-wlendone)*
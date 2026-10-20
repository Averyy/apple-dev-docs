# bRequest

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The request code.

**Availability**:
- macOS 10.1+

## Declaration

```c
UInt8 bRequest;
```

## See Also

### Getting the Properties
- [bmRequestType](./api-1546240-bmrequesttype.md)
  The type of the request.
- [wValue](./api-1546569-wvalue.md)
  The 16-bit parameter for the request.
- [wIndex](./api-1545983-windex.md)
  The 16-bit parameter for the request.
- [wLength](./api-1546424-wlength.md)
  The length of the data part of the request.
- [pData](./api-1546393-pdata.md)
  The pointer to the data for the request.
- [wLenDone](./api-1546065-wlendone.md)
  The number of data bytes that the system actually transferred.
- [completionTimeout](./api-1546188-completiontimeout.md)
  The value of the completion timeout in milliseconds.
- [noDataTimeout](./api-1546538-nodatatimeout.md)
  The value of the completion timeout in milliseconds if there’s no data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevrequestto/1546186-brequest)*
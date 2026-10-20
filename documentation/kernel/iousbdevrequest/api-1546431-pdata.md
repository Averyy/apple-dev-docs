# pData

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The pointer to the data for the request.

**Availability**:
- macOS 10.0+

## Declaration

```c
void *pData;
```

## See Also

### Getting the Properties
- [bmRequestType](./api-1546317-bmrequesttype.md)
  The type of the request.
- [bRequest](./api-1546404-brequest.md)
  The request code.
- [wValue](./api-1546433-wvalue.md)
  The 16-bit parameter for the request.
- [wIndex](./api-1546579-windex.md)
  The 16-bit parameter for the request.
- [wLength](./api-1545928-wlength.md)
  The length of the data part of the request.
- [wLenDone](./api-1546308-wlendone.md)
  The number of data bytes that the system actually transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevrequest/1546431-pdata)*
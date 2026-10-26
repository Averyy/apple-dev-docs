# Keyword Parameter Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify keyword values for Apple event parameters, as well as information for the `AEManagerInfo` function to retrieve. Some common key word values are shown here.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : AEKeyword {
    ...
};
```

## Topics

### Constants
- [keyDirectObject](./api-1527206-keyword_parameter_constants/keydirectobject.md)
  Direct parameter. Usually specifies the data to be acted upon by the target application.
- [keyErrorNumber](./api-1527206-keyword_parameter_constants/keyerrornumber.md)
  Error number. Often used to extract error information from a reply Apple event.
- [keyErrorString](./api-1527206-keyword_parameter_constants/keyerrorstring.md)
  Error string. Often used to extract error information from a reply Apple event to display to the user.
- [keyProcessSerialNumber](./api-1527206-keyword_parameter_constants/keyprocessserialnumber.md)
  Process serial number. See also [`AEManagerInfo`](./api-1449373-aemanagerinfo.md).
- [keyPreDispatch](./api-1527206-keyword_parameter_constants/keypredispatch.md)
  A predispatch handler (an Apple event handler that the Apple Event Manager calls immediately before it dispatches an Apple event). See also [Managing Special Handler Dispatch Tables](../applicationservices/apple_event_manager.md#1652333).
- [keySelectProc](./api-1527206-keyword_parameter_constants/keyselectproc.md)
  You pass this value in the `functionClass` parameter of the [`AEManagerInfo`](./api-1449373-aemanagerinfo.md) function to disable the Object Support Library. Disabling the Object Support Library is not recommended.
- [keyAERecorderCount](./api-1527206-keyword_parameter_constants/keyaerecordercount.md)
  Used with the `keyword` parameter of the [`AEManagerInfo`](./api-1449373-aemanagerinfo.md) function. If you pass this value, on return, the `result` parameter supplies the number of processes that are currently recording Apple events.
- [keyAEVersion](./api-1527206-keyword_parameter_constants/keyaeversion.md)
  Used with the `keyword` parameter of the [`AEManagerInfo`](./api-1449373-aemanagerinfo.md) function. If you pass this value, on return, the `result` parameter supplies version information for the Apple Event Manager, in NumVersion format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1527206-keyword_parameter_constants)*
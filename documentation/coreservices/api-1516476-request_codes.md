# Request Codes

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
enum : int {
    ...
};
```

## Topics

### Constants
- [kComponentOpenSelect](./api-1516476-request_codes/kcomponentopenselect.md)
  A request to open a connection. Your component must respond to this request code.
- [kComponentCloseSelect](./api-1516476-request_codes/kcomponentcloseselect.md)
  A request to close a connection. Your component must respond to this request code.
- [kComponentCanDoSelect](./api-1516476-request_codes/kcomponentcandoselect.md)
  A request to determine whether your component supports a particular request. Your component must respond to this request code
- [kComponentVersionSelect](./api-1516476-request_codes/kcomponentversionselect.md)
  A request to return your component’s version number. Your component must respond to this request code.
- [kComponentRegisterSelect](./api-1516476-request_codes/kcomponentregisterselect.md)
  A request to determine whether your component can operate in the current environment. Your component may or may not respond to this request code.
- [kComponentTargetSelect](./api-1516476-request_codes/kcomponenttargetselect.md)
  A request to call another component whenever your component would call itself. Your component may or may not respond to this request code.
- [kComponentUnregisterSelect](./api-1516476-request_codes/kcomponentunregisterselect.md)
  A request to perform any operations necessary as a result of your component being unregistered. Your component may or may not respond to this request code
- [kComponentGetMPWorkFunctionSelect](./api-1516476-request_codes/kcomponentgetmpworkfunctionselect.md)
- [kComponentExecuteWiredActionSelect](./api-1516476-request_codes/kcomponentexecutewiredactionselect.md)
- [kComponentGetPublicResourceSelect](./api-1516476-request_codes/kcomponentgetpublicresourceselect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516476-request_codes)*
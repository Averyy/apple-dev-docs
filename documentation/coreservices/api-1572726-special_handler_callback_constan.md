# Special Handler Callback Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify an object callback function to install, get, or remove from the special handler dispatch table.

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
- [keyAERangeStart](./api-1572726-special_handler_callback_constan/keyaerangestart.md)
  Specifies the first Apple event object in a desired range.
- [keyAERangeStop](./api-1572726-special_handler_callback_constan/keyaerangestop.md)
  Specifies the last Apple event object in the desired range.
- [keyDisposeTokenProc](./api-1572726-special_handler_callback_constan/keydisposetokenproc.md)
  Token disposal function. See [`OSLDisposeTokenProcPtr`](./osldisposetokenprocptr.md).
- [keyAECompareProc](./api-1572726-special_handler_callback_constan/keyaecompareproc.md)
  Object-comparison function. See [`OSLCompareProcPtr`](./oslcompareprocptr.md).
- [keyAECountProc](./api-1572726-special_handler_callback_constan/keyaecountproc.md)
  Object-counting function. See [`OSLCountProcPtr`](./oslcountprocptr.md).
- [keyAEMarkTokenProc](./api-1572726-special_handler_callback_constan/keyaemarktokenproc.md)
  Mark token function. See [`OSLGetMarkTokenProcPtr`](./oslgetmarktokenprocptr.md).
- [keyAEMarkProc](./api-1572726-special_handler_callback_constan/keyaemarkproc.md)
  Object-marking function. See [`OSLMarkProcPtr`](./oslmarkprocptr.md).
- [keyAEAdjustMarksProc](./api-1572726-special_handler_callback_constan/keyaeadjustmarksproc.md)
  Mark-adjusting function. See [`OSLAdjustMarksProcPtr`](./osladjustmarksprocptr.md).
- [keyAEGetErrDescProc](./api-1572726-special_handler_callback_constan/keyaegeterrdescproc.md)
  Get error descriptor callback function. See [`OSLGetErrDescProcPtr`](./oslgeterrdescprocptr.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1572726-special_handler_callback_constan)*
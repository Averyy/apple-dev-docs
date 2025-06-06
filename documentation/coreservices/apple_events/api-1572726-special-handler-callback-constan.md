# Special Handler Callback Constants

**Framework**: Core Services

Specify an object callback function to install, get, or remove from the special handler dispatch table.

#### Overview

You use these constants with the [`AEInstallSpecialHandler(_:_:_:)`](1445532-aeinstallspecialhandler.md), [`AEGetSpecialHandler(_:_:_:)`](1444274-aegetspecialhandler.md), or [`AERemoveSpecialHandler(_:_:_:)`](1447960-aeremovespecialhandler.md) functions. 

## Topics

### Constants
- [var keyAERangeStart: AEKeyword](keyaerangestart.md)
  Specifies the first Apple event object in a desired range.
- [var keyAERangeStop: AEKeyword](keyaerangestop.md)
  Specifies the last Apple event object in the desired range.
- [var keyDisposeTokenProc: AEKeyword](keydisposetokenproc.md)
  Token disposal function. See [`OSLDisposeTokenProcPtr`](osldisposetokenprocptr.md).
- [var keyAECompareProc: AEKeyword](keyaecompareproc.md)
  Object-comparison function. See [`OSLCompareProcPtr`](oslcompareprocptr.md).
- [var keyAECountProc: AEKeyword](keyaecountproc.md)
  Object-counting function. See [`OSLCountProcPtr`](oslcountprocptr.md).
- [var keyAEMarkTokenProc: AEKeyword](keyaemarktokenproc.md)
  Mark token function. See [`OSLGetMarkTokenProcPtr`](oslgetmarktokenprocptr.md).
- [var keyAEMarkProc: AEKeyword](keyaemarkproc.md)
  Object-marking function. See [`OSLMarkProcPtr`](oslmarkprocptr.md).
- [var keyAEAdjustMarksProc: AEKeyword](keyaeadjustmarksproc.md)
  Mark-adjusting function. See [`OSLAdjustMarksProcPtr`](osladjustmarksprocptr.md).
- [var keyAEGetErrDescProc: AEKeyword](keyaegeterrdescproc.md)
  Get error descriptor callback function. See [`OSLGetErrDescProcPtr`](oslgeterrdescprocptr.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1572726-special_handler_callback_constan)*
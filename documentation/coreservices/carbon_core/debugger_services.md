# Debugger Services

**Framework**: Core Services  
**Role**: API Collection

Handle assertions and exceptions at run time.

> **Deprecated**: In macOS 10.8 and later, these macros are defined in `/usr/include/ConditionalMacros.h`.

#### Overview

> ⚠️ **Warning**: If your code includes the Core Services framework, be sure to include `AssertMacros.h` before you include `CoreServices.h`; otherwise, `DEBUG_ASSERT_MESSAGE` will be defined to use the deprecated `DebugAssert` function in `Debugging.h`.

## Topics

### Data Types
- [DebugAssertOutputHandlerProcPtr](../debugassertoutputhandlerprocptr.md)
- [DebugAssertOutputHandlerUPP](../debugassertoutputhandlerupp.md)
- [DebugComponentCallbackProcPtr](../debugcomponentcallbackprocptr.md)
- [DebugComponentCallbackUPP](../debugcomponentcallbackupp.md)
- [DebuggerDisposeThreadProcPtr](../debuggerdisposethreadprocptr.md)
- [DebuggerDisposeThreadTPP](../debuggerdisposethreadtpp.md)
- [DebuggerDisposeThreadUPP](../debuggerdisposethreadupp.md)
- [DebuggerNewThreadProcPtr](../debuggernewthreadprocptr.md)
- [DebuggerNewThreadTPP](../debuggernewthreadtpp.md)
- [DebuggerNewThreadUPP](../debuggernewthreadupp.md)
- [DebuggerThreadSchedulerProcPtr](../debuggerthreadschedulerprocptr.md)
- [DebuggerThreadSchedulerTPP](../debuggerthreadschedulertpp.md)
- [DebuggerThreadSchedulerUPP](../debuggerthreadschedulerupp.md)

## See Also

### Services
- [Multiprocessing Services](./multiprocessing_services.md)
  Support multitasking in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/debugger_services)*
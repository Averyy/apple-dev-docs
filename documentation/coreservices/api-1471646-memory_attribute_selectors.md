# Memory Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for memory.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltOSAttr](./api-1471646-memory_attribute_selectors/gestaltosattr.md)
- [gestaltSysZoneGrowable](./api-1471646-memory_attribute_selectors/gestaltsyszonegrowable.md)
- [gestaltLaunchCanReturn](./api-1471646-memory_attribute_selectors/gestaltlaunchcanreturn.md)
- [gestaltLaunchFullFileSpec](./api-1471646-memory_attribute_selectors/gestaltlaunchfullfilespec.md)
- [gestaltLaunchControl](./api-1471646-memory_attribute_selectors/gestaltlaunchcontrol.md)
  If this bit is set, the Process Manager is available.
- [gestaltTempMemSupport](./api-1471646-memory_attribute_selectors/gestalttempmemsupport.md)
  If `true`, there is temporary memory support.
- [gestaltRealTempMemory](./api-1471646-memory_attribute_selectors/gestaltrealtempmemory.md)
  If `true`, temporary memory handles are real.
- [gestaltTempMemTracked](./api-1471646-memory_attribute_selectors/gestalttempmemtracked.md)
  If `true`, temporary memory handles are tracked.
- [gestaltIPCSupport](./api-1471646-memory_attribute_selectors/gestaltipcsupport.md)
- [gestaltSysDebuggerSupport](./api-1471646-memory_attribute_selectors/gestaltsysdebuggersupport.md)
- [gestaltNativeProcessMgrBit](./api-1471646-memory_attribute_selectors/gestaltnativeprocessmgrbit.md)
- [gestaltAltivecRegistersSwappedCorrectlyBit](./api-1471646-memory_attribute_selectors/gestaltaltivecregistersswappedcorrectlybit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471646-memory_attribute_selectors)*
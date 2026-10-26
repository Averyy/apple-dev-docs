# gestaltLaunchCanReturn

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltLaunchCanReturn = 1
```

#### Discussion

If this bit is set, the `_Launch` trap macro can return to the caller. The `_Launch` trap macro in system software version 7.0 (and in earlier versions running MultiFinder) gives your application the option to continue running after it launches another application. In earlier versions of system software not running MultiFinder, the `_Launch` trap macro forces the launching application to quit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471646-memory_attribute_selectors/gestaltlaunchcanreturn)*
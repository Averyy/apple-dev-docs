# kIOPSCommandDelayedRemovePowerKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Command to give a UPS when it should remove power from its AC plugs in a specified amount of time

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kIOPSCommandDelayedRemovePowerKey
```

#### Discussion

- The matching argument should be a CFNumber of kCFNumberIntType specifying when the UPS should
- remove power from its AC power ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopscommanddelayedremovepowerkey)*
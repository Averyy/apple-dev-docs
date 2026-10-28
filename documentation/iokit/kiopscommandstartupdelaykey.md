# kIOPSCommandStartupDelayKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Tell UPS how long it should wait for

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kIOPSCommandStartupDelayKey
```

## Discussion

- The matching argument should be a CFNumber of kCFNumberIntType specifying when the UPS should
- remove power from its AC power ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopscommandstartupdelaykey)*
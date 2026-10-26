# kIOPMAssertionTimeoutActionLog

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A potential value for [`kIOPMAssertionTimeoutActionKey`](./kiopmassertiontimeoutactionkey.md)

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionTimeoutActionLog
```

#### Discussion

When this timeout action is specified, PM will log the timeout event but will not turn off or affect the setting of the assertion in any way.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertiontimeoutactionlog)*
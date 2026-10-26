# kIOPMAssertionTimeoutActionRelease

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A potential value for [`kIOPMAssertionTimeoutActionKey`](./kiopmassertiontimeoutactionkey.md)

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionTimeoutActionRelease
```

#### Discussion

When a timeout expires with this action, Power Management will log the timeout event, and will release the assertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertiontimeoutactionrelease)*
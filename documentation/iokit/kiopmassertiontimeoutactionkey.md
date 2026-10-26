# kIOPMAssertionTimeoutActionKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Specifies the action to take upon timeout expiration.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionTimeoutActionKey
```

#### Discussion

The action specified by this key applies only if you include an [`kIOPMAssertionTimeoutKey`](./kiopmassertiontimeoutkey.md). If you don’t specify a timeout action, the default is [`kIOPMAssertionTimeoutActionTurnOff`](./kiopmassertiontimeoutactionturnoff.md).

You can add this key in the dictionary you pass to [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md). The key may be present in the dictionary that [`IOPMAssertionCopyProperties`](./api-1557066-iopmassertioncopyproperties.md) returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertiontimeoutactionkey)*
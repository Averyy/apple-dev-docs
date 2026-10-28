# kIOPMAssertionFrameworkIDKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

Specify if the assertion creator is a framework.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPMAssertionFrameworkIDKey
```

## Discussion

If the code that creates the assertion resides in a framework or library, the caller should specify a CFBundleIdentifier, as a CFString, identifying that bundle here. This info helps developers and administrators determine the source of an assertion.

This key may be specified in the dictionary passed to [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md).

This key may be present in the dictionary returned from [`IOPMAssertionCopyProperties`](./api-1557066-iopmassertioncopyproperties.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertionframeworkidkey)*
# Filter

**Framework**: Kernel  
**Kind**: tdef

## Declaration

```c
typedef bool ( *Filter)(
   OSObject *,
   IOFilterInterruptEventSource *);
```

#### Return Value

false if this interrupt can be ignored.

#### Overview

C Function pointer to a routine to call when an interrupt occurs.

## Parameters

- `owner`: Pointer to the owning/client instance.
- `sender`: Where is the interrupt comming from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource/filter)*
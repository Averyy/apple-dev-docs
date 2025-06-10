# Filter

**Framework**: Kernel  
**Kind**: tdef

## Declaration

```swift
typedef bool ( *Filter)(
   OSObject *,
   IOFilterInterruptEventSource *);
```

#### Return_value

false if this interrupt can be ignored.

#### Overview

C Function pointer to a routine to call when an interrupt occurs.

## Parameters

- `owner`: Pointer to the owning/client instance.
- `sender`: Where is the interrupt comming from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource/filter)*
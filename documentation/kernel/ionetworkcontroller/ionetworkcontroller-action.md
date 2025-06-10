# IONetworkController::Action

**Framework**: Kernel  
**Kind**: tdef

## Declaration

```swift
typedef IOReturn ( *Action)(
   void *target,
   void *param0,
   void *param1,
   void *param2,
   void *param3);
```

#### Overview

Definition of a C function that can be called through executeCommand().

## Parameters

- `target`: The first argument passed to action.
- `param0`: Action parameter 0.
- `param1`: Action parameter 1.
- `param2`: Action parameter 2.
- `param3`: Action parameter 3.

## See Also

- [Action](ioworkloop/action.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkcontroller/ionetworkcontroller_action)*
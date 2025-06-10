# IntValueChangeHandler

**Framework**: Kernel  
**Kind**: tdef

Handler function used to make a notification when a value is to be changed.

## Declaration

```swift
typedef IOReturn ( *IntValueChangeHandler)(
   OSObject *target,
   IOAudioControl *audioControl,
   SInt32 oldValue,
   SInt32 newValue);
```

#### Return_value

Must return kIOReturnSuccess when the hardware is successfully updated.

## Parameters

- `target`: Reference supplied when the handler was registered.
- `audioControl`: The IOAudioControl that is changing.
- `oldValue`: The old value of the control.
- `newValue`: The new value the control is being changed to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiocontrol/intvaluechangehandler)*
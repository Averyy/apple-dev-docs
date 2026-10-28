# start

**Framework**: Kernel  
**Kind**: instm

Called to start a newly created IOAudioPort.

## Declaration

```cpp
virtual bool start(
 IOService *provider);
```

## Return Value

Returns true on success

## Overview

This is called automatically by IOAudioDevice when attachAudioPort() is called.

## Parameters

- `provider`: The IOAudioDevice that owns this port

## See Also

### Miscellaneous
- [addAudioControl](./api-1811855-addaudiocontrol.md)
  Adds a newly created IOAudioControl instance to the port.
- [deactivateAudioControls](./api-1811875-deactivateaudiocontrols.md)
  Called to shut down all of the audio controls for this port.
- [free](./api-1811888-free.md)
  Frees all of the resources allocated by the IOAudioPort.
- [initWithAttributes](./api-1811904-initwithattributes.md)
  Initializes a newly allocated IOAudioPort instance with the given attributes
- [stop](./api-1811938-stop.md)
  Called when the IOAudioDevice is stopping when it is no longer available.
- [withAttributes](./api-1811950-withattributes.md)
  Allocates a new IOAudioPort instance with the given attributes


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioport/1811924-start)*
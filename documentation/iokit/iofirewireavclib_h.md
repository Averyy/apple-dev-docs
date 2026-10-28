# IOFireWireAVCLib.h

**Framework**: IOKit  
**Role**: API Collection

## Overview

### Included Headers

- <IOKit/IOCFPlugIn.h>
- <IOKit/firewire/IOFireWireFamilyCommon.h>
- <IOKit/avc/IOFireWireAVCConsts.h>

## Topics

### Callbacks
- [IOFWAVCCommandHandlerCallback](./iofwavccommandhandlercallback.md)
  Callback called when a incoming AVC command matching a registered command handler is received.
- [IOFWAVCPCRCallback](./iofwavcpcrcallback.md)
  Callback called after a successful lock transaction to a CMP plug.
- [IOFWAVCRequestCallback](./iofwavcrequestcallback.md)
  This Callback has been deprecated. Use installAVCCommandHandler instead.
- [IOFWAVCSubunitPlugHandlerCallback](./iofwavcsubunitplughandlercallback.md)
  Callback called when a incoming AVC command matching a registered command handler is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclib_h)*
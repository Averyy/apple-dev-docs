# setNotificationTarget

**Framework**: Kernel  
**Kind**: instm

Registers a C function to handle access notifications sent from this object.

## Declaration

```cpp
virtual void setNotificationTarget(
 void *target, 
 Action action, 
 void *param = 0);
```

## Overview

A notification is sent by an IONetworkData object to the registered notification handler, when an access method is called to modify the contents of the data buffer.

## Parameters

- `target`: The first parameter passed to the notification handler.
- `action`: A pointer to a C function that will handle the notification. If 0, then notification is disabled.
- `param`: An optional parameter passed to the notification handler.

## See Also

### Miscellaneous
- [clearBuffer](./api-1812449-clearbuffer.md)
  Clears the data buffer by filling it with zeroes.
- [free](./api-1812455-free.md)
  Frees the IONetworkData object.
- [getAccessTypes](./api-1812461-getaccesstypes.md)
  Gets the types of data access supported by this object.
- [getBuffer](./api-1812470-getbuffer.md)
  Gets a pointer to the data buffer.
- [getBufferType](./api-1812479-getbuffertype.md)
  Gets the type of data buffer managed by this object.
- [getKey](./api-1812486-getkey.md)
  Gets a unique OSSymbol key associated with this object.
- [getNotificationAction](./api-1812491-getnotificationaction.md)
  Gets the C function that was registered to handle access notifications sent from this object.
- [getNotificationParameter](./api-1812494-getnotificationparameter.md)
  Gets the parameter that will be passed to the access notification handler.
- [getNotificationTarget](./api-1812497-getnotificationtarget.md)
  Gets the first parameter that will be passed to the access notification handler.
- [getSize](./api-1812500-getsize.md)
  Gets the size of the data buffer.
- [init](./api-1812508-init.md)
  Initializes an IONetworkData object.
- [read](./api-1812511-read.md)
  An access method that reads from the data buffer.
- [readBytes](./api-1812517-readbytes.md)
  Reads from the data buffer and copies the data to a destination buffer provided by the caller.
- [reset](./api-1812524-reset.md)
  An access method that resets the data buffer.
- [serialize](./api-1812531-serialize.md)
  Serializes the IONetworkData object.
- [setAccessTypes](./api-1812540-setaccesstypes.md)
  Sets the types of access that are permitted on the data buffer.
- [withExternalBuffer](./api-1812563-withexternalbuffer.md)
  Factory method that constructs and initializes an IONetworkData object with an external data buffer.
- [withInternalBuffer](./api-1812581-withinternalbuffer.md)
  Factory method that constructs and initializes an IONetworkData object with an internal data buffer.
- [withNoBuffer](./api-1812601-withnobuffer.md)
  Factory method that constructs and initializes an IONetworkData object without a data buffer.
- [write](./api-1812620-write.md)
  An access method that writes to the data buffer.
- [writeBytes](./api-1812640-writebytes.md)
  Writes to the data buffer with data from a source buffer provided by the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkdata/1812552-setnotificationtarget)*
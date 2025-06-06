# sendAsyncResult64WithOptions

**Framework**: Kernel  
**Kind**: instm

Send a notification as with sendAsyncResult, but with finite queueing.

## Declaration

```swift
static IOReturn sendAsyncResult64WithOptions(
 OSAsyncReference64 reference, 
 IOReturn result,
 io_user_reference_t args[],
 UInt32 numArgs, 
 IOOptionBits options);
```

#### Overview

IOUserClient::sendAsyncResult64() will infitely queue messages if the client is not processing them in a timely fashion. This variant will not, for simple handling of situations where clients may be expected to stop processing messages.

## See Also

- [exportObjectToClient](iouserclient/1809421-exportobjecttoclient.md)
- [releaseAsyncReference64](iouserclient/1809435-releaseasyncreference64.md)
  Release the mach_port_t reference held within the OSAsyncReference64 structure.
- [releaseNotificationPort](iouserclient/1809442-releasenotificationport.md)
  Release the mach_port_t passed to registerNotificationPort().
- [removeMappingForDescriptor](iouserclient/1809451-removemappingfordescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iouserclient/1809458-sendasyncresult64withoptions)*
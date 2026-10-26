# NotificationIsOn

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Is notification on?

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
Boolean (*NotificationIsOn)(IOFireWireLibIRMAllocationRef self);
```

#### Return Value

Returns true if notifications for this IRMAllocation are enabled

## Parameters

- `self`: The IRMAllocation interface to use.

## See Also

### Miscellaneous
- [allocateIsochResources](./api-1555936-allocateisochresources.md)
  Use this interface to allocate isochronous resources
- [areIsochResourcesAllocated](./api-1555631-areisochresourcesallocated.md)
  Poll to see if IRM resources are still allocated
- [deallocateIsochResources](./api-1556089-deallocateisochresources.md)
  Deallocate previously allocated resources
- [GetRefCon](./api-1555605-getrefcon.md)
  Get the current refcon
- [SetRefCon](./api-1555776-setrefcon.md)
  Set a new refcon
- [setReleaseIRMResourcesOnFree](./api-1555923-setreleaseirmresourcesonfree.md)
  Set a new value for releaseIRMResourcesOnFree
- [TurnOffNotification](./api-1555873-turnoffnotification.md)
  Force notification off.
- [TurnOnNotification](./api-1555769-turnonnotification.md)
  Try to turn on notifications


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelibirmallocationinterface/1556097-notificationison)*
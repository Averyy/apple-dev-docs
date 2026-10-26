# deallocateIsochResources

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Deallocate previously allocated resources

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
IOReturn (*deallocateIsochResources)(IOFireWireLibIRMAllocationRef self);
```

#### Return Value

Returns true if deallocation success

## Parameters

- `self`: The IRMAllocation interface to use.

## See Also

### Miscellaneous
- [allocateIsochResources](./api-1555936-allocateisochresources.md)
  Use this interface to allocate isochronous resources
- [areIsochResourcesAllocated](./api-1555631-areisochresourcesallocated.md)
  Poll to see if IRM resources are still allocated
- [GetRefCon](./api-1555605-getrefcon.md)
  Get the current refcon
- [NotificationIsOn](./api-1556097-notificationison.md)
  Is notification on?
- [SetRefCon](./api-1555776-setrefcon.md)
  Set a new refcon
- [setReleaseIRMResourcesOnFree](./api-1555923-setreleaseirmresourcesonfree.md)
  Set a new value for releaseIRMResourcesOnFree
- [TurnOffNotification](./api-1555873-turnoffnotification.md)
  Force notification off.
- [TurnOnNotification](./api-1555769-turnonnotification.md)
  Try to turn on notifications


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelibirmallocationinterface/1556089-deallocateisochresources)*
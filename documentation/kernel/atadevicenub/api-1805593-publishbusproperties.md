# publishBusProperties

**Framework**: Kernel  
**Kind**: instm

puts info about this device's bus capability in the device tree.

## Declaration

```cpp
virtual void publishBusProperties(
 void);
```

## See Also

### Miscellaneous
- [allocCommand](./api-1805563-alloccommand.md)
  create command objects for clients.
- [ataDeviceNub](./api-1805565-atadevicenub.md)
  static creator function - used by IOATAControllers to create nubs.
- [attach](./api-1805568-attach.md)
  override of IOService method.
- [executeCommand](./api-1805572-executecommand.md)
  Submit IO requests
- [freeCommand](./api-1805576-freecommand.md)
  Clients use this method to dispose of command objects.
- [getDeviceID](./api-1805578-getdeviceid.md)
  get the unit id of this drive (0 or 1)
- [init](./api-1805582-init.md)
  used after creating the nub.
- [MyATACallback](./api-1805585-myatacallback.md)
  to be deprecated.
- [processCallback](./api-1805590-processcallback.md)
  to be deprecated.
- [publishProperties](./api-1805598-publishproperties.md)
  publish the nub's properties in the device tree.
- [publishVendorProperties](./api-1805600-publishvendorproperties.md)
  will be deprecated.
- [swapBytes16](./api-1805603-swapbytes16.md)
  to be deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/atadevicenub/1805593-publishbusproperties)*
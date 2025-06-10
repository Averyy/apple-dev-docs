# allocCommand

**Framework**: Kernel  
**Kind**: instm

create command objects for clients.

## Declaration

```swift
virtual IOATACommand* allocCommand(
 void );
```

## See Also

- [ataDeviceNub](atadevicenub/1805565-atadevicenub.md)
  static creator function - used by IOATAControllers to create nubs.
- [attach](atadevicenub/1805568-attach.md)
  override of IOService method.
- [executeCommand](atadevicenub/1805572-executecommand.md)
  Submit IO requests
- [freeCommand](atadevicenub/1805576-freecommand.md)
  Clients use this method to dispose of command objects.
- [getDeviceID](atadevicenub/1805578-getdeviceid.md)
  get the unit id of this drive (0 or 1)
- [init](atadevicenub/1805582-init.md)
  used after creating the nub.
- [MyATACallback](atadevicenub/1805585-myatacallback.md)
  to be deprecated.
- [processCallback](atadevicenub/1805590-processcallback.md)
  to be deprecated.
- [publishBusProperties](atadevicenub/1805593-publishbusproperties.md)
  puts info about this device's bus capability in the device tree.
- [publishProperties](atadevicenub/1805598-publishproperties.md)
  publish the nub's properties in the device tree.
- [publishVendorProperties](atadevicenub/1805600-publishvendorproperties.md)
  will be deprecated.
- [swapBytes16](atadevicenub/1805603-swapbytes16.md)
  to be deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/atadevicenub/1805563-alloccommand)*
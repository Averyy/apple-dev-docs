# Device

**Framework**: TVMLKit JS  
**Kind**: cl  
**Role**: Class

An object that provides information about an Apple TV and the host app installed on the device.

**Availability**:
- tvOS 9.0+

## Declaration

```
interface Device
```

## Overview

You cannot create an instance of the `Device` class. An instance of this class is available in the global context as `Device`.

## Topics

### Retrieving Device Information
- [appIdentifier](./device/api-1627339-appidentifier.md)
  The unique identifier for the app.
- [appVersion](./device/api-1627395-appversion.md)
  The current app version.
- [model](./device/api-1627347-model.md)
  A string that identifies the device model.
- [productType](./device/api-1627386-producttype.md)
  The version of the product installed on the Apple TV.
- [systemVersion](./device/api-1627323-systemversion.md)
  The tvOS version.
- [vendorIdentifier](./device/api-1627383-vendoridentifier.md)
  The universally unique identifier (UUID) of the device.

## See Also

### Device Settings
- [Settings](./settings.md)
  An object that provides access to setting information for a device.
- [Restrictions](./restrictions.md)
  An object used to retrieve rating restriction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/device)*
# WAError

**Framework**: Wi-Fi Aware  
**Kind**: enum

An error in Wi-Fi Aware.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum WAError
```

#### Overview

Wi-Fi Aware may throw a [`WAError`](waerror.md) to indicate when an underlying issue occurs, with the [`Network`](https://developer.apple.comhttps://developer.apple.com/documentation/Network) framework throwing an `NWError`. If the `NWError` occurs due to Wi-Fi Aware, then the `Network/NWError/wifiAware` property on `Network/NWError` can provide access to additional information about the underlying Wi-Fi Aware error.

## Topics

### Checking for general errors
- [case error(WAError.ErrorDetails)](waerror/error(_:).md)
  A general error.
- [WAError.ErrorDetails](waerror/errordetails.md)
  The optional details describing the error.
### Checking for missing entitlement
- [WAError.EntitlementMissingDetails](waerror/entitlementmissingdetails.md)
  The optional details describing the missing entitlement.
- [case entitlementMissing(WAError.EntitlementMissingDetails)](waerror/entitlementmissing(_:).md)
  An error that occurs if your app is missing the entitlement needed for the requested operation.
### Checking for unsupported host hardware
- [case wifiAwareUnsupported(WAError.WiFiAwareUnsupportedDetails)](waerror/wifiawareunsupported(_:).md)
  An error that occurs if Wi-Fi Aware isn’t supported on the device.
- [WAError.WiFiAwareUnsupportedDetails](waerror/wifiawareunsupporteddetails.md)
  The optional details describing the unavailability of Wi-Fi Aware on the device.
### Checking for insufficient radio resources
- [case noRadioResources(WAError.NoRadioResourcesDetails)](waerror/noradioresources(_:).md)
  An error that occurs if the radio lacks resources.
- [WAError.NoRadioResourcesDetails](waerror/noradioresourcesdetails.md)
  The optional details describing what resources are lacking.
### Checking for undeclared services
- [case serviceNotDeclared(WAError.ServiceNotDeclaredDetails)](waerror/servicenotdeclared(_:).md)
  An error that occurs if your app didn’t declare the necessary services.
- [WAError.ServiceNotDeclaredDetails](waerror/servicenotdeclareddetails.md)
  The optional details that describe the app service wasn’t declared.
### Checking for service already in use
- [case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)](waerror/servicealreadysubscribing(_:).md)
  An error that occurs if a new subscriber or `Network/NetworkBrowser` can’t be created.
- [WAError.ServiceAlreadySubscribingDetails](waerror/servicealreadysubscribingdetails.md)
  The optional details describing the service that’s subscribing.
- [case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)](waerror/servicealreadypublishing(_:).md)
  An error that occurs if a new publisher or `Network/NetworkListener` can’t be created.
- [WAError.ServiceAlreadyPublishingDetails](waerror/servicealreadypublishingdetails.md)
  The optional details describing the service that’s publishing.
### Checking if paired devices are present or specified
- [case noPairedDevices(WAError.NoPairedDevicesDetails)](waerror/nopaireddevices(_:).md)
  An error that occurs if your app doesn’t have access to any paired devices.
- [WAError.NoPairedDevicesDetails](waerror/nopaireddevicesdetails.md)
  The optional details describing the lack of paired devices.
### Checking for invalid device
- [case deviceInvalid(WAError.DeviceInvalidDetails)](waerror/deviceinvalid(_:).md)
  An error that occurs if your app specifies a paired device it doesn’t have access to.
- [WAError.DeviceInvalidDetails](waerror/deviceinvaliddetails.md)
  The optional details describing the device that’s invalid.
### Checking for unavailable device
- [case deviceNoLongerAvailable(WAError.DeviceNoLongerAvailableDetails)](waerror/devicenolongeravailable(_:).md)
  An error that occurs if a device is no longer available.
- [WAError.DeviceNoLongerAvailableDetails](waerror/devicenolongeravailabledetails.md)
  The optional details describing the unavailable device.
### Checking for connection
- [case connectionFailed(WAError.ConnectionFailedDetails)](waerror/connectionfailed(_:).md)
  An error that occurs if the service is unable to connect.
- [WAError.ConnectionFailedDetails](waerror/connectionfaileddetails.md)
  The optional details describing the failed connection.
### Checking for timeouts
- [case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)](waerror/connectionidletimeout(_:).md)
  An error that occurs due to an idle or unused connection.
- [case publisherTimeout(WAError.PublisherTimeoutDetails)](waerror/publishertimeout(_:).md)
  An error that occurs due to publisher timeout.
- [case subscriberTimeout(WAError.SubscriberTimeoutDetails)](waerror/subscribertimeout(_:).md)
  An error that occurs due to subscriber timeout.
- [WAError.ConnectionIdleTimeoutDetails](waerror/connectionidletimeoutdetails.md)
  The optional details describing the missing resources.
- [WAError.PublisherTimeoutDetails](waerror/publishertimeoutdetails.md)
  The optional details describing the timed out publisher.
- [WAError.SubscriberTimeoutDetails](waerror/subscribertimeoutdetails.md)
  The optional details describing the timed out subscriber.
### Checking for terminated connection
- [case connectionTerminated(WAError.ConnectionTerminatedDetails)](waerror/connectionterminated(_:).md)
  An error that occurs if the connection was terminated.
- [WAError.ConnectionTerminatedDetails](waerror/connectionterminateddetails.md)
  The optional details describing the terminated connection.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum NWError](../Network/NWError.md)
  The errors returned by objects in the Network framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror)*
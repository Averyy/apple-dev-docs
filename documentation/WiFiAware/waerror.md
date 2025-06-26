# WAError

**Framework**: Wi-Fi Aware  
**Kind**: enum

An error in Wi-Fi Aware.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum WAError
```

#### Overview

Wi-Fi Aware APIs may throw a [`WAError`](waerror.md) to indicate when an underlying issue occurs, with Network APIs throwing an `NWError` from [`Network.framework`](https://developer.apple.comhttps://developer.apple.com/documentation/Network). If the `NWError` occurs due to Wi-Fi Aware, then the `Network/NWError` property can provide access to additional information about the underlying Wi-Fi Aware error.

## Topics

### Checking for general errors
- [case error(WAError.ErrorDetails)](waerror/error(_:).md)
  A general error.
- [WAError.ErrorDetails](waerror/errordetails.md)
  The optional details describing the error.
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
  An error that occurs if your app didn’t declared the necessary services.
- [WAError.ServiceNotDeclaredDetails](waerror/servicenotdeclareddetails.md)
  The optional details that describe the app service wasn’t declared.
### Checking for service already in use
- [case serviceAlreadySubscribing(WAError.ServiceAlreadySubscribingDetails)](waerror/servicealreadysubscribing(_:).md)
  An error that occurs if the system can’t create a new subscriber or browser.
- [WAError.ServiceAlreadySubscribingDetails](waerror/servicealreadysubscribingdetails.md)
  The optional details describing the service that’s subscribing.
- [case serviceAlreadyPublishing(WAError.ServiceAlreadyPublishingDetails)](waerror/servicealreadypublishing(_:).md)
  An error that occurs if the system can’t create a new publisher or listener.
- [WAError.ServiceAlreadyPublishingDetails](waerror/servicealreadypublishingdetails.md)
  The optional details describing the service that’s publishing.
### Checking if paired devices are present or specified
- [case noPairedDevices(WAError.NoPairedDevicesDetails)](waerror/nopaireddevices(_:).md)
  An error that occurs if your app doesn’t have access to any paired devices.
- [WAError.NoPairedDevicesDetails](waerror/nopaireddevicesdetails.md)
  The optional details describing the lack of paired devices.
### Checking for invalid device
- [case deviceInvalid(WAError.DeviceInvalidDetails)](waerror/deviceinvalid(_:).md)
  An error that occurs if your app specifies a paired device to which it doesn’t have access.
- [WAError.DeviceInvalidDetails](waerror/deviceinvaliddetails.md)
  The optional details describing the device that’s invalid.
### Checking for unavailable device
- [case deviceNoLongerAvailable(WAError.DeviceNoLongerAvailableDetails)](waerror/devicenolongeravailable(_:).md)
  An error that occurs if a device is out of range or no longer available.
- [WAError.DeviceNoLongerAvailableDetails](waerror/devicenolongeravailabledetails.md)
  The optional details describing the lost device.
### Checking for connection
- [case connectionFailed(WAError.ConnectionFailedDetails)](waerror/connectionfailed(_:).md)
  An error that occurs if the service is unable to connect.
- [WAError.ConnectionFailedDetails](waerror/connectionfaileddetails.md)
  The optional details describing the failed connection.
### Checking for connection timeouts
- [case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)](waerror/connectionidletimeout(_:).md)
  An error that occurs due to an idle or unused connection.
- [WAError.ConnectionIdleTimeoutDetails](waerror/connectionidletimeoutdetails.md)
  The optional details describing the missing resources.
### Creating an error
- [init(from: any Decoder) throws](waerror/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Generating structures
- [WAError.ConnectionTerminatedDetails](waerror/connectionterminateddetails.md)
  The optional details describing the terminated connection.
- [WAError.PublisherTimeoutDetails](waerror/publishertimeoutdetails.md)
  The optional details describing the timed out publisher.
- [WAError.SubscriberTimeoutDetails](waerror/subscribertimeoutdetails.md)
  The optional details describing the timed-out subscriber.
### Generating enumeration cases
- [case connectionTerminated(WAError.ConnectionTerminatedDetails)](waerror/connectionterminated(_:).md)
  An error that occurs if someone terminates the connection.
- [case publisherTimeout(WAError.PublisherTimeoutDetails)](waerror/publishertimeout(_:).md)
  An error that occurs due to publisher timeout.
- [case subscriberTimeout(WAError.SubscriberTimeoutDetails)](waerror/subscribertimeout(_:).md)
  An error that occurs due to subscriber timeout.
### Structures
- [WAError.EntitlementMissingDetails](waerror/entitlementmissingdetails.md)
  The optional details describing the missing entitlement.
### Enumeration Cases
- [case entitlementMissing(WAError.EntitlementMissingDetails)](waerror/entitlementmissing(_:).md)
  An error that occurs if your App is missing the entitlement needed for the requested operation.
### Instance Methods
- [func encode(to: any Encoder) throws](waerror/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Error Implementations](waerror/error-implementations.md)
- [LocalizedError Implementations](waerror/localizederror-implementations.md)

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
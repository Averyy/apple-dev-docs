# WAPairedDevice

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

A known Wi-Fi Aware device that your app can connect to.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct WAPairedDevice
```

## Overview

Your app may request the system securely pair and grant access to remote devices. Use [AccessorySetupKit](../AccessorySetupKit/AccessorySetupKit.md) or [DeviceDiscoveryUI](../DeviceDiscoveryUI/DeviceDiscoveryUI.md) to add the devices to the set of `WAPairedDevice.Devices` that your app may connect to on-demand. The list of paired devices can change over time as a person adds and removes devices from the system.

## Topics

### Selecting from your app’s paired devices
- [WAPairedDevice.Devices](./wapaireddevice/devices.md)
  A dictionary holding a snapshot of currently paired devices accessible and known to your app.
- [static var allDevices: WAPairedDevice.DevicesSequence](./wapaireddevice/alldevices.md)
  Provides a snapshot of all the paired devices known to your app.
- [static func allDevices(matching: Predicate<WAPairedDevice>) -> WAPairedDevice.DevicesSequence](./wapaireddevice/alldevices%28matching%29.md)
  Provides a snapshot of all the paired devices known to your app.
- [WAPairedDevice.DevicesSequence](./wapaireddevice/devicessequence.md)
  A sequence that vends updates to a paired device list, as the list changes.
### Getting the app-specific identifier
- [WAPairedDevice.ID](./wapaireddevice/id-swift.typealias.md)
  A type of value that uniquely identifies the paired device.
- [let id: WAPairedDevice.ID](./wapaireddevice/id-swift.property.md)
  A stable ID that you can use to uniquely identify a device.
### Getting the configured device name
- [let name: String?](./wapaireddevice/name.md)
  The user-provided name of the device as a string, or `nil` if not available.
### Getting pairing-related device data
- [let pairingInfo: WAPairedDevice.PairingInfo?](./wapaireddevice/pairinginfo-swift.property.md)
  The unauthenticated information provided by the device before a person pairs it for the first time.
- [WAPairedDevice.PairingInfo](./wapaireddevice/pairinginfo-swift.struct.md)
  A collection of unauthenticated information the system receives from a device before it’s paired for the first time.
### Getting a string description
- [var description: String](./wapaireddevice/description.md)
  A string description of the publisher.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Paired devices
- [WAPairedDevice.Devices](./wapaireddevice/devices.md)
  A dictionary holding a snapshot of currently paired devices accessible and known to your app.
- [WAPairedDevice.DevicesSequence](./wapaireddevice/devicessequence.md)
  A sequence that vends updates to a paired device list, as the list changes.
- [WAPairedDevice.PairingInfo](./wapaireddevice/pairinginfo-swift.struct.md)
  A collection of unauthenticated information the system receives from a device before it’s paired for the first time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice)*
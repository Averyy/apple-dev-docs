# allDevices(matching:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Provides a snapshot of all the paired devices known to your app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static func allDevices(matching: Predicate<WAPairedDevice>) -> WAPairedDevice.DevicesSequence
```

#### Return Value

A new [`WAPairedDevice.DevicesSequence`](wapaireddevice/devicessequence.md) that returns [`WAPairedDevice.Devices`](wapaireddevice/devices.md) elements holding a snapshot of the currently paired devices known to your app.

#### Discussion

This method gets an `AsyncSequence` that provides snapshots of all [`WAPairedDevice.Devices`](wapaireddevice/devices.md) currently paired and known to your app that match the provided predicate, and provides updates when the snapshot of [`WAPairedDevice.Devices`](wapaireddevice/devices.md) matching that predicate changes. The sequence outputs an empty dictionary if there are no paired devices matching the predicate that are known to your app, or if a person removes all of your app’s matching paired devices.

You can select the set of `Devices` matching a filter from this property using the code below:

```swift
let filter = #Predicate<WAPairedDevice> { $0.pairingInfo?.vendorName.starts(with: "Example Inc") ?? false }

// Get a snapshot of all paired devices at the current moment.
guard let devices = try await WAPairedDevice.allDevices(matching:filter).current() { return }

// Get a snapshot of all paired devices at the current moment, and get a new snapshot each time a device is added, changed, or removed.
for try await devices in WAPairedDevice.allDevices(matching:filter) {
	// Process update.
}
```

## Parameters

- `matching`: The predicate that filters the devices. The system only provides updates for devices matching this predicate.

## See Also

- [WAPairedDevice.Devices](wapaireddevice/devices.md)
  A dictionary holding a snapshot of currently paired devices accessible and known to your app.
- [static var allDevices: WAPairedDevice.DevicesSequence](wapaireddevice/alldevices.md)
  Provides a snapshot of all the paired devices known to your app.
- [WAPairedDevice.DevicesSequence](wapaireddevice/devicessequence.md)
  A sequence that vends updates to a paired device list, as the list changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/alldevices(matching:))*
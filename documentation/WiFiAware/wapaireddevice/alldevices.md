# allDevices

**Framework**: Wi-Fi Aware  
**Kind**: property

Provides a snapshot of all the paired devices known to your app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static var allDevices: WAPairedDevice.DevicesSequence { get }
```

## Mentions

- [Connecting devices for peer-to-peer Wi-Fi](connecting-paired-devices.md)

#### Return Value

A new [`WAPairedDevice.DevicesSequence`](wapaireddevice/devicessequence.md) that returns [`WAPairedDevice.Devices`](wapaireddevice/devices.md) elements holding a snapshot of the currently paired devices known to the app.

#### Discussion

This property gets an `AsyncSequence` and provides updates with a new [`WAPairedDevice.Devices`](wapaireddevice/devices.md) snapshot when the set of paired devices known to your app changes. The sequence outputs an empty dictionary if there are no paired devices known to your app, or if a person removes all of your app’s paired devices.

You can select the set of `Devices` from this property using the following code snippet:

```swift
// Get a snapshot of all paired devices at the current moment.
guard let devices = try await WAPairedDevice.allDevices.current() { return }

// Get a snapshot of all paired devices at the current moment, and a new snapshot each time a device is added, changed, or removed.
for try await devices in WAPairedDevice.allDevices {
	// Process update.
}
```

## See Also

- [WAPairedDevice.Devices](wapaireddevice/devices.md)
  A dictionary holding a snapshot of currently paired devices accessible and known to your app.
- [static func allDevices(matching: Predicate<WAPairedDevice>) -> WAPairedDevice.DevicesSequence](wapaireddevice/alldevices(matching:).md)
  Provides a snapshot of all the paired devices known to your app.
- [WAPairedDevice.DevicesSequence](wapaireddevice/devicessequence.md)
  A sequence that vends updates to a paired device list, as the list changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/alldevices)*
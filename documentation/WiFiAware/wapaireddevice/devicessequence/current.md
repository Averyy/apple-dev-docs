# current()

**Framework**: Wi-Fi Aware  
**Kind**: method

Fetches a one-time snapshot of all paired devices that are currently known and  accessible to your app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func current() async throws -> WAPairedDevice.DevicesSequence.Element?
```

#### Return Value

A single [`WAPairedDevice.Devices`](wapaireddevice/devices.md) element holding a snapshot of the currently paired devices known to the app, or `nil` if the sequence has no more values.

#### Discussion

The [`WAPairedDevice.Devices`](wapaireddevice/devices.md) dictionary holds a snapshot of the currently paired devices that are known and accessible to your app. This method returns an empty dictionary if there are no paired devices known to your app. The following code is an example of how to use `current()` to return the first `Devices` snapshot in the sequence:

```swift
guard let devices = try await WAPairedDevice.allDevices.current() { return }
```

Don’t use this method if you need to monitor for changes to the paired device list, or change app behavior in response to such changes. Instead, use

```swift
for try await devices in WAPairedDevice.allDevices {
	// Process the devices.
}
```

> **Note**: An error if the system can’t read the sequence, or if the app isn’t permitted to access Wi-Fi Aware devices.

> **Note**: [`allDevices`](wapaireddevice/alldevices.md)

> **Note**: [`allDevices(matching:)`](wapaireddevice/alldevices(matching:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence/current())*
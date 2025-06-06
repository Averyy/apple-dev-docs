# Connecting to Bluetooth Peripherals in Swift Playgrounds

**Framework**: Playground Bluetooth

Scan for peripherals and display them in your playground's live view.

#### Overview

Playgrounds use Bluetooth to connect to nearby peripherals to send and receive commands or data. You can incorporate periperals into your playground to have your users learn programming concepts by interacting with real-world objects.

##### 3030120

You use a [`PlaygroundBluetoothCentralManager`](playgroundbluetoothcentralmanager.md) to scan for and connect to nearby Bluetooth peripherals. It automatically stores the ID of the most recently connected peripheral. The example below scans for all kinds of peripherals by passing `nil` to the initializer for the [`PlaygroundBluetoothCentralManagerDelegate`](playgroundbluetoothcentralmanagerdelegate.md).

```swift
let managerDelegate: PlaygroundBluetoothCentralManagerDelegate = <# manager delegate instance #>
 
let manager = PlaygroundBluetoothCentralManager(services: nil)
manager.delegate = managerDelegate
```

Once you determine which Bluetooth services your playground page requires, instead of passing `nil` for those services, pass an array of [`CBUUID`](https://developer.apple.com/documentation/corebluetooth/cbuuid) instances.

##### 3030119

You use a [`PlaygroundBluetoothConnectionView`](playgroundbluetoothconnectionview.md) to display status information about nearby peripherals. The example belows shows how to configure and place a connection view on a playground page.

```swift
let viewDelegate: PlaygroundBluetoothConnectionViewDelegate = <# view delegate instance #>
let connectionView = PlaygroundBluetoothConnectionView(centralManager: manager, delegate: viewDelegate)
connectionView.dataSource = viewDelegate
 
// Place the connection view within the rest of your page's content.
let page: UIViewController & PlaygroundLiveViewSafeAreaContainer = <# playground page view controller #>
page.view.addSubview(connectionView)
 
// Position the connection view in the top right corner.
connectionView.topAnchor.constraint(equalTo: page.liveViewSafeAreaGuide.topAnchor, constant: 20).isActive = true
connectionView.trailingAnchor.constraint(equalTo: page.liveViewSafeAreaGuide.trailingAnchor, constant: -20).isActive = true
 
PlaygroundPage.current.liveView = page
```

> ❗ **Important**: Always use the system-provided [`PlaygroundBluetoothConnectionView`](playgroundbluetoothconnectionview.md) to display connection information for peripherals. Doing so helps provide a consistent experience for people who also use playground books created by others.

Always use the system-provided [`PlaygroundBluetoothConnectionView`](playgroundbluetoothconnectionview.md) to display connection information for peripherals. Doing so helps provide a consistent experience for people who also use playground books created by others.

## See Also

- [class PlaygroundBluetoothCentralManager](playgroundbluetoothcentralmanager.md)
  A streamlined interface for connecting the central manager for the current playground page to nearby Bluetooth peripherals.
- [protocol PlaygroundBluetoothCentralManagerDelegate](playgroundbluetoothcentralmanagerdelegate.md)
  A delegate you use to respond to peripheral discovery and manage the lifecycle of connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/connecting_to_bluetooth_peripherals_in_swift_playgrounds)*
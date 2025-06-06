# Playground Bluetooth

**Framework**: Playground Bluetooth

Display and manage connections to Bluetooth peripherals in Swift Playgrounds.

**Availability**:
- Swift Playgrounds 2.0+

#### Overview

The PlaygroundBluetooth framework provides a common interface that you use to display and manage connections to Bluetooth peripherals from the framework’s central manager within a playground page.

![A screenshot showing a PlaygroundBluetoothConnectionView instance in the upper right corner. The connection view is displaying three peripherals; one is marked as connected.](https://docs-assets.developer.apple.com/published/4be3ab3166/3030117@2x.png)

## Topics

### Peripheral Connection
- [Connecting to Bluetooth Peripherals in Swift Playgrounds](connecting_to_bluetooth_peripherals_in_swift_playgrounds.md)
  Scan for peripherals and display them in your playground's live view.
- [class PlaygroundBluetoothCentralManager](playgroundbluetoothcentralmanager.md)
  A streamlined interface for connecting the central manager for the current playground page to nearby Bluetooth peripherals.
- [protocol PlaygroundBluetoothCentralManagerDelegate](playgroundbluetoothcentralmanagerdelegate.md)
  A delegate you use to respond to peripheral discovery and manage the lifecycle of connections.
### Peripheral Display
- [class PlaygroundBluetoothConnectionView](playgroundbluetoothconnectionview.md)
  A view that displays the connection status of a peripheral to the central manager for the current page and manages connections to other peripherals.
- [protocol PlaygroundBluetoothConnectionViewDelegate](playgroundbluetoothconnectionviewdelegate.md)
  A delegate you use to respond to user- and system-initiated interactions with the central manager’s connection view.
- [protocol PlaygroundBluetoothConnectionViewDataSource](playgroundbluetoothconnectionviewdatasource.md)
  The protocol you adopt to display an available peripheral in a playground page’s connection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth)*
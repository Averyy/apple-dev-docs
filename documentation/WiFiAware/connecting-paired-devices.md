# Connecting devices for peer-to-peer Wi-Fi

**Framework**: Wi-Fi Aware  
**Role**: Article

Make outgoing and accept incoming secure connections with paired devices.

## Overview

With the Wi-Fi Aware™ technology, your app can securely establish peer-to-peer (P2P) connections between Wi-Fi devices. By using the Wi-Fi Aware framework, devices can discover, pair, and communicate with other nearby devices without an internet connection or access point.

For your app to pair devices, or ask the person using your app for access to existing devices, you can use either of the following two methods:

- [DeviceDiscoveryUI](../DeviceDiscoveryUI/DeviceDiscoveryUI.md): Pair any kind of device for device-to-device and app-to-app use cases, such as file transfer and media streaming.
- [AccessorySetupKit](../AccessorySetupKit/AccessorySetupKit.md): Pair a person’s personal hardware accessory with the accessory’s companion app, such as for setup and accessory management.

After a person pairs a device or grants your app access to a device, the system adds the device to your app’s [`WAPairedDevice.Devices`](./wapaireddevice/devices.md) collection, which is accessible through the [`allDevices`](./wapaireddevice/alldevices.md) APIs.

### Connect paired devices

After your app pairs devices, it can initiate secure peer-to-peer Wi-Fi connections between those devices on demand. The Wi-Fi Aware framework integrates with the [Network](../Network/Network.md) framework to provide Wi-Fi Aware connections and related functionality, extending several common networking primitives:

- [`NetworkBrowser`](../Network/networkbrowser.md) subscribes to Wi-Fi Aware services on paired devices, and makes outgoing secure connections to them.
- [`NetworkListener`](../Network/networklistener.md) publishes Wi-Fi Aware services to paired devices, and accepts incoming secure connections from them.
- [`NetworkConnection`](../Network/networkconnection.md) opens a secure, high-performance data connection to Wi-Fi Aware devices.
- [`NWParameters`](../Network/nwparameters.md) configures Wi-Fi Aware parameters.
- [`NWPath`](../Network/nwpath.md) fetches Wi-Fi Aware connection statuses and performance metrics.
- [`NWError`](../Network/nwerror.md) fetches Wi-Fi Aware error statuses.

### Create a listener to publish

The following code example creates a `NetworkListener` that publishes the `_example-service._tcp` service over Wi-Fi Aware, and accepts incoming connections from the specified paired devices:

```swift
// Specifies a service.
extension WAPublishableService {
    public static var exampleService: WAPublishableService {
        allServices["_example-service._tcp"]!
    }
}

// Selects devices from the list of the example app's paired devices.
let devices = #Predicate<WAPairedDevice> { $0.name?.starts(with: "My Device") ?? false }

// Constructs a `NetworkListener` to publish the service and accept connections from the selected devices.
try await NetworkListener(for:
    .wifiAware(.connecting(to: .exampleService, from: .matching(devices))),
using: {
    TLS()
})
.onStateUpdate { listener, state in
    // Processes state updates.
}
.run { connection in
    // Handle incoming connections.
}
```

### Create a browser to subscribe

The following code example creates a `NetworkBrowser` that subscribes for the `_example-service._tcp` service over Wi-Fi Aware, and provides browse results that the system can use to make outgoing connections to the specified paired devices:

```swift
// Specifies a service.
extension WASubscribableService {
    public static var exampleService: WASubscribableService {
        allServices["_example-service._tcp"]!
    }
}

// Selects `devices` from the list of all paired devices.
let devices = #Predicate<WAPairedDevice> { $0.name?.starts(with: "My Device") ?? false }

// Constructs a `NetworkBrowser` to subscribe for the service on the selected devices. 
let browser = NetworkBrowser(
    for:
        .wifiAware( .connecting(to: .matching(devices),  from: .exampleService))
)
.onStateUpdate { browser, state in
    // Processes state updates.
}

// Run the browser and get discovered endpoints
let endpoint = try await browser.run { waEndpoints in
    // Handle discovered endpoints.
    // Return .finish(endpoint) once the desired endpoint(s) are discovered or .continue to keep the browser active.
}
```

### Make a connection

The following code example creates a `NetworkConnection` to a discovered Wi-Fi Aware endpoint:

```swift
// On the browser device, construct a `NetworkConnection` to make a connection to one of the discovered endpoints from the browse operation.
let connection = NetworkConnection(
    to:
        endpoint,
    using: {
        TLS()
    }
).onStateUpdate { connection, state in
    // Processes state updates.
}

// The run closure on the `NetworkListener` device receives the incoming connection.
```

### Monitor connection performance

The following code example gets the Wi-Fi Aware performance report from the current path of a connection.

```swift
if let wifiAwarePath = try await connection.currentPath?.wifiAware {
    let performanceReport = wifiAwarePath.performance

    // Use the performance report.
}
```

### Get Wi-Fi Aware errors

The following code example gets the Wi-Fi Aware specific error code from the [`NWError`](../Network/nwerror.md) reported by the Network framework as part of the state updates provided for the `NetworkBrowser`, `NetworkListener` and `NetworkConnection` instances.

```swift
.onStateUpdate { _, state in
    switch state {
    ...

    case .failed(let nwError): let wifiAwareError = error.wifiAware
    default: break
    }
}
```

## See Also

### Essentials
- [Building peer-to-peer apps](./building-peer-to-peer-apps.md)
  Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [Adopting Wi-Fi Aware](./adopting-wi-fi-aware.md)
  Add entitlements and declare your app’s services.
- [com.apple.developer.wifi-aware](../BundleResources/entitlements/com.apple.developer.wifi-aware.md)
  The entitlement the system requires for an app to use the Wi-Fi Aware framework.
- [WiFiAwareServices](../BundleResources/information-property-list/wifiawareservices.md)
  Dictionaries of Wi-Fi Aware services that the app can publish or subscribe to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/connecting-paired-devices)*
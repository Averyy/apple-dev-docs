# Wi-Fi Aware

**Framework**: Wi-Fi Aware  
**Kind**: module

Securely pair and connect to external devices over peer-to-peer Wi-Fi.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

#### Overview

The Wi-Fi Aware™ technology (also known as Neighbor Awareness Networking or NAN) is a Wi-Fi Alliance™ standard specification that enables devices to securely discover, pair, and communicate with nearby devices without an internet connection or access point. Your app can use the Wi-Fi Aware framework to connect with Wi-Fi Aware certified accessories. The framework offers a secure and standardized way to establish peer-to-peer (P2P) connections between Wi-Fi devices, providing networking capabilities such as:

- High-bandwidth and low-latency data transfers
- Connections to paired devices that are authenticated and encrypted at the Wi-Fi layer
- Simultaneous connections to multiple Wi-Fi Aware devices
- Simultaneous use of Wi-Fi Aware devices and a Wi-Fi infrastructure network
- Fully peer-to-peer topology, allowing peers to come and go without breaking connections to other peers

The Wi-Fi Aware technology works without the need for Wi-Fi infrastructure networks, cellular links, internet connections, or cloud servers. Your app can pair Wi-Fi Aware devices using [`AccessorySetupKit`](https://developer.apple.comhttps://developer.apple.com/documentation/accessorysetupkit/) or [`DeviceDiscoveryUI`](https://developer.apple.comhttps://developer.apple.com/documentation/devicediscoveryui). When paired, your app can create secure, authenticated, and encrypted peer-to-peer connections between paired devices on-demand, using the Wi-Fi Aware and [`Network`](https://developer.apple.comhttps://developer.apple.com/documentation/Network) frameworks.

> ❗ **Important**: The following Apple devices support the Wi-Fi Aware framework: - iPhone 12 and later
- iPad (10th generation) and later
- iPad Air (4th generation) and later
- iPad Pro 11-inch (3rd generation) and later
- iPad Pro 12.9-inch (5th generation) and later
- iPad mini (6th generation) and later

## Topics

### Essentials
- [Building peer-to-peer apps](building-peer-to-peer-apps.md)
  Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [Connecting devices for peer-to-peer Wi-Fi](connecting-paired-devices.md)
  Make outgoing and accept incoming secure connections with paired devices.
- [Adopting Wi-Fi Aware](adopting-wi-fi-aware.md)
  Add entitlements and declare your app’s services.
- [com.apple.developer.wifi-aware](../BundleResources/Entitlements/com.apple.developer.wifi-aware.md)
  The entitlement the system requires for an app to use the Wi-Fi Aware framework.
- [WiFiAwareServices](../BundleResources/Information-Property-List/WiFiAwareServices.md)
  Dictionaries of Wi-Fi Aware services that the app can publish or subscribe to.
### Host capabilities
- [struct WACapabilities](wacapabilities.md)
  A structure that checks the host device’s supported features and capabilities.
- [WACapabilities.Feature](wacapabilities/feature.md)
  Features that your app’s current host device can support.
### Services to discover
- [protocol WAService](waservice.md)
  A protocol that defines a service that a device can publish or subscribe to.
- [struct WASubscribableService](wasubscribableservice.md)
  A service your app discovers on remote devices and can connect to.
- [struct WAPublishableService](wapublishableservice.md)
  A service, hosted by your app, that remote devices can connect to.
### Paired devices
- [struct WAPairedDevice](wapaireddevice.md)
  A known Wi-Fi Aware device that your app can connect to.
- [WAPairedDevice.Devices](wapaireddevice/devices.md)
  A dictionary holding a snapshot of currently paired devices accessible and known to your app.
- [WAPairedDevice.DevicesSequence](wapaireddevice/devicessequence.md)
  A sequence that vends updates to a paired device list, as the list changes.
- [WAPairedDevice.PairingInfo](wapaireddevice/pairinginfo-swift.struct.md)
  A collection of unauthenticated information the system receives from a device before it’s paired for the first time.
### Subscriber
- [struct WASubscriberBrowser](wasubscriberbrowser.md)
  The structure that configures a network browser to subscribe to a Wi-Fi Aware service and make outgoing connections to paired devices.
- [WASubscriberBrowser.Action](wasubscriberbrowser/action.md)
  The structure that configures the Wi-Fi Aware subscriber operation the network browser performs.
- [WASubscriberBrowser.Devices](wasubscriberbrowser/devices.md)
  The structure that determines the devices to connect to.
### Publisher
- [struct WAPublisherListener](wapublisherlistener.md)
  Configures a network listener to publish a service over Wi-Fi Aware and accept incoming connections from paired devices.
- [WAPublisherListener.Action](wapublisherlistener/action.md)
  The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.
- [WAPublisherListener.Devices](wapublisherlistener/devices.md)
  The structure that determines the devices to connect to.
- [WAPublisherListener.DatapathParameters](wapublisherlistener/datapathparameters.md)
  The parameter that sets the initial Wi-Fi Aware data path configuration for any devices that are connected.
### Parameters
- [final class NWParameters](../Network/NWParameters.md)
  An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [struct NWParametersBuilder<Top, each P> where Top : NetworkProtocolOptions, repeat each P : NetworkProtocolOptions](../Network/NWParametersBuilder.md)
- [struct WAParameters](waparameters.md)
  Parameters configuring a Wi-Fi Aware data path connection.
### Connections
- [struct WAEndpoint](waendpoint.md)
  The endpoint of a Wi-Fi Aware connection.
### Connection performance
- [struct NWPath](../Network/NWPath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [struct WAPath](wapath.md)
  A representation of the current Wi-Fi Aware path.
- [enum WAPerformanceMode](waperformancemode.md)
  The performance mode that indicates what performance criterion to prioritize.
- [enum WAAccessCategory](waaccesscategory.md)
  The underling quality-of-service (QoS) the Wi-Fi layer uses to transmit data packets from a connection over the air.
- [struct WAPerformanceReport](waperformancereport.md)
  The current performance state of the data path.
### Errors
- [enum NWError](../Network/NWError.md)
  The errors returned by objects in the Network framework.
- [enum WAError](waerror.md)
  An error in Wi-Fi Aware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WiFiAware)*
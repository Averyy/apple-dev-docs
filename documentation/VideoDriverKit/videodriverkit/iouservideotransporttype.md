# IOUserVideoTransportType

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoTransportType : uint32_t;
```

#### Overview

Commonly used values for transport types

The transport type ID returned when a device doesn’t provide a transport type.

The transport type ID for VideoDevices built into the system.

The transport type ID for VideoDevices connected via the PCI bus.

The transport type ID for VideoDevices connected via USB.

The transport type ID for VideoDevices connected via FireWire.

The transport type ID for VideoDevices connected via Bluetooth.

The transport type ID for VideoDevices connected via Bluetooth Low Energy.

The transport type ID for VideoDevices connected via HDMI.

The transport type ID for VideoDevices connected via DisplayPort.

The transport type ID for VideoDevices connected via AirPlay.

The transport type ID for VideoDevices connected via AVB.

The transport type ID for VideoDevices connected via Thunderbolt.

## Topics

### Protocol-based transport types
- [PCI](videodriverkit/iouservideotransporttype/pci.md)
- [USB](videodriverkit/iouservideotransporttype/usb.md)
- [FireWire](videodriverkit/iouservideotransporttype/firewire.md)
- [Bluetooth](videodriverkit/iouservideotransporttype/bluetooth.md)
- [BluetoothLE](videodriverkit/iouservideotransporttype/bluetoothle.md)
- [HDMI](videodriverkit/iouservideotransporttype/hdmi.md)
- [DisplayPort](videodriverkit/iouservideotransporttype/displayport.md)
- [AirPlay](videodriverkit/iouservideotransporttype/airplay.md)
- [AVB](videodriverkit/iouservideotransporttype/avb.md)
- [Thunderbolt](videodriverkit/iouservideotransporttype/thunderbolt.md)
### Other transport types
- [Unknown](videodriverkit/iouservideotransporttype/unknown.md)
- [BuiltIn](videodriverkit/iouservideotransporttype/builtin.md)

## See Also

- [GetTransportType](iouservideobox/gettransporttype.md)
- [SetTransportType](iouservideobox/settransporttype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideotransporttype)*
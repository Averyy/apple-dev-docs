# IOUserVideoTransportType

**Framework**: VideoDriverKit  
**Kind**: enum  
**Role**: Enumeration

The transport type of a video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
enum IOUserVideoTransportType : uint32_t;
```

## Topics

### Protocol-based transport types
- [PCI](./iouservideotransporttype/pci.md)
  The transport type identifier for video devices connected via the PCI bus.
- [USB](./iouservideotransporttype/usb.md)
  The transport type identifier for video devices connected via USB.
- [FireWire](./iouservideotransporttype/firewire.md)
  The transport type identifier for video devices connected via FireWire.
- [Bluetooth](./iouservideotransporttype/bluetooth.md)
  The transport type identifier for video devices connected via Bluetooth Low Energy.
- [BluetoothLE](./iouservideotransporttype/bluetoothle.md)
  The transport type identifier for video devices connected via Bluetooth.
- [HDMI](./iouservideotransporttype/hdmi.md)
  The transport type identifier for video devices connected via HDMI.
- [DisplayPort](./iouservideotransporttype/displayport.md)
  The transport type identifier for video devices connected via DisplayPort.
- [AirPlay](./iouservideotransporttype/airplay.md)
  The transport type identifier for video devices connected via AirPlay.
- [AVB](./iouservideotransporttype/avb.md)
  The transport type identifier for video devices connected via AVB.
- [Thunderbolt](./iouservideotransporttype/thunderbolt.md)
  The transport type identifier for video devices connected via Thunderbolt.
### Other transport types
- [Unknown](./iouservideotransporttype/unknown.md)
  The transport type identifier returned when a device doesn’t provide a transport type.
- [BuiltIn](./iouservideotransporttype/builtin.md)
  The transport type identifier for video devices built into the system.

## See Also

### Working with transport types
- [GetTransportType](../iouservideobox/gettransporttype.md)
  Gets the transport type of the video box.
- [SetTransportType](../iouservideobox/settransporttype.md)
  Sets the transport type of the IOUserVideoBox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideotransporttype)*
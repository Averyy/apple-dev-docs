# IOUserVideoTransportType

**Framework**: VideoDriverKit  
**Kind**: enum

The transport type of a video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
enum IOUserVideoTransportType : uint32_t;
```

## Topics

### Protocol-based transport types
- [PCI](videodriverkit/iouservideotransporttype/pci.md)
  The transport type identifier for video devices connected via the PCI bus.
- [USB](videodriverkit/iouservideotransporttype/usb.md)
  The transport type identifier for video devices connected via USB.
- [FireWire](videodriverkit/iouservideotransporttype/firewire.md)
  The transport type identifier for video devices connected via FireWire.
- [Bluetooth](videodriverkit/iouservideotransporttype/bluetooth.md)
  The transport type identifier for video devices connected via Bluetooth Low Energy.
- [BluetoothLE](videodriverkit/iouservideotransporttype/bluetoothle.md)
  The transport type identifier for video devices connected via Bluetooth.
- [HDMI](videodriverkit/iouservideotransporttype/hdmi.md)
  The transport type identifier for video devices connected via HDMI.
- [DisplayPort](videodriverkit/iouservideotransporttype/displayport.md)
  The transport type identifier for video devices connected via DisplayPort.
- [AirPlay](videodriverkit/iouservideotransporttype/airplay.md)
  The transport type identifier for video devices connected via AirPlay.
- [AVB](videodriverkit/iouservideotransporttype/avb.md)
  The transport type identifier for video devices connected via AVB.
- [Thunderbolt](videodriverkit/iouservideotransporttype/thunderbolt.md)
  The transport type identifier for video devices connected via Thunderbolt.
### Other transport types
- [Unknown](videodriverkit/iouservideotransporttype/unknown.md)
  The transport type identifier returned when a device doesn’t provide a transport type.
- [BuiltIn](videodriverkit/iouservideotransporttype/builtin.md)
  The transport type identifier for video devices built into the system.

## See Also

- [GetTransportType](iouservideobox/gettransporttype.md)
  Gets the transport type of the video box.
- [SetTransportType](iouservideobox/settransporttype.md)
  Sets the transport type of the IOUserVideoBox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideotransporttype)*
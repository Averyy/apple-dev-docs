# USB

**Framework**: Kernel

Implement a driver that supports Universal Serial Bus (USB) devices.

#### Overview

Use kernel extensions to implement support for devices with real-time requirements, such as audio and video devices. 

> ❗ **Important**: For most types of USB drivers, Apple has deprecated the use of kernel extensions. Instead, create a DriverKit extension using [`USBDriverKit`](https://developer.apple.com/documentation/usbdriverkit).

This framework refers to the USB Implementers Forum (USB-IF) , Revision 1.0, September 22, 2017. You can view this specification and other referenced USB specifications at [`http://www.usb.org/`](https://developer.apple.comhttp://www.usb.org/).

## Topics

### Device Communication
- [Building a Simple USB Driver](hardware_families/usb/building_a_simple_usb_driver.md)
  Set up and load a driver that logs output to the Console app.
- [IOUSBHostIOSourceClientRecordLink](iousbhostiosourceclientrecordlink.md)
  A structure that represents a USB host input/output source client record entry.
- [IOUSBHostIOSourceClientRecordList](iousbhostiosourceclientrecordlist.md)
  A structure that represents a list of USB host input/output source client records.
### USB Specifications
- [IOUSBIsochronousFrame](iousbisochronousframe.md)
  A structure representing a single frame in an isochronous transfer.
- [USB Device Descriptors](hardware_families/usb/usb_device_descriptors.md)
  Structures and functions for working with device descriptors.
- [Additional Specifications](hardware_families/usb/additional_specifications.md)
  Structures related to hubs, devices, and endpoints.
### Actions
- [IOUSBCompletionAction](iousbcompletionaction.md)
  A function the system calls when the USB input/output request completes.
- [IOUSBCompletion](iousbcompletion.md)
  The structure that specifies the action to perform when the USB input/output request completes.
- [IOUSBHostBundledCompletion](iousbhostbundledcompletion.md)
  The structure that specifies the action to perform when a bulk USB input/output request completes.
- [IOUSBHostBundledCompletionAction](iousbhostbundledcompletionaction.md)
  The function description for a USB host bundled completion action.
- [IOUSBHostCompletion](iousbhostcompletion.md)
  The structure that specifies the action to perform when the USB input/output request completes.
- [IOUSBHostCompletionAction](iousbhostcompletionaction.md)
  The function description for a USB host completion action.
- [IOUSBHostIsochronousCompletion](iousbhostisochronouscompletion.md)
  A structure describing the completion callback for an asynchronous isochronous operation.
- [IOUSBHostIsochronousCompletionAction](iousbhostisochronouscompletionaction.md)
  The function description for a USB host isochronous completion action.
- [IOUSBIsocCompletion](iousbisoccompletion.md)
  A structure specifying the action to perform when an isochronous USB input/output operation completes.
- [IOUSBIsocCompletionAction](iousbisoccompletionaction.md)
  The function that executes when the isochronous USB input/output request completes.
- [IOUSBLowLatencyIsocCompletion](iousblowlatencyisoccompletion.md)
  The function that executes when the low-latency isochronous USB input/output request completes.
- [IOUSBLowLatencyIsocCompletionAction](iousblowlatencyisoccompletionaction.md)
  The function that excutes when the low-latency isochronous USB input/output request completes.
- [IOUSBCompletionActionWithTimeStamp](iousbcompletionactionwithtimestamp.md)
  The function that executes when the USB input/output request completes.
- [IOUSBCompletionWithTimeStamp](iousbcompletionwithtimestamp.md)
  A structure specifying action to perform when the USB input/output request completes.

## See Also

- [ATA](hardware_families/ata.md)
  Implement a driver that supports Advanced Technology Attachment (ATA) devices.
- [Bluetooth](hardware_families/bluetooth.md)
  Implement a driver that supports Bluetooth devices.
- [FireWire](hardware_families/firewire.md)
  Implement a driver that supports FireWire devices. 
- [PCI](hardware_families/pci.md)
  Implement a driver that supports Thunderbolt devices or PCI cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/usb)*
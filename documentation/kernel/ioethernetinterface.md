# IOEthernetInterface

**Framework**: Kernel  
**Kind**: cl

The Ethernet interface object.

**Availability**:
- macOS 10.6+ - Deprecated in 10.15.4

## Declaration

```swift
class IOEthernetInterface : IONetworkInterface
```

#### Overview

An Ethernet controller driver, that is a subclass of IOEthernetController, will instantiate an object of this class when the driver calls the attachInterface() method. This interface object will then vend an Ethernet interface to DLIL, and manage the connection between the controller driver and the upper networking layers. Drivers will seldom need to subclass IOEthernetInterface.

## Topics

### Miscellaneous
- [controllerDidChangePowerState](ioethernetinterface/1810626-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerDidOpen](ioethernetinterface/1810636-controllerdidopen.md)
  A notification that the interface has opened the network controller.
- [controllerWillChangePowerState](ioethernetinterface/1810670-controllerwillchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object is about to transition to a new power state.
- [controllerWillClose](ioethernetinterface/1810684-controllerwillclose.md)
  A notification that the interface will close the network controller.
- [free](ioethernetinterface/1810696-free.md)
  Frees the IOEthernetInterface instance.
- [getNamePrefix](ioethernetinterface/1810711-getnameprefix.md)
  Returns a string containing the prefix to use when creating a BSD name for this interface.
- [init](ioethernetinterface/1810722-init.md)
  Initializes an IOEthernetInterface instance.
- [performCommand](ioethernetinterface/1810736-performcommand.md)
  Handles an ioctl command sent to the Ethernet interface.
### Instance Variables
- [_reserved](ioethernetinterface/reserved.md)
### Instance Methods
- [- attachToDataLinkLayer](ioethernetinterface/1585552-attachtodatalinklayer.md)
- [- controllerDidChangePowerState](ioethernetinterface/1585555-controllerdidchangepowerstate.md)
- [- controllerDidOpen](ioethernetinterface/1585532-controllerdidopen.md)
- [- controllerWillChangePowerState](ioethernetinterface/1585542-controllerwillchangepowerstate.md)
- [- controllerWillClose](ioethernetinterface/1585544-controllerwillclose.md)
- [- disableFilter](ioethernetinterface/1585537-disablefilter.md)
- [- enableController](ioethernetinterface/1585547-enablecontroller.md)
- [- enableFilter](ioethernetinterface/1585560-enablefilter.md)
- [- feedPacketInputTap](ioethernetinterface/1585536-feedpacketinputtap.md)
- [- feedPacketOutputTap](ioethernetinterface/1585540-feedpacketoutputtap.md)
- [- free](ioethernetinterface/1585566-free.md)
- [- getFilters](ioethernetinterface/1585551-getfilters.md)
- [- getMetaClass](ioethernetinterface/1585558-getmetaclass.md)
- [- getNamePrefix](ioethernetinterface/1585553-getnameprefix.md)
- [- init](ioethernetinterface/1585541-init.md)
- [- initIfnetParams](ioethernetinterface/1585559-initifnetparams.md)
- [- inputEvent](ioethernetinterface/1585535-inputevent.md)
- [- performCommand](ioethernetinterface/1585549-performcommand.md)
- [- reportInterfaceWakeFlags](ioethernetinterface/1585562-reportinterfacewakeflags.md)
- [- setFilters](ioethernetinterface/1585534-setfilters.md)
- [- setupMulticastFilter](ioethernetinterface/1585561-setupmulticastfilter.md)
- [- syncSIOCADDMULTI](ioethernetinterface/1585550-syncsiocaddmulti.md)
- [- syncSIOCDELMULTI](ioethernetinterface/1585543-syncsiocdelmulti.md)
- [- syncSIOCGIFDEVMTU](ioethernetinterface/1585548-syncsiocgifdevmtu.md)
- [- syncSIOCSIFADDR](ioethernetinterface/1585557-syncsiocsifaddr.md)
- [- syncSIOCSIFCAP](ioethernetinterface/2934826-syncsiocsifcap.md)
- [- syncSIOCSIFFLAGS](ioethernetinterface/1585567-syncsiocsifflags.md)
- [- syncSIOCSIFLLADDR](ioethernetinterface/1585545-syncsiocsiflladdr.md)
- [- syncSIOCSIFMTU](ioethernetinterface/1585546-syncsiocsifmtu.md)
- [- willTerminate](ioethernetinterface/1585539-willterminate.md)
### Type Methods
- [+ enableFilter_Wrapper](ioethernetinterface/1585556-enablefilter_wrapper.md)
- [+ handleEthernetInputEvent](ioethernetinterface/1585533-handleethernetinputevent.md)
- [+ performGatedCommand](ioethernetinterface/1585565-performgatedcommand.md)

## Relationships

### Inherits From
- [IONetworkInterface](ionetworkinterface.md)

## See Also

- [IOUSBDevice](iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](1575304-ioofpathmatching.md)
- [IOUSBHostInterface](iousbhostinterface.md)
- [IOUSBHostDevice](iousbhostdevice.md)
- [IOUSBHostPipe](iousbhostpipe.md)
- [IOUSBHostIOSource](iousbhostiosource.md)
- [IOUSBHostStream](iousbhoststream.md)
- [IOHIDEventDriver](iohideventdriver.md)
- [IOHIDEventService](iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDInterface](iohidinterface.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDSystem](iohidsystem.md)
- [IOHIKeyboardMapper](iohikeyboardmapper.md)
- [IOHIKeyboard](iohikeyboard.md)
- [IOHIPointing](iohipointing.md)
- [IOHIDevice](iohidevice.md)
- [IOHIDElement](iohidelement.md)
- [IOHIDWorkLoop](iohidworkloop.md)
- [IOEthernetController](ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetinterface)*
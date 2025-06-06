# IOUSBHostInterface

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.11+ - Deprecated in 10.15.4

## Declaration

```swift
class IOUSBHostInterface : IOUSBInterface
```

## Topics

### Instance Methods
- [- Close](iousbhostinterface/3294653-close.md)
- [- Close_Impl](iousbhostinterface/3294654-close_impl.md)
- [- CopyDevice](iousbhostinterface/3294656-copydevice.md)
- [- CopyDevice_Impl](iousbhostinterface/3294657-copydevice_impl.md)
- [- CopyPipe](iousbhostinterface/3294659-copypipe.md)
- [- CopyPipe_Impl](iousbhostinterface/3294660-copypipe_impl.md)
- [- Dispatch](iousbhostinterface/3294662-dispatch.md)
- [- GetFrameNumber](iousbhostinterface/3438057-getframenumber.md)
- [- GetFrameNumber_Impl](iousbhostinterface/3294663-getframenumber_impl.md)
- [- GetIdlePolicy](iousbhostinterface/3294665-getidlepolicy.md)
- [- GetIdlePolicy_Impl](iousbhostinterface/3294666-getidlepolicy_impl.md)
- [- GetPortStatus](iousbhostinterface/3294668-getportstatus.md)
- [- GetPortStatus_Impl](iousbhostinterface/3294669-getportstatus_impl.md)
- [- Open](iousbhostinterface/3294671-open.md)
- [- Open_Impl](iousbhostinterface/3294672-open_impl.md)
- [- SelectAlternateSetting](iousbhostinterface/3294674-selectalternatesetting.md)
- [- SelectAlternateSetting_Impl](iousbhostinterface/3294675-selectalternatesetting_impl.md)
- [- SetIdlePolicy](iousbhostinterface/3294677-setidlepolicy.md)
- [- SetIdlePolicy_Impl](iousbhostinterface/3294678-setidlepolicy_impl.md)
- [- abortDeviceRequests](iousbhostinterface/1522056-abortdevicerequests.md)
- [- attach](iousbhostinterface/1522041-attach.md)
- [- close](iousbhostinterface/1522083-close.md)
- [- closeGated](iousbhostinterface/1522061-closegated.md)
- [- closePipes](iousbhostinterface/1522093-closepipes.md)
- [- closePipesGated](iousbhostinterface/1522046-closepipesgated.md)
- [- compareProperty](iousbhostinterface/1522085-compareproperty.md)
- [- compareProperty](iousbhostinterface/3516799-compareproperty.md)
- [- copyPipe](iousbhostinterface/1522071-copypipe.md)
- [- copyPipeGated](iousbhostinterface/1522089-copypipegated.md)
- [- createIOBuffer](iousbhostinterface/1522051-createiobuffer.md)
- [- destroyPipes](iousbhostinterface/1522053-destroypipes.md)
- [- destroyPipesGated](iousbhostinterface/1522072-destroypipesgated.md)
- [- deviceRequest](iousbhostinterface/1522092-devicerequest.md)
- [- deviceRequest](iousbhostinterface/3516800-devicerequest.md)
- [- deviceRequest](iousbhostinterface/3516801-devicerequest.md)
- [- deviceRequest](iousbhostinterface/3516802-devicerequest.md)
- [- free](iousbhostinterface/1522074-free.md)
- [- getConfigurationDescriptor](iousbhostinterface/1522080-getconfigurationdescriptor.md)
- [- getDevice](iousbhostinterface/1522048-getdevice.md)
- [- getFrameNumber](iousbhostinterface/1522064-getframenumber.md)
- [- getIdlePolicy](iousbhostinterface/1522042-getidlepolicy.md)
- [- getInterfaceDescriptor](iousbhostinterface/1522076-getinterfacedescriptor.md)
- [- getInterfaceDescriptorGated](iousbhostinterface/1522081-getinterfacedescriptorgated.md)
- [- getMetaClass](iousbhostinterface/1522070-getmetaclass.md)
- [- getPortStatus](iousbhostinterface/1522078-getportstatus.md)
- [- getStringDescriptor](iousbhostinterface/1522045-getstringdescriptor.md)
- [- initWithDescriptors](iousbhostinterface/1522047-initwithdescriptors.md)
- [- matchPropertyTable](iousbhostinterface/1522067-matchpropertytable.md)
- [- matchPropertyTable](iousbhostinterface/3516803-matchpropertytable.md)
- [- message](iousbhostinterface/1522043-message.md)
- [- newUserClient](iousbhostinterface/3294680-newuserclient.md)
- [- open](iousbhostinterface/1522086-open.md)
- [- openGated](iousbhostinterface/1522037-opengated.md)
- [- pipeLockLock](iousbhostinterface/1522073-pipelocklock.md)
- [- pipeLockUnlock](iousbhostinterface/1522038-pipelockunlock.md)
- [- selectAlternateSetting](iousbhostinterface/1522060-selectalternatesetting.md)
- [- selectAlternateSettingGated](iousbhostinterface/1522065-selectalternatesettinggated.md)
- [- setIdlePolicy](iousbhostinterface/1522040-setidlepolicy.md)
- [- start](iousbhostinterface/1522091-start.md)
- [- stop](iousbhostinterface/1522088-stop.md)
- [- stringFromReturn](iousbhostinterface/1522069-stringfromreturn.md)
- [- terminate](iousbhostinterface/1522087-terminate.md)
- [- updateMatchingProperties](iousbhostinterface/1522055-updatematchingproperties.md)
### Type Methods
- [+ Close_Invoke](iousbhostinterface/3182574-close_invoke.md)
- [+ CopyDevice_Invoke](iousbhostinterface/3182577-copydevice_invoke.md)
- [+ CopyPipe_Invoke](iousbhostinterface/3182579-copypipe_invoke.md)
- [+ GetFrameNumber_Invoke](iousbhostinterface/3182588-getframenumber_invoke.md)
- [+ GetIdlePolicy_Invoke](iousbhostinterface/3182590-getidlepolicy_invoke.md)
- [+ GetPortStatus_Invoke](iousbhostinterface/3182593-getportstatus_invoke.md)
- [+ Open_Invoke](iousbhostinterface/3182595-open_invoke.md)
- [+ SelectAlternateSetting_Invoke](iousbhostinterface/3182597-selectalternatesetting_invoke.md)
- [+ SetIdlePolicy_Invoke](iousbhostinterface/3182599-setidlepolicy_invoke.md)
- [+ withDescriptors](iousbhostinterface/1522058-withdescriptors.md)

## Relationships

### Inherits From
- [IOUSBInterface](iousbinterface.md)

## See Also

- [IOUSBDevice](iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](1575304-ioofpathmatching.md)
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
- [IOEthernetInterface](ioethernetinterface.md)
  The Ethernet interface object.
- [IOEthernetController](ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostinterface)*
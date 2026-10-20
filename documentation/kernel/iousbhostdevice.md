# IOUSBHostDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.11+ - Deprecated in 10.15.4

## Declaration

```cpp
class IOUSBHostDevice : IOUSBDevice
```

## Topics

### Instance Methods
- [- AbortDeviceRequests](./iousbhostdevice/api-3294604-abortdevicerequests.md)
- [- AbortDeviceRequests_Impl](./iousbhostdevice/api-3294605-abortdevicerequests_impl.md)
- [- AsyncDeviceRequest](./iousbhostdevice/api-3294607-asyncdevicerequest.md)
- [- AsyncDeviceRequest_Impl](./iousbhostdevice/api-3294608-asyncdevicerequest_impl.md)
- [- Close](./iousbhostdevice/api-3294610-close.md)
- [- Close_Impl](./iousbhostdevice/api-3294611-close_impl.md)
- [- CompleteAsyncDeviceRequest](./iousbhostdevice/api-3294613-completeasyncdevicerequest.md)
- [- CopyInterface](./iousbhostdevice/api-3294615-copyinterface.md)
- [- CopyInterface_Impl](./iousbhostdevice/api-3294616-copyinterface_impl.md)
- [- CreateIOBuffer](./iousbhostdevice/api-3294618-createiobuffer.md)
- [- CreateIOBuffer_Impl](./iousbhostdevice/api-3294619-createiobuffer_impl.md)
- [- CreateInterfaceIterator](./iousbhostdevice/api-3294621-createinterfaceiterator.md)
- [- CreateInterfaceIterator_Impl](./iousbhostdevice/api-3294622-createinterfaceiterator_impl.md)
- [- DestroyInterfaceIterator](./iousbhostdevice/api-3294624-destroyinterfaceiterator.md)
- [- DestroyInterfaceIterator_Impl](./iousbhostdevice/api-3294625-destroyinterfaceiterator_impl.md)
- [- DeviceRequest](./iousbhostdevice/api-3294627-devicerequest.md)
- [- DeviceRequest_Impl](./iousbhostdevice/api-3294628-devicerequest_impl.md)
- [- Dispatch](./iousbhostdevice/api-3294630-dispatch.md)
- [- GetAddress](./iousbhostdevice/api-3294631-getaddress.md)
- [- GetAddress_Impl](./iousbhostdevice/api-3294632-getaddress_impl.md)
- [- GetFrameNumber](./iousbhostdevice/api-3438056-getframenumber.md)
- [- GetFrameNumber_Impl](./iousbhostdevice/api-3294634-getframenumber_impl.md)
- [- GetPortStatus](./iousbhostdevice/api-3294636-getportstatus.md)
- [- GetPortStatus_Impl](./iousbhostdevice/api-3294637-getportstatus_impl.md)
- [- GetSpeed](./iousbhostdevice/api-3294639-getspeed.md)
- [- GetSpeed_Impl](./iousbhostdevice/api-3294640-getspeed_impl.md)
- [- Open](./iousbhostdevice/api-3294642-open.md)
- [- Open_Impl](./iousbhostdevice/api-3294643-open_impl.md)
- [- PMstop](./iousbhostdevice/api-1543395-pmstop.md)
- [- Reset](./iousbhostdevice/api-3294645-reset.md)
- [- Reset_Impl](./iousbhostdevice/api-3294646-reset_impl.md)
- [- SetConfiguration](./iousbhostdevice/api-3294648-setconfiguration.md)
- [- SetConfiguration_Impl](./iousbhostdevice/api-3294649-setconfiguration_impl.md)
- [- abortDeviceRequests](./iousbhostdevice/api-1543435-abortdevicerequests.md)
- [- abortDeviceRequestsGated](./iousbhostdevice/api-1543480-abortdevicerequestsgated.md)
- [- addPowerChild](./iousbhostdevice/api-1543386-addpowerchild.md)
- [- addPowerChildGated](./iousbhostdevice/api-1543401-addpowerchildgated.md)
- [- addPowerChildThreadCall](./iousbhostdevice/api-1543437-addpowerchildthreadcall.md)
- [- allocateDownstreamBusCurrent](./iousbhostdevice/api-1543454-allocatedownstreambuscurrent.md)
- [- allocateDownstreamBusCurrentGated](./iousbhostdevice/api-1543464-allocatedownstreambuscurrentgate.md)
- [- attach](./iousbhostdevice/api-1543469-attach.md)
- [- cacheDescriptor](./iousbhostdevice/api-1543430-cachedescriptor.md)
- [- cacheDescriptorGated](./iousbhostdevice/api-1543463-cachedescriptorgated.md)
- [- close](./iousbhostdevice/api-1543377-close.md)
- [- closeGated](./iousbhostdevice/api-1543449-closegated.md)
- [- compareProperty](./iousbhostdevice/api-1543452-compareproperty.md)
- [- compareProperty](./iousbhostdevice/api-3516784-compareproperty.md)
- [- createIOBuffer](./iousbhostdevice/api-1543494-createiobuffer.md)
- [- createPipe](./iousbhostdevice/api-1543407-createpipe.md)
- [- createPipeGated](./iousbhostdevice/api-1543411-createpipegated.md)
- [- deviceRequest](./iousbhostdevice/api-1543421-devicerequest.md)
- [- deviceRequest](./iousbhostdevice/api-3516785-devicerequest.md)
- [- deviceRequest](./iousbhostdevice/api-3516786-devicerequest.md)
- [- deviceRequest](./iousbhostdevice/api-3516787-devicerequest.md)
- [- deviceRequest](./iousbhostdevice/api-3516788-devicerequest.md)
- [- forcePower](./iousbhostdevice/api-1543397-forcepower.md)
- [- forcePowerGated](./iousbhostdevice/api-1543393-forcepowergated.md)
- [- free](./iousbhostdevice/api-1543478-free.md)
- [- getAddress](./iousbhostdevice/api-1543403-getaddress.md)
- [- getCapabilityDescriptors](./iousbhostdevice/api-1543412-getcapabilitydescriptors.md)
- [- getConfigurationDescriptor](./iousbhostdevice/api-1543384-getconfigurationdescriptor.md)
- [- getConfigurationDescriptor](./iousbhostdevice/api-3516789-getconfigurationdescriptor.md)
- [- getConfigurationDescriptorWithValue](./iousbhostdevice/api-1543459-getconfigurationdescriptorwithva.md)
- [- getDescriptor](./iousbhostdevice/api-1543445-getdescriptor.md)
- [- getDescriptorGated](./iousbhostdevice/api-1543448-getdescriptorgated.md)
- [- getDeviceDescriptor](./iousbhostdevice/api-1543418-getdevicedescriptor.md)
- [- getFrameNumber](./iousbhostdevice/api-1543486-getframenumber.md)
- [- getLPMExitLatency](./iousbhostdevice/api-2880436-getlpmexitlatency.md)
- [- getLPMExitLatencyGated](./iousbhostdevice/api-2880438-getlpmexitlatencygated.md)
- [- getMetaClass](./iousbhostdevice/api-1543468-getmetaclass.md)
- [- getPortStatus](./iousbhostdevice/api-1543383-getportstatus.md)
- [- getSpeed](./iousbhostdevice/api-1543433-getspeed.md)
- [- getStringDescriptor](./iousbhostdevice/api-1543434-getstringdescriptor.md)
- [- handleClose](./iousbhostdevice/api-1543381-handleclose.md)
- [- handleIsOpen](./iousbhostdevice/api-1543487-handleisopen.md)
- [- handleOpen](./iousbhostdevice/api-1543423-handleopen.md)
- [- idleAssertion](./iousbhostdevice/api-1543405-idleassertion.md)
- [- initWithController](./iousbhostdevice/api-1543488-initwithcontroller.md)
- [- initialPowerStateForDomainState](./iousbhostdevice/api-1543424-initialpowerstatefordomainstate.md)
- [- internalDeviceRequest](./iousbhostdevice/api-1543490-internaldevicerequest.md)
- [- internalDeviceRequestGated](./iousbhostdevice/api-1543391-internaldevicerequestgated.md)
- [- matchPropertyTable](./iousbhostdevice/api-1543439-matchpropertytable.md)
- [- matchPropertyTable](./iousbhostdevice/api-3516790-matchpropertytable.md)
- [- message](./iousbhostdevice/api-1543402-message.md)
- [- newUserClient](./iousbhostdevice/api-3294652-newuserclient.md)
- [- open](./iousbhostdevice/api-1543427-open.md)
- [- openGated](./iousbhostdevice/api-1543473-opengated.md)
- [- pmStopThreadCall](./iousbhostdevice/api-1543428-pmstopthreadcall.md)
- [- powerChangeDone](./iousbhostdevice/api-1543491-powerchangedone.md)
- [- powerStateDidChangeTo](./iousbhostdevice/api-1543476-powerstatedidchangeto.md)
- [- powerStateDidChangeToGated](./iousbhostdevice/api-1543420-powerstatedidchangetogated.md)
- [- powerStateWillChangeTo](./iousbhostdevice/api-1543453-powerstatewillchangeto.md)
- [- powerStateWillChangeToGated](./iousbhostdevice/api-1543447-powerstatewillchangetogated.md)
- [- registerPowerService](./iousbhostdevice/api-1543417-registerpowerservice.md)
- [- removePowerChild](./iousbhostdevice/api-1543406-removepowerchild.md)
- [- reset](./iousbhostdevice/api-1543415-reset.md)
- [- setConfiguration](./iousbhostdevice/api-1543493-setconfiguration.md)
- [- setConfigurationGated](./iousbhostdevice/api-1543399-setconfigurationgated.md)
- [- setPowerState](./iousbhostdevice/api-1543458-setpowerstate.md)
- [- setPowerStateGated](./iousbhostdevice/api-1543461-setpowerstategated.md)
- [- setProperties](./iousbhostdevice/api-1644644-setproperties.md)
- [- setProperty](./iousbhostdevice/api-1644643-setproperty.md)
- [- setProperty](./iousbhostdevice/api-3516791-setproperty.md)
- [- setProperty](./iousbhostdevice/api-3516792-setproperty.md)
- [- setProperty](./iousbhostdevice/api-3516793-setproperty.md)
- [- setProperty](./iousbhostdevice/api-3516794-setproperty.md)
- [- setProperty](./iousbhostdevice/api-3516795-setproperty.md)
- [- setProperty](./iousbhostdevice/api-3516796-setproperty.md)
- [- start](./iousbhostdevice/api-1543387-start.md)
- [- stop](./iousbhostdevice/api-1543466-stop.md)
- [- stringFromReturn](./iousbhostdevice/api-1543456-stringfromreturn.md)
- [- terminate](./iousbhostdevice/api-1543379-terminate.md)
- [- terminateGated](./iousbhostdevice/api-1543495-terminategated.md)
- [- updateIdlePolicy](./iousbhostdevice/api-1543409-updateidlepolicy.md)
- [- updateIdlePolicyAsync](./iousbhostdevice/api-1543483-updateidlepolicyasync.md)
- [- updateIdlePolicyGated](./iousbhostdevice/api-1543441-updateidlepolicygated.md)
- [- updateLPMPolicyGated](./iousbhostdevice/api-2880437-updatelpmpolicygated.md)
### Type Methods
- [+ AbortDeviceRequests_Invoke](./iousbhostdevice/api-3182482-abortdevicerequests_invoke.md)
- [+ AsyncDeviceRequest_Invoke](./iousbhostdevice/api-3182484-asyncdevicerequest_invoke.md)
- [+ Close_Invoke](./iousbhostdevice/api-3182486-close_invoke.md)
- [+ CompleteAsyncDeviceRequest_Invoke](./iousbhostdevice/api-4520043-completeasyncdevicerequest_invok.md)
- [+ CompleteAsyncDeviceRequest_Invoke](./iousbhostdevice/api-4520044-completeasyncdevicerequest_invok.md)
- [+ CopyInterface_Invoke](./iousbhostdevice/api-3182495-copyinterface_invoke.md)
- [+ CreateIOBuffer_Invoke](./iousbhostdevice/api-3182498-createiobuffer_invoke.md)
- [+ CreateInterfaceIterator_Invoke](./iousbhostdevice/api-3182500-createinterfaceiterator_invoke.md)
- [+ DestroyInterfaceIterator_Invoke](./iousbhostdevice/api-3182502-destroyinterfaceiterator_invoke.md)
- [+ DeviceRequest_Invoke](./iousbhostdevice/api-3182504-devicerequest_invoke.md)
- [+ GetAddress_Invoke](./iousbhostdevice/api-3182508-getaddress_invoke.md)
- [+ GetFrameNumber_Invoke](./iousbhostdevice/api-3182510-getframenumber_invoke.md)
- [+ GetPortStatus_Invoke](./iousbhostdevice/api-3182512-getportstatus_invoke.md)
- [+ GetSpeed_Invoke](./iousbhostdevice/api-3182514-getspeed_invoke.md)
- [+ Open_Invoke](./iousbhostdevice/api-3182516-open_invoke.md)
- [+ Reset_Invoke](./iousbhostdevice/api-3182518-reset_invoke.md)
- [+ SetConfiguration_Invoke](./iousbhostdevice/api-3182520-setconfiguration_invoke.md)
- [+ asyncDeviceRequestCompletionCallback](./iousbhostdevice/api-3294651-asyncdevicerequestcompletioncall.md)
- [+ withController](./iousbhostdevice/api-1543394-withcontroller.md)

## Relationships

### Inherits From
- [IOUSBDevice](./iousbdevice.md)

## See Also

### IOKit
- [IOUSBDevice](./iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](./iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](./api-1575304-ioofpathmatching.md)
- [IOUSBHostInterface](./iousbhostinterface.md)
- [IOUSBHostPipe](./iousbhostpipe.md)
- [IOUSBHostIOSource](./iousbhostiosource.md)
- [IOUSBHostStream](./iousbhoststream.md)
- [IOHIDEventDriver](./iohideventdriver.md)
- [IOHIDEventService](./iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDInterface](./iohidinterface.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDSystem](./iohidsystem.md)
- [IOHIKeyboardMapper](./iohikeyboardmapper.md)
- [IOHIKeyboard](./iohikeyboard.md)
- [IOHIPointing](./iohipointing.md)
- [IOHIDevice](./iohidevice.md)
- [IOHIDElement](./iohidelement.md)
- [IOHIDWorkLoop](./iohidworkloop.md)
- [IOEthernetInterface](./ioethernetinterface.md)
  The Ethernet interface object.
- [IOEthernetController](./ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostdevice)*
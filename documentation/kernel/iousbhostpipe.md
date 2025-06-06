# IOUSBHostPipe

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.11+ - Deprecated in 10.15.4

## Declaration

```swift
class IOUSBHostPipe : IOUSBHostIOSource
```

## Topics

### Instance Methods
- [- Abort](iousbhostpipe/3294681-abort.md)
- [- Abort_Impl](iousbhostpipe/3294682-abort_impl.md)
- [- AdjustPipe](iousbhostpipe/3294684-adjustpipe.md)
- [- AdjustPipe_Impl](iousbhostpipe/3294685-adjustpipe_impl.md)
- [- AsyncIO](iousbhostpipe/3294687-asyncio.md)
- [- AsyncIOBundled](iousbhostpipe/3438058-asynciobundled.md)
- [- AsyncIOBundled_Impl](iousbhostpipe/3294688-asynciobundled_impl.md)
- [- AsyncIO_Impl](iousbhostpipe/3294690-asyncio_impl.md)
- [- ClearStall](iousbhostpipe/3294692-clearstall.md)
- [- ClearStall_Impl](iousbhostpipe/3294693-clearstall_impl.md)
- [- CompleteAsyncIO](iousbhostpipe/3294695-completeasyncio.md)
- [- CompleteAsyncIOBundled](iousbhostpipe/3438059-completeasynciobundled.md)
- [- CompleteAsyncIsochIO](iousbhostpipe/3438062-completeasyncisochio.md)
- [- CreateMemoryDescriptorRing](../usbdriverkit/iousbhostpipe/creatememorydescriptorring.md)
- [- CreateMemoryDescriptorRing_Impl](iousbhostpipe/3294700-creatememorydescriptorring_impl.md)
- [- Dispatch](iousbhostpipe/3294702-dispatch.md)
- [- GetDescriptors](iousbhostpipe/3294703-getdescriptors.md)
- [- GetDescriptors_Impl](iousbhostpipe/3294704-getdescriptors_impl.md)
- [- GetDeviceAddress](iousbhostpipe/3294706-getdeviceaddress.md)
- [- GetDeviceAddress_Impl](iousbhostpipe/3294707-getdeviceaddress_impl.md)
- [- GetIdlePolicy](iousbhostpipe/3294709-getidlepolicy.md)
- [- GetIdlePolicy_Impl](iousbhostpipe/3294710-getidlepolicy_impl.md)
- [- GetSpeed](iousbhostpipe/3294712-getspeed.md)
- [- GetSpeed_Impl](iousbhostpipe/3294713-getspeed_impl.md)
- [- IO](iousbhostpipe/3294715-io.md)
- [- IO_Impl](iousbhostpipe/3294716-io_impl.md)
- [- IsochIO](iousbhostpipe/3438063-isochio.md)
- [- IsochIO_Impl](iousbhostpipe/3366019-isochio_impl.md)
- [- SetIdlePolicy](iousbhostpipe/3294718-setidlepolicy.md)
- [- SetIdlePolicy_Impl](iousbhostpipe/3294719-setidlepolicy_impl.md)
- [- SetMemoryDescriptor](../usbdriverkit/iousbhostpipe/setmemorydescriptor.md)
- [- SetMemoryDescriptor_Impl](iousbhostpipe/3294722-setmemorydescriptor_impl.md)
- [- abort](iousbhostpipe/1584505-abort.md)
- [- abortGated](iousbhostpipe/1584499-abortgated.md)
- [- adjustOutstandingIO](iousbhostpipe/2881960-adjustoutstandingio.md)
- [- adjustPipe](iousbhostpipe/1584512-adjustpipe.md)
- [- adjustPipe](iousbhostpipe/3516804-adjustpipe.md)
- [- adjustPipeGated](iousbhostpipe/1584485-adjustpipegated.md)
- [- adjustPipeGatedV2](iousbhostpipe/1644642-adjustpipegatedv2.md)
- [- clearStall](iousbhostpipe/1584510-clearstall.md)
- [- clearStallGated](iousbhostpipe/1584497-clearstallgated.md)
- [- closeGated](iousbhostpipe/1584482-closegated.md)
- [- controlRequest](iousbhostpipe/1584489-controlrequest.md)
- [- controlRequest](iousbhostpipe/3516805-controlrequest.md)
- [- controlRequest](iousbhostpipe/3516806-controlrequest.md)
- [- controlRequest](iousbhostpipe/3516807-controlrequest.md)
- [- controlRequestGated](iousbhostpipe/1584491-controlrequestgated.md)
- [- copyStream](iousbhostpipe/1584502-copystream.md)
- [- copyStreamGated](iousbhostpipe/1584514-copystreamgated.md)
- [- destroyGated](iousbhostpipe/1584506-destroygated.md)
- [- destroyMemoryDescriptorRing](iousbhostpipe/3294727-destroymemorydescriptorring.md)
- [- disableStreams](iousbhostpipe/1584507-disablestreams.md)
- [- disableStreamsGated](iousbhostpipe/1584492-disablestreamsgated.md)
- [- enableStreams](iousbhostpipe/1584483-enablestreams.md)
- [- enableStreamsGated](iousbhostpipe/1584496-enablestreamsgated.md)
- [- free](iousbhostpipe/1584484-free.md)
- [- getDescriptors](iousbhostpipe/1644641-getdescriptors.md)
- [- getDeviceAddress](iousbhostpipe/1584487-getdeviceaddress.md)
- [- getEndpointDescriptor](iousbhostpipe/1584486-getendpointdescriptor.md)
- [- getIdlePolicy](iousbhostpipe/1584498-getidlepolicy.md)
- [- getIdlePolicyGated](iousbhostpipe/1584508-getidlepolicygated.md)
- [- getMetaClass](iousbhostpipe/1584511-getmetaclass.md)
- [- getOutstandingIO](iousbhostpipe/2881961-getoutstandingio.md)
- [- getSpeed](iousbhostpipe/1584488-getspeed.md)
- [- getSuperSpeedEndpointCompanionDescriptor](iousbhostpipe/1584513-getsuperspeedendpointcompanionde.md)
- [- initWithDescriptorsAndOwners](iousbhostpipe/1584493-initwithdescriptorsandowners.md)
- [- io](iousbhostpipe/1584504-io.md)
- [- io](iousbhostpipe/3516808-io.md)
- [- io](iousbhostpipe/3516809-io.md)
- [- io](iousbhostpipe/3516810-io.md)
- [- io](iousbhostpipe/3753556-io.md)
- [- io](iousbhostpipe/3753557-io.md)
- [- isochronousIoGated](iousbhostpipe/1584509-isochronousiogated.md)
- [- openGated](iousbhostpipe/1584503-opengated.md)
- [- setIdlePolicy](iousbhostpipe/1584500-setidlepolicy.md)
- [- setIdlePolicyGated](iousbhostpipe/1584494-setidlepolicygated.md)
### Type Methods
- [+ Abort_Invoke](iousbhostpipe/3182644-abort_invoke.md)
- [+ AdjustPipe_Invoke](iousbhostpipe/3182646-adjustpipe_invoke.md)
- [+ AsyncIOBundled_Invoke](iousbhostpipe/3230711-asynciobundled_invoke.md)
- [+ AsyncIO_Invoke](iousbhostpipe/3182648-asyncio_invoke.md)
- [+ ClearStall_Invoke](iousbhostpipe/3182650-clearstall_invoke.md)
- [+ CompleteAsyncIOBundled_Invoke](iousbhostpipe/4520045-completeasynciobundled_invoke.md)
- [+ CompleteAsyncIOBundled_Invoke](iousbhostpipe/4520046-completeasynciobundled_invoke.md)
- [+ CompleteAsyncIO_Invoke](iousbhostpipe/4520047-completeasyncio_invoke.md)
- [+ CompleteAsyncIO_Invoke](iousbhostpipe/4520048-completeasyncio_invoke.md)
- [+ CompleteAsyncIsochIO_Invoke](iousbhostpipe/4520049-completeasyncisochio_invoke.md)
- [+ CompleteAsyncIsochIO_Invoke](iousbhostpipe/4520050-completeasyncisochio_invoke.md)
- [+ CreateMemoryDescriptorRing_Invoke](iousbhostpipe/3295834-creatememorydescriptorring_invok.md)
- [+ GetDescriptors_Invoke](iousbhostpipe/3182657-getdescriptors_invoke.md)
- [+ GetDeviceAddress_Invoke](iousbhostpipe/3182659-getdeviceaddress_invoke.md)
- [+ GetIdlePolicy_Invoke](iousbhostpipe/3182661-getidlepolicy_invoke.md)
- [+ GetSpeed_Invoke](iousbhostpipe/3182663-getspeed_invoke.md)
- [+ IO_Invoke](iousbhostpipe/3182665-io_invoke.md)
- [+ IsochIO_Invoke](iousbhostpipe/3366113-isochio_invoke.md)
- [+ SetIdlePolicy_Invoke](iousbhostpipe/3182668-setidlepolicy_invoke.md)
- [+ SetMemoryDescriptor_Invoke](iousbhostpipe/3295836-setmemorydescriptor_invoke.md)
- [+ asyncIOCompletionCallback](iousbhostpipe/3294724-asynciocompletioncallback.md)
- [+ asyncIOCompletionCallbackBundled](iousbhostpipe/3294725-asynciocompletioncallbackbundled.md)
- [+ asyncIsochIOCompletionCallback](iousbhostpipe/3294726-asyncisochiocompletioncallback.md)
- [+ asyncIsochIOTransactionCompletionCallback](iousbhostpipe/3753555-asyncisochiotransactioncompletio.md)
- [+ isochIOTransactionCompatCallback](iousbhostpipe/3753558-isochiotransactioncompatcallback.md)
- [+ rawBufferControlRequestCompletion](iousbhostpipe/1584490-rawbuffercontrolrequestcompletio.md)
- [+ withDescriptorsAndOwners](iousbhostpipe/1584495-withdescriptorsandowners.md)

## Relationships

### Inherits From
- [IOUSBHostIOSource](iousbhostiosource.md)

## See Also

- [IOUSBDevice](iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](1575304-ioofpathmatching.md)
- [IOUSBHostInterface](iousbhostinterface.md)
- [IOUSBHostDevice](iousbhostdevice.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostpipe)*
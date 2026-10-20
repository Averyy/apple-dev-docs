# IOUSBHostPipe

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.11+ - Deprecated in 10.15.4

## Declaration

```cpp
class IOUSBHostPipe : IOUSBHostIOSource
```

## Topics

### Instance Methods
- [- Abort](./iousbhostpipe/api-3294681-abort.md)
- [- Abort_Impl](./iousbhostpipe/api-3294682-abort_impl.md)
- [- AdjustPipe](./iousbhostpipe/api-3294684-adjustpipe.md)
- [- AdjustPipe_Impl](./iousbhostpipe/api-3294685-adjustpipe_impl.md)
- [- AsyncIO](./iousbhostpipe/api-3294687-asyncio.md)
- [- AsyncIOBundled](./iousbhostpipe/api-3438058-asynciobundled.md)
- [- AsyncIOBundled_Impl](./iousbhostpipe/api-3294688-asynciobundled_impl.md)
- [- AsyncIO_Impl](./iousbhostpipe/api-3294690-asyncio_impl.md)
- [- ClearStall](./iousbhostpipe/api-3294692-clearstall.md)
- [- ClearStall_Impl](./iousbhostpipe/api-3294693-clearstall_impl.md)
- [- CompleteAsyncIO](./iousbhostpipe/api-3294695-completeasyncio.md)
- [- CompleteAsyncIOBundled](./iousbhostpipe/api-3438059-completeasynciobundled.md)
- [- CompleteAsyncIsochIO](./iousbhostpipe/api-3438062-completeasyncisochio.md)
- [- CreateMemoryDescriptorRing](../USBDriverKit/iousbhostpipe/creatememorydescriptorring.md)
- [- CreateMemoryDescriptorRing_Impl](./iousbhostpipe/api-3294700-creatememorydescriptorring_impl.md)
- [- Dispatch](./iousbhostpipe/api-3294702-dispatch.md)
- [- GetDescriptors](./iousbhostpipe/api-3294703-getdescriptors.md)
- [- GetDescriptors_Impl](./iousbhostpipe/api-3294704-getdescriptors_impl.md)
- [- GetDeviceAddress](./iousbhostpipe/api-3294706-getdeviceaddress.md)
- [- GetDeviceAddress_Impl](./iousbhostpipe/api-3294707-getdeviceaddress_impl.md)
- [- GetIdlePolicy](./iousbhostpipe/api-3294709-getidlepolicy.md)
- [- GetIdlePolicy_Impl](./iousbhostpipe/api-3294710-getidlepolicy_impl.md)
- [- GetSpeed](./iousbhostpipe/api-3294712-getspeed.md)
- [- GetSpeed_Impl](./iousbhostpipe/api-3294713-getspeed_impl.md)
- [- IO](./iousbhostpipe/api-3294715-io.md)
- [- IO_Impl](./iousbhostpipe/api-3294716-io_impl.md)
- [- IsochIO](./iousbhostpipe/api-3438063-isochio.md)
- [- IsochIO_Impl](./iousbhostpipe/api-3366019-isochio_impl.md)
- [- SetIdlePolicy](./iousbhostpipe/api-3294718-setidlepolicy.md)
- [- SetIdlePolicy_Impl](./iousbhostpipe/api-3294719-setidlepolicy_impl.md)
- [- SetMemoryDescriptor](../USBDriverKit/iousbhostpipe/setmemorydescriptor.md)
- [- SetMemoryDescriptor_Impl](./iousbhostpipe/api-3294722-setmemorydescriptor_impl.md)
- [- abort](./iousbhostpipe/api-1584505-abort.md)
- [- abortGated](./iousbhostpipe/api-1584499-abortgated.md)
- [- adjustOutstandingIO](./iousbhostpipe/api-2881960-adjustoutstandingio.md)
- [- adjustPipe](./iousbhostpipe/api-1584512-adjustpipe.md)
- [- adjustPipe](./iousbhostpipe/api-3516804-adjustpipe.md)
- [- adjustPipeGated](./iousbhostpipe/api-1584485-adjustpipegated.md)
- [- adjustPipeGatedV2](./iousbhostpipe/api-1644642-adjustpipegatedv2.md)
- [- clearStall](./iousbhostpipe/api-1584510-clearstall.md)
- [- clearStallGated](./iousbhostpipe/api-1584497-clearstallgated.md)
- [- closeGated](./iousbhostpipe/api-1584482-closegated.md)
- [- controlRequest](./iousbhostpipe/api-1584489-controlrequest.md)
- [- controlRequest](./iousbhostpipe/api-3516805-controlrequest.md)
- [- controlRequest](./iousbhostpipe/api-3516806-controlrequest.md)
- [- controlRequest](./iousbhostpipe/api-3516807-controlrequest.md)
- [- controlRequestGated](./iousbhostpipe/api-1584491-controlrequestgated.md)
- [- copyStream](./iousbhostpipe/api-1584502-copystream.md)
- [- copyStreamGated](./iousbhostpipe/api-1584514-copystreamgated.md)
- [- destroyGated](./iousbhostpipe/api-1584506-destroygated.md)
- [- destroyMemoryDescriptorRing](./iousbhostpipe/api-3294727-destroymemorydescriptorring.md)
- [- disableStreams](./iousbhostpipe/api-1584507-disablestreams.md)
- [- disableStreamsGated](./iousbhostpipe/api-1584492-disablestreamsgated.md)
- [- enableStreams](./iousbhostpipe/api-1584483-enablestreams.md)
- [- enableStreamsGated](./iousbhostpipe/api-1584496-enablestreamsgated.md)
- [- free](./iousbhostpipe/api-1584484-free.md)
- [- getDescriptors](./iousbhostpipe/api-1644641-getdescriptors.md)
- [- getDeviceAddress](./iousbhostpipe/api-1584487-getdeviceaddress.md)
- [- getEndpointDescriptor](./iousbhostpipe/api-1584486-getendpointdescriptor.md)
- [- getIdlePolicy](./iousbhostpipe/api-1584498-getidlepolicy.md)
- [- getIdlePolicyGated](./iousbhostpipe/api-1584508-getidlepolicygated.md)
- [- getMetaClass](./iousbhostpipe/api-1584511-getmetaclass.md)
- [- getOutstandingIO](./iousbhostpipe/api-2881961-getoutstandingio.md)
- [- getSpeed](./iousbhostpipe/api-1584488-getspeed.md)
- [- getSuperSpeedEndpointCompanionDescriptor](./iousbhostpipe/api-1584513-getsuperspeedendpointcompanionde.md)
- [- initWithDescriptorsAndOwners](./iousbhostpipe/api-1584493-initwithdescriptorsandowners.md)
- [- io](./iousbhostpipe/api-1584504-io.md)
- [- io](./iousbhostpipe/api-3516808-io.md)
- [- io](./iousbhostpipe/api-3516809-io.md)
- [- io](./iousbhostpipe/api-3516810-io.md)
- [- io](./iousbhostpipe/api-3753556-io.md)
- [- io](./iousbhostpipe/api-3753557-io.md)
- [- isochronousIoGated](./iousbhostpipe/api-1584509-isochronousiogated.md)
- [- openGated](./iousbhostpipe/api-1584503-opengated.md)
- [- setIdlePolicy](./iousbhostpipe/api-1584500-setidlepolicy.md)
- [- setIdlePolicyGated](./iousbhostpipe/api-1584494-setidlepolicygated.md)
### Type Methods
- [+ Abort_Invoke](./iousbhostpipe/api-3182644-abort_invoke.md)
- [+ AdjustPipe_Invoke](./iousbhostpipe/api-3182646-adjustpipe_invoke.md)
- [+ AsyncIOBundled_Invoke](./iousbhostpipe/api-3230711-asynciobundled_invoke.md)
- [+ AsyncIO_Invoke](./iousbhostpipe/api-3182648-asyncio_invoke.md)
- [+ ClearStall_Invoke](./iousbhostpipe/api-3182650-clearstall_invoke.md)
- [+ CompleteAsyncIOBundled_Invoke](./iousbhostpipe/api-4520045-completeasynciobundled_invoke.md)
- [+ CompleteAsyncIOBundled_Invoke](./iousbhostpipe/api-4520046-completeasynciobundled_invoke.md)
- [+ CompleteAsyncIO_Invoke](./iousbhostpipe/api-4520047-completeasyncio_invoke.md)
- [+ CompleteAsyncIO_Invoke](./iousbhostpipe/api-4520048-completeasyncio_invoke.md)
- [+ CompleteAsyncIsochIO_Invoke](./iousbhostpipe/api-4520049-completeasyncisochio_invoke.md)
- [+ CompleteAsyncIsochIO_Invoke](./iousbhostpipe/api-4520050-completeasyncisochio_invoke.md)
- [+ CreateMemoryDescriptorRing_Invoke](./iousbhostpipe/api-3295834-creatememorydescriptorring_invok.md)
- [+ GetDescriptors_Invoke](./iousbhostpipe/api-3182657-getdescriptors_invoke.md)
- [+ GetDeviceAddress_Invoke](./iousbhostpipe/api-3182659-getdeviceaddress_invoke.md)
- [+ GetIdlePolicy_Invoke](./iousbhostpipe/api-3182661-getidlepolicy_invoke.md)
- [+ GetSpeed_Invoke](./iousbhostpipe/api-3182663-getspeed_invoke.md)
- [+ IO_Invoke](./iousbhostpipe/api-3182665-io_invoke.md)
- [+ IsochIO_Invoke](./iousbhostpipe/api-3366113-isochio_invoke.md)
- [+ SetIdlePolicy_Invoke](./iousbhostpipe/api-3182668-setidlepolicy_invoke.md)
- [+ SetMemoryDescriptor_Invoke](./iousbhostpipe/api-3295836-setmemorydescriptor_invoke.md)
- [+ asyncIOCompletionCallback](./iousbhostpipe/api-3294724-asynciocompletioncallback.md)
- [+ asyncIOCompletionCallbackBundled](./iousbhostpipe/api-3294725-asynciocompletioncallbackbundled.md)
- [+ asyncIsochIOCompletionCallback](./iousbhostpipe/api-3294726-asyncisochiocompletioncallback.md)
- [+ asyncIsochIOTransactionCompletionCallback](./iousbhostpipe/api-3753555-asyncisochiotransactioncompletio.md)
- [+ isochIOTransactionCompatCallback](./iousbhostpipe/api-3753558-isochiotransactioncompatcallback.md)
- [+ rawBufferControlRequestCompletion](./iousbhostpipe/api-1584490-rawbuffercontrolrequestcompletio.md)
- [+ withDescriptorsAndOwners](./iousbhostpipe/api-1584495-withdescriptorsandowners.md)

## Relationships

### Inherits From
- [IOUSBHostIOSource](./iousbhostiosource.md)

## See Also

### IOKit
- [IOUSBDevice](./iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](./iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](./api-1575304-ioofpathmatching.md)
- [IOUSBHostInterface](./iousbhostinterface.md)
- [IOUSBHostDevice](./iousbhostdevice.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostpipe)*
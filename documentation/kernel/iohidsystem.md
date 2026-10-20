# IOHIDSystem

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.15.4+ - Deprecated in 10.15.4

## Declaration

```cpp
class IOHIDSystem : IOService
```

## Topics

### Instance Methods
- [- animateWaitCursor](./iohidsystem/api-1646093-animatewaitcursor.md)
- [- attach](./iohidsystem/api-1646018-attach.md)
- [- changeCursor](./iohidsystem/api-1646067-changecursor.md)
- [- configureReport](./iohidsystem/api-3516597-configurereport.md)
- [- createFilteredParamPropertiesForService](./iohidsystem/api-1646048-createfilteredparampropertiesfor.md)
- [- createParameters](./iohidsystem/api-1646064-createparameters.md)
- [- createShmem](./iohidsystem/api-1646043-createshmem.md)
- [- createShmemGated](./iohidsystem/api-1645992-createshmemgated.md)
- [- detach](./iohidsystem/api-1646097-detach.md)
- [- disableContinuousCursor](./iohidsystem/api-1646055-disablecontinuouscursor.md)
- [- dispatchEvent](./iohidsystem/api-1646005-dispatchevent.md)
- [- doProcessNotifications](./iohidsystem/api-1646070-doprocessnotifications.md)
- [- enableContinuousCursor](./iohidsystem/api-1646063-enablecontinuouscursor.md)
- [- evClose](./iohidsystem/api-1646002-evclose.md)
- [- evCloseGated](./iohidsystem/api-1646091-evclosegated.md)
- [- evDispatch](./iohidsystem/api-1646082-evdispatch.md)
- [- evOpen](./iohidsystem/api-1646020-evopen.md)
- [- evOpenGated](./iohidsystem/api-4191644-evopengated.md)
- [- eventFlags](./iohidsystem/api-1645998-eventflags.md)
- [- extGetButtonEventNum](./iohidsystem/api-1646071-extgetbuttoneventnum.md)
- [- extGetButtonEventNumGated](./iohidsystem/api-1645984-extgetbuttoneventnumgated.md)
- [- extGetStateForSelector](./iohidsystem/api-1646019-extgetstateforselector.md)
- [- extGetUserHidActivityState](./iohidsystem/api-1646084-extgetuserhidactivitystate.md)
- [- extPostEvent](./iohidsystem/api-1645983-extpostevent.md)
- [- extPostEventGated](./iohidsystem/api-1646046-extposteventgated.md)
- [- extRegisterVirtualDisplay](./iohidsystem/api-1646077-extregistervirtualdisplay.md)
- [- extSetBounds](./iohidsystem/api-1646069-extsetbounds.md)
- [- extSetMouseLocation](./iohidsystem/api-1646034-extsetmouselocation.md)
- [- extSetMouseLocationGated](./iohidsystem/api-1646062-extsetmouselocationgated.md)
- [- extSetOnScreenBounds](./iohidsystem/api-1646011-extsetonscreenbounds.md)
- [- extSetStateForSelector](./iohidsystem/api-1646049-extsetstateforselector.md)
- [- extSetVirtualDisplayBounds](./iohidsystem/api-1646022-extsetvirtualdisplaybounds.md)
- [- extUnregisterVirtualDisplay](./iohidsystem/api-1645980-extunregistervirtualdisplay.md)
- [- free](./iohidsystem/api-1646087-free.md)
- [- genericNotificationHandler](./iohidsystem/api-1646073-genericnotificationhandler.md)
- [- getMetaClass](./iohidsystem/api-1646079-getmetaclass.md)
- [- getUserHidActivityStateGated](./iohidsystem/api-1646059-getuserhidactivitystategated.md)
- [- getWorkLoop](./iohidsystem/api-1646076-getworkloop.md)
- [- hidActivityChecker](./iohidsystem/api-1646000-hidactivitychecker.md)
- [- hideCursor](./iohidsystem/api-1646061-hidecursor.md)
- [- hideWaitCursor](./iohidsystem/api-1646066-hidewaitcursor.md)
- [- init](./iohidsystem/api-1646024-init.md)
- [- initShmem](./iohidsystem/api-1646026-initshmem.md)
- [- keyboardEvent](./iohidsystem/api-1646037-keyboardevent.md)
- [- keyboardEvent](./iohidsystem/api-3516598-keyboardevent.md)
- [- keyboardEventGated](./iohidsystem/api-1646008-keyboardeventgated.md)
- [- keyboardSpecialEvent](./iohidsystem/api-1646031-keyboardspecialevent.md)
- [- keyboardSpecialEvent](./iohidsystem/api-3516599-keyboardspecialevent.md)
- [- keyboardSpecialEventGated](./iohidsystem/api-1646025-keyboardspecialeventgated.md)
- [- message](./iohidsystem/api-1646060-message.md)
- [- moveCursor](./iohidsystem/api-1646080-movecursor.md)
- [- newUserClient](./iohidsystem/api-1646033-newuserclient.md)
- [- newUserClientGated](./iohidsystem/api-1646053-newuserclientgated.md)
- [- periodicEvents](./iohidsystem/api-1645990-periodicevents.md)
- [- pointToScreen](./iohidsystem/api-1646078-pointtoscreen.md)
- [- postEvent](./iohidsystem/api-1645987-postevent.md)
- [- probe](./iohidsystem/api-1646042-probe.md)
- [- registerEventQueue](./iohidsystem/api-1646001-registereventqueue.md)
- [- registerEventQueueGated](./iohidsystem/api-1646083-registereventqueuegated.md)
- [- registerEventSource](./iohidsystem/api-1645995-registereventsource.md)
- [- registerScreen](./iohidsystem/api-1646095-registerscreen.md)
- [- registerScreenGated](./iohidsystem/api-1645981-registerscreengated.md)
- [- reportUserHidActivityGated](./iohidsystem/api-1646041-reportuserhidactivitygated.md)
- [- resetCursor](./iohidsystem/api-1646088-resetcursor.md)
- [- scheduleNextPeriodicEvent](./iohidsystem/api-1646003-schedulenextperiodicevent.md)
- [- setBounds](./iohidsystem/api-1646038-setbounds.md)
- [- setContinuousCursorEnable](./iohidsystem/api-1645996-setcontinuouscursorenable.md)
- [- setContinuousCursorEnableGated](./iohidsystem/api-1646032-setcontinuouscursorenablegated.md)
- [- setCursorEnable](./iohidsystem/api-1645993-setcursorenable.md)
- [- setCursorEnableGated](./iohidsystem/api-1646092-setcursorenablegated.md)
- [- setCursorPosition](./iohidsystem/api-1646010-setcursorposition.md)
- [- setDisplayBoundsGated](./iohidsystem/api-1646081-setdisplayboundsgated.md)
- [- setEventsEnable](./iohidsystem/api-1646051-seteventsenable.md)
- [- setParamProperties](./iohidsystem/api-1645982-setparamproperties.md)
- [- setParamPropertiesPostGated](./iohidsystem/api-1646023-setparampropertiespostgated.md)
- [- setParamPropertiesPreGated](./iohidsystem/api-1646096-setparampropertiespregated.md)
- [- setProperties](./iohidsystem/api-1645999-setproperties.md)
- [- showCursor](./iohidsystem/api-1646054-showcursor.md)
- [- showWaitCursor](./iohidsystem/api-1645977-showwaitcursor.md)
- [- sleepDisplayTickle](./iohidsystem/api-2544881-sleepdisplaytickle.md)
- [- start](./iohidsystem/api-1646007-start.md)
- [- startCursor](./iohidsystem/api-1646009-startcursor.md)
- [- unregisterEventQueue](./iohidsystem/api-1646068-unregistereventqueue.md)
- [- unregisterEventQueueGated](./iohidsystem/api-1646090-unregistereventqueuegated.md)
- [- unregisterScreen](./iohidsystem/api-1646028-unregisterscreen.md)
- [- unregisterScreenGated](./iohidsystem/api-1645997-unregisterscreengated.md)
- [- updateEventFlags](./iohidsystem/api-1646089-updateeventflags.md)
- [- updateEventFlags](./iohidsystem/api-3516600-updateeventflags.md)
- [- updateEventFlagsGated](./iohidsystem/api-1646056-updateeventflagsgated.md)
- [- updateHidActivity](./iohidsystem/api-1646052-updatehidactivity.md)
- [- updateParamPropertiesGated](./iohidsystem/api-1646094-updateparampropertiesgated.md)
- [- updatePowerState](./iohidsystem/api-2544880-updatepowerstate.md)
- [- updateReport](./iohidsystem/api-3516601-updatereport.md)
- [- workspaceBounds](./iohidsystem/api-1645979-workspacebounds.md)
### Type Methods
- [+ doCreateShmem](./iohidsystem/api-1646004-docreateshmem.md)
- [+ doEvClose](./iohidsystem/api-1646030-doevclose.md)
- [+ doExtGetButtonEventNum](./iohidsystem/api-1645988-doextgetbuttoneventnum.md)
- [+ doExtGetStateForSelector](./iohidsystem/api-1646036-doextgetstateforselector.md)
- [+ doExtPostEvent](./iohidsystem/api-1646047-doextpostevent.md)
- [+ doExtSetMouseLocation](./iohidsystem/api-1646050-doextsetmouselocation.md)
- [+ doExtSetStateForSelector](./iohidsystem/api-1646075-doextsetstateforselector.md)
- [+ doKeyboardEvent](./iohidsystem/api-1646040-dokeyboardevent.md)
- [+ doKeyboardSpecialEvent](./iohidsystem/api-1646058-dokeyboardspecialevent.md)
- [+ doNewUserClient](./iohidsystem/api-1646065-donewuserclient.md)
- [+ doProcessKeyboardEQ](./iohidsystem/api-1646045-doprocesskeyboardeq.md)
- [+ doRegisterEventQueue](./iohidsystem/api-1646035-doregistereventqueue.md)
- [+ doRegisterScreen](./iohidsystem/api-1646017-doregisterscreen.md)
- [+ doSetContinuousCursorEnable](./iohidsystem/api-1646039-dosetcontinuouscursorenable.md)
- [+ doSetCursorEnable](./iohidsystem/api-1646012-dosetcursorenable.md)
- [+ doSetDisplayBounds](./iohidsystem/api-1645991-dosetdisplaybounds.md)
- [+ doSetParamPropertiesPost](./iohidsystem/api-1645978-dosetparampropertiespost.md)
- [+ doSetParamPropertiesPre](./iohidsystem/api-1646044-dosetparampropertiespre.md)
- [+ doUnregisterEventQueue](./iohidsystem/api-1646015-dounregistereventqueue.md)
- [+ doUnregisterScreen](./iohidsystem/api-1646085-dounregisterscreen.md)
- [+ doUpdateEventFlags](./iohidsystem/api-1646057-doupdateeventflags.md)
- [+ getUserHidActivityState](./iohidsystem/api-1646006-getuserhidactivitystate.md)
- [+ handlePublishNotification](./iohidsystem/api-1646074-handlepublishnotification.md)
- [+ handleTerminationNotification](./iohidsystem/api-2921472-handleterminationnotification.md)
- [+ instance](./iohidsystem/api-1645989-instance.md)
- [+ makeInt32ArrayParamProperty](./iohidsystem/api-1646086-makeint32arrayparamproperty.md)
- [+ makeNumberParamProperty](./iohidsystem/api-1646016-makenumberparamproperty.md)
- [+ powerStateHandler](./iohidsystem/api-2544879-powerstatehandler.md)
- [+ processKeyboardEQ](./iohidsystem/api-1645985-processkeyboardeq.md)
- [+ reportUserHidActivity](./iohidsystem/api-1646027-reportuserhidactivity.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### IOKit
- [IOUSBDevice](./iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](./iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](./api-1575304-ioofpathmatching.md)
- [IOUSBHostInterface](./iousbhostinterface.md)
- [IOUSBHostDevice](./iousbhostdevice.md)
- [IOUSBHostPipe](./iousbhostpipe.md)
- [IOUSBHostIOSource](./iousbhostiosource.md)
- [IOUSBHostStream](./iousbhoststream.md)
- [IOHIDEventDriver](./iohideventdriver.md)
- [IOHIDEventService](./iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDInterface](./iohidinterface.md)
  IOService represents an device or OS service in IOKit and DriverKit.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidsystem)*
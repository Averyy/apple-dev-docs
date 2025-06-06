# IOHIDSystem

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.15.4+ - Deprecated in 10.15.4

## Declaration

```swift
class IOHIDSystem : IOService
```

## Topics

### Instance Methods
- [- animateWaitCursor](iohidsystem/1646093-animatewaitcursor.md)
- [- attach](iohidsystem/1646018-attach.md)
- [- changeCursor](iohidsystem/1646067-changecursor.md)
- [- configureReport](iohidsystem/3516597-configurereport.md)
- [- createFilteredParamPropertiesForService](iohidsystem/1646048-createfilteredparampropertiesfor.md)
- [- createParameters](iohidsystem/1646064-createparameters.md)
- [- createShmem](iohidsystem/1646043-createshmem.md)
- [- createShmemGated](iohidsystem/1645992-createshmemgated.md)
- [- detach](iohidsystem/1646097-detach.md)
- [- disableContinuousCursor](iohidsystem/1646055-disablecontinuouscursor.md)
- [- dispatchEvent](iohidsystem/1646005-dispatchevent.md)
- [- doProcessNotifications](iohidsystem/1646070-doprocessnotifications.md)
- [- enableContinuousCursor](iohidsystem/1646063-enablecontinuouscursor.md)
- [- evClose](iohidsystem/1646002-evclose.md)
- [- evCloseGated](iohidsystem/1646091-evclosegated.md)
- [- evDispatch](iohidsystem/1646082-evdispatch.md)
- [- evOpen](iohidsystem/1646020-evopen.md)
- [- evOpenGated](iohidsystem/4191644-evopengated.md)
- [- eventFlags](iohidsystem/1645998-eventflags.md)
- [- extGetButtonEventNum](iohidsystem/1646071-extgetbuttoneventnum.md)
- [- extGetButtonEventNumGated](iohidsystem/1645984-extgetbuttoneventnumgated.md)
- [- extGetStateForSelector](iohidsystem/1646019-extgetstateforselector.md)
- [- extGetUserHidActivityState](iohidsystem/1646084-extgetuserhidactivitystate.md)
- [- extPostEvent](iohidsystem/1645983-extpostevent.md)
- [- extPostEventGated](iohidsystem/1646046-extposteventgated.md)
- [- extRegisterVirtualDisplay](iohidsystem/1646077-extregistervirtualdisplay.md)
- [- extSetBounds](iohidsystem/1646069-extsetbounds.md)
- [- extSetMouseLocation](iohidsystem/1646034-extsetmouselocation.md)
- [- extSetMouseLocationGated](iohidsystem/1646062-extsetmouselocationgated.md)
- [- extSetOnScreenBounds](iohidsystem/1646011-extsetonscreenbounds.md)
- [- extSetStateForSelector](iohidsystem/1646049-extsetstateforselector.md)
- [- extSetVirtualDisplayBounds](iohidsystem/1646022-extsetvirtualdisplaybounds.md)
- [- extUnregisterVirtualDisplay](iohidsystem/1645980-extunregistervirtualdisplay.md)
- [- free](iohidsystem/1646087-free.md)
- [- genericNotificationHandler](iohidsystem/1646073-genericnotificationhandler.md)
- [- getMetaClass](iohidsystem/1646079-getmetaclass.md)
- [- getUserHidActivityStateGated](iohidsystem/1646059-getuserhidactivitystategated.md)
- [- getWorkLoop](iohidsystem/1646076-getworkloop.md)
- [- hidActivityChecker](iohidsystem/1646000-hidactivitychecker.md)
- [- hideCursor](iohidsystem/1646061-hidecursor.md)
- [- hideWaitCursor](iohidsystem/1646066-hidewaitcursor.md)
- [- init](iohidsystem/1646024-init.md)
- [- initShmem](iohidsystem/1646026-initshmem.md)
- [- keyboardEvent](iohidsystem/1646037-keyboardevent.md)
- [- keyboardEvent](iohidsystem/3516598-keyboardevent.md)
- [- keyboardEventGated](iohidsystem/1646008-keyboardeventgated.md)
- [- keyboardSpecialEvent](iohidsystem/1646031-keyboardspecialevent.md)
- [- keyboardSpecialEvent](iohidsystem/3516599-keyboardspecialevent.md)
- [- keyboardSpecialEventGated](iohidsystem/1646025-keyboardspecialeventgated.md)
- [- message](iohidsystem/1646060-message.md)
- [- moveCursor](iohidsystem/1646080-movecursor.md)
- [- newUserClient](iohidsystem/1646033-newuserclient.md)
- [- newUserClientGated](iohidsystem/1646053-newuserclientgated.md)
- [- periodicEvents](iohidsystem/1645990-periodicevents.md)
- [- pointToScreen](iohidsystem/1646078-pointtoscreen.md)
- [- postEvent](iohidsystem/1645987-postevent.md)
- [- probe](iohidsystem/1646042-probe.md)
- [- registerEventQueue](iohidsystem/1646001-registereventqueue.md)
- [- registerEventQueueGated](iohidsystem/1646083-registereventqueuegated.md)
- [- registerEventSource](iohidsystem/1645995-registereventsource.md)
- [- registerScreen](iohidsystem/1646095-registerscreen.md)
- [- registerScreenGated](iohidsystem/1645981-registerscreengated.md)
- [- reportUserHidActivityGated](iohidsystem/1646041-reportuserhidactivitygated.md)
- [- resetCursor](iohidsystem/1646088-resetcursor.md)
- [- scheduleNextPeriodicEvent](iohidsystem/1646003-schedulenextperiodicevent.md)
- [- setBounds](iohidsystem/1646038-setbounds.md)
- [- setContinuousCursorEnable](iohidsystem/1645996-setcontinuouscursorenable.md)
- [- setContinuousCursorEnableGated](iohidsystem/1646032-setcontinuouscursorenablegated.md)
- [- setCursorEnable](iohidsystem/1645993-setcursorenable.md)
- [- setCursorEnableGated](iohidsystem/1646092-setcursorenablegated.md)
- [- setCursorPosition](iohidsystem/1646010-setcursorposition.md)
- [- setDisplayBoundsGated](iohidsystem/1646081-setdisplayboundsgated.md)
- [- setEventsEnable](iohidsystem/1646051-seteventsenable.md)
- [- setParamProperties](iohidsystem/1645982-setparamproperties.md)
- [- setParamPropertiesPostGated](iohidsystem/1646023-setparampropertiespostgated.md)
- [- setParamPropertiesPreGated](iohidsystem/1646096-setparampropertiespregated.md)
- [- setProperties](iohidsystem/1645999-setproperties.md)
- [- showCursor](iohidsystem/1646054-showcursor.md)
- [- showWaitCursor](iohidsystem/1645977-showwaitcursor.md)
- [- sleepDisplayTickle](iohidsystem/2544881-sleepdisplaytickle.md)
- [- start](iohidsystem/1646007-start.md)
- [- startCursor](iohidsystem/1646009-startcursor.md)
- [- unregisterEventQueue](iohidsystem/1646068-unregistereventqueue.md)
- [- unregisterEventQueueGated](iohidsystem/1646090-unregistereventqueuegated.md)
- [- unregisterScreen](iohidsystem/1646028-unregisterscreen.md)
- [- unregisterScreenGated](iohidsystem/1645997-unregisterscreengated.md)
- [- updateEventFlags](iohidsystem/1646089-updateeventflags.md)
- [- updateEventFlags](iohidsystem/3516600-updateeventflags.md)
- [- updateEventFlagsGated](iohidsystem/1646056-updateeventflagsgated.md)
- [- updateHidActivity](iohidsystem/1646052-updatehidactivity.md)
- [- updateParamPropertiesGated](iohidsystem/1646094-updateparampropertiesgated.md)
- [- updatePowerState](iohidsystem/2544880-updatepowerstate.md)
- [- updateReport](iohidsystem/3516601-updatereport.md)
- [- workspaceBounds](iohidsystem/1645979-workspacebounds.md)
### Type Methods
- [+ doCreateShmem](iohidsystem/1646004-docreateshmem.md)
- [+ doEvClose](iohidsystem/1646030-doevclose.md)
- [+ doExtGetButtonEventNum](iohidsystem/1645988-doextgetbuttoneventnum.md)
- [+ doExtGetStateForSelector](iohidsystem/1646036-doextgetstateforselector.md)
- [+ doExtPostEvent](iohidsystem/1646047-doextpostevent.md)
- [+ doExtSetMouseLocation](iohidsystem/1646050-doextsetmouselocation.md)
- [+ doExtSetStateForSelector](iohidsystem/1646075-doextsetstateforselector.md)
- [+ doKeyboardEvent](iohidsystem/1646040-dokeyboardevent.md)
- [+ doKeyboardSpecialEvent](iohidsystem/1646058-dokeyboardspecialevent.md)
- [+ doNewUserClient](iohidsystem/1646065-donewuserclient.md)
- [+ doProcessKeyboardEQ](iohidsystem/1646045-doprocesskeyboardeq.md)
- [+ doRegisterEventQueue](iohidsystem/1646035-doregistereventqueue.md)
- [+ doRegisterScreen](iohidsystem/1646017-doregisterscreen.md)
- [+ doSetContinuousCursorEnable](iohidsystem/1646039-dosetcontinuouscursorenable.md)
- [+ doSetCursorEnable](iohidsystem/1646012-dosetcursorenable.md)
- [+ doSetDisplayBounds](iohidsystem/1645991-dosetdisplaybounds.md)
- [+ doSetParamPropertiesPost](iohidsystem/1645978-dosetparampropertiespost.md)
- [+ doSetParamPropertiesPre](iohidsystem/1646044-dosetparampropertiespre.md)
- [+ doUnregisterEventQueue](iohidsystem/1646015-dounregistereventqueue.md)
- [+ doUnregisterScreen](iohidsystem/1646085-dounregisterscreen.md)
- [+ doUpdateEventFlags](iohidsystem/1646057-doupdateeventflags.md)
- [+ getUserHidActivityState](iohidsystem/1646006-getuserhidactivitystate.md)
- [+ handlePublishNotification](iohidsystem/1646074-handlepublishnotification.md)
- [+ handleTerminationNotification](iohidsystem/2921472-handleterminationnotification.md)
- [+ instance](iohidsystem/1645989-instance.md)
- [+ makeInt32ArrayParamProperty](iohidsystem/1646086-makeint32arrayparamproperty.md)
- [+ makeNumberParamProperty](iohidsystem/1646016-makenumberparamproperty.md)
- [+ powerStateHandler](iohidsystem/2544879-powerstatehandler.md)
- [+ processKeyboardEQ](iohidsystem/1645985-processkeyboardeq.md)
- [+ reportUserHidActivity](iohidsystem/1646027-reportuserhidactivity.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iohidsystem)*
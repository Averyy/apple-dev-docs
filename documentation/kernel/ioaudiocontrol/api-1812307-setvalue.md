# setValue

**Framework**: Kernel  
**Kind**: instm

Sets the value for this control.

## Declaration

```swift
virtual IOReturn setValue(
 OSObject *newValue);
```

#### Return_value

Returns kIOReturnSuccess if the value is successfully set.

#### Overview

When the control's value is changed, a call is made to performValueChange(). If that call succeeds, the value is set and sendValueChangeNotification() is called to send a notification to the user clients. This function must be called on the IOWorkLoop.

## Parameters

- `newValue`: The new value for this control.

## See Also

- [addUserClient](ioaudiocontrol/1812069-adduserclient.md)
  Called on the IOWorkLoop to add a new IOAudioControlUserClient.
- [addUserClientAction](ioaudiocontrol/1812079-adduserclientaction.md)
  IOCommandGate Action which calls addUserClient() while holding the IOCommandGate.
- [clientClosed](ioaudiocontrol/1812087-clientclosed.md)
  Called automatically by the IOAudioControlUserClient when a user client closes its connection to the control.
- [createUserClient(task_t, void *, UInt32, IOAudioControlUserClient **)](ioaudiocontrol/1812095-createuserclient.md)
  Creates a new IOAudioControlUserClient instance.
- [createUserClient(task_t, void *, UInt32, IOAudioControlUserClient **, OSDictionary *)](ioaudiocontrol/1812104-createuserclient.md)
  Creates a new IOAudioControlUserClient instance.
- [detachUserClientsAction](ioaudiocontrol/1812113-detachuserclientsaction.md)
- [flushValue](ioaudiocontrol/1812123-flushvalue.md)
  Forces the control to be flushed out to the hardware.
- [free](ioaudiocontrol/1812130-free.md)
  Frees all of the resources allocated by the IOAudioControl.
- [getChannelID](ioaudiocontrol/1812135-getchannelid.md)
  Returns the channel ID for the control.
- [getCommandGate](ioaudiocontrol/1812146-getcommandgate.md)
  Returns the IOCommandGate for this IOAudioControl.
- [getControlID](ioaudiocontrol/1812156-getcontrolid.md)
  Returns the control ID for the control.
- [getIsStarted](ioaudiocontrol/1812169-getisstarted.md)
  Returns true after start() has been called.
- [getValue](ioaudiocontrol/1812181-getvalue.md)
  Returns the current value of the control.
- [getWorkLoop](ioaudiocontrol/1812197-getworkloop.md)
  Returns the IOWorkLoop for the whole audio driver.
- [hardwareValueChanged](ioaudiocontrol/1812208-hardwarevaluechanged.md)
  Updates the value for this control and sends out the value changed notification.
- [init](ioaudiocontrol/1812219-init.md)
  Initializes a newly allocated IOAudioControl with the given attributes.
- [newUserClient](ioaudiocontrol/1812229-newuserclient.md)
  Creates a new user client object for this IOAudioControl instance.
- [performValueChange](ioaudiocontrol/1812237-performvaluechange.md)
  Called by setValue() to make the call to the valueChangeHandler to update the hardware.
- [removeUserClient](ioaudiocontrol/1812247-removeuserclient.md)
  Called on the IOWorkLoop to remove an IOAudioControlUserClient.
- [removeUserClientAction](ioaudiocontrol/1812259-removeuserclientaction.md)
  IOCommandGate Action which calls removeUserClient() while holding the IOCommandGate.
- [sendValueChangeNotification](ioaudiocontrol/1812267-sendvaluechangenotification.md)
  Called when the value has changed for the control.
- [setChannelID](ioaudiocontrol/1812275-setchannelid.md)
  Called at init time to set the channel ID for this IOAudioControl.
- [setChannelName](ioaudiocontrol/1812281-setchannelname.md)
  Called at init time to set the channel name for this IOAudioControl.
- [setControlID](ioaudiocontrol/1812283-setcontrolid.md)
  Sets the controlID for this control.
- [setProperties](ioaudiocontrol/1812287-setproperties.md)
  Changes a property of this IOService.
- [setReadOnlyFlag](ioaudiocontrol/1812291-setreadonlyflag.md)
  Call this function to say that a control is read only. This call cannot be undone, so if a control is only temporarily unsetable, do not use this call but instead return an error from the control handler.
- [setSubType(UInt32)](ioaudiocontrol/1812293-setsubtype.md)
  Called at init time to set the control type.
- [setType(UInt32)](ioaudiocontrol/1812300-settype.md)
  Called at init time to set the control type.
- [setUsage](ioaudiocontrol/1812305-setusage.md)
  Called at init time to set the control usage.
- [setValueAction](ioaudiocontrol/1812310-setvalueaction.md)
  IOCommandGate Action which calls setValue() while holding the IOCommandGate.
- [start](ioaudiocontrol/1812313-start.md)
  Starts a newly created IOAudioControl.
- [stop](ioaudiocontrol/1812316-stop.md)
  Stops the control when the provider is going away.
- [updateValue](ioaudiocontrol/1812319-updatevalue.md)
  Called by setValue() in order to update the value and the registry.
- [validateValue](ioaudiocontrol/1812322-validatevalue.md)
  Called by setValue() to verify that the value is valid.
- [withAttributes](ioaudiocontrol/1812328-withattributes.md)
  Static function that allocates a new IOAudioControl with the given attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiocontrol/1812307-setvalue)*
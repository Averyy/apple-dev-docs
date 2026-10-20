# IOAudioControl

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Represents any controllable attribute of an IOAudioDevice.

**Availability**:
- macOS 10.1+

## Declaration

```cpp
class IOAudioControl : IOService
```

#### Overview

An IOAudioControl instance may belong to one IOAudioPort. Additionally, it may associated with an IOAudioEngine as a default control for that IOAudioEngine.

When its value changes, it sends a notification to the CoreAudio.framework (HAL). It also makes a call to the ValueChangeHandler.

The base IOAudioControl class contains a type, a value and a channel ID representing the channel(s) which the control acts on. It may also contain a readable format for the name of the channel as well as a control ID that can be used to identify unique controls. Additionally it may contain a subType and a usage. Each type has its own set of possible subTypes. There currently four different control types defined: kIOAudioControlTypeLevel, kIOAudioControlTypeToggle, kIOAudioControlTypeSelector. Each one is represented by a subclass of IOAudioControl: IOAudioLevelControl, IOAudioToggleControl, IOAudioSelectorControl. The level control defines a range of allowed values and has a defined subtype of kIOAudioLevelControlSubTypeVolume used to define a volume control. The toggle control allows for a boolean value and has a defined subtype kIOAudioToggleControlSubTypeMute for a mute control. The selector control has a list of allowed selections with a value and description for each allowed selection and has the following sub types: kIOAudioSelectorControlSubTypeOutput for an output selector and kIOAudioSelectorControlSubTypeInput for an input selector. See the subclass documentation for a more complete description of each

There are enums for default channel ID values and common channel names in IOAudioTypes.h. The channel ID values are prefixed with 'kIOAudioControlChannelID' and the common channel names are prefixed with 'kIOAudioControlChannelName'. All of the attributes of the IOAudioControl are stored in the registry. The key used for each attribute is defined in IOAudioTypes.h with the define matching the following pattern: 'kIOAudioControl<attribute name>Key'. For example: kIOAudioControlChannelIDKey.

In addition to the existing defined control types, drivers can define their own as well for other purposes.

Changes to the IOAudioControl's value made by the CoreAudio.framework are done through the IORegistry. When the CoreAudio.framework initiates a value change, the control receives a setProperties() message. The setProperties() implementation looks for the property 'IOAudioControlValue' and if present, calls setValue() on the driver's IOWorkLoop with the new value. The setValue() function first checks to see if the new value is different. If so, it calls performValueChange() to call through to the driver to make the change in the hardware. If that call succeeds the value is changed and the new value is set in the registry. Additionally notifications are sent to all clients that have registered for them.

## Topics

### Miscellaneous
- [addUserClient](./ioaudiocontrol/api-1812069-adduserclient.md)
  Called on the IOWorkLoop to add a new IOAudioControlUserClient.
- [addUserClientAction](./ioaudiocontrol/api-1812079-adduserclientaction.md)
  IOCommandGate Action which calls addUserClient() while holding the IOCommandGate.
- [clientClosed](./ioaudiocontrol/api-1812087-clientclosed.md)
  Called automatically by the IOAudioControlUserClient when a user client closes its connection to the control.
- [createUserClient(task_t, void *, UInt32, IOAudioControlUserClient **)](./ioaudiocontrol/api-1812095-createuserclient.md)
  Creates a new IOAudioControlUserClient instance.
- [createUserClient(task_t, void *, UInt32, IOAudioControlUserClient **, OSDictionary *)](./ioaudiocontrol/api-1812104-createuserclient.md)
  Creates a new IOAudioControlUserClient instance.
- [detachUserClientsAction](./ioaudiocontrol/api-1812113-detachuserclientsaction.md)
- [flushValue](./ioaudiocontrol/api-1812123-flushvalue.md)
  Forces the control to be flushed out to the hardware.
- [free](./ioaudiocontrol/api-1812130-free.md)
  Frees all of the resources allocated by the IOAudioControl.
- [getChannelID](./ioaudiocontrol/api-1812135-getchannelid.md)
  Returns the channel ID for the control.
- [getCommandGate](./ioaudiocontrol/api-1812146-getcommandgate.md)
  Returns the IOCommandGate for this IOAudioControl.
- [getControlID](./ioaudiocontrol/api-1812156-getcontrolid.md)
  Returns the control ID for the control.
- [getIsStarted](./ioaudiocontrol/api-1812169-getisstarted.md)
  Returns true after start() has been called.
- [getValue](./ioaudiocontrol/api-1812181-getvalue.md)
  Returns the current value of the control.
- [getWorkLoop](./ioaudiocontrol/api-1812197-getworkloop.md)
  Returns the IOWorkLoop for the whole audio driver.
- [hardwareValueChanged](./ioaudiocontrol/api-1812208-hardwarevaluechanged.md)
  Updates the value for this control and sends out the value changed notification.
- [init](./ioaudiocontrol/api-1812219-init.md)
  Initializes a newly allocated IOAudioControl with the given attributes.
- [newUserClient](./ioaudiocontrol/api-1812229-newuserclient.md)
  Creates a new user client object for this IOAudioControl instance.
- [performValueChange](./ioaudiocontrol/api-1812237-performvaluechange.md)
  Called by setValue() to make the call to the valueChangeHandler to update the hardware.
- [removeUserClient](./ioaudiocontrol/api-1812247-removeuserclient.md)
  Called on the IOWorkLoop to remove an IOAudioControlUserClient.
- [removeUserClientAction](./ioaudiocontrol/api-1812259-removeuserclientaction.md)
  IOCommandGate Action which calls removeUserClient() while holding the IOCommandGate.
- [sendValueChangeNotification](./ioaudiocontrol/api-1812267-sendvaluechangenotification.md)
  Called when the value has changed for the control.
- [setChannelID](./ioaudiocontrol/api-1812275-setchannelid.md)
  Called at init time to set the channel ID for this IOAudioControl.
- [setChannelName](./ioaudiocontrol/api-1812281-setchannelname.md)
  Called at init time to set the channel name for this IOAudioControl.
- [setControlID](./ioaudiocontrol/api-1812283-setcontrolid.md)
  Sets the controlID for this control.
- [setProperties](./ioaudiocontrol/api-1812287-setproperties.md)
  Changes a property of this IOService.
- [setReadOnlyFlag](./ioaudiocontrol/api-1812291-setreadonlyflag.md)
  Call this function to say that a control is read only. This call cannot be undone, so if a control is only temporarily unsetable, do not use this call but instead return an error from the control handler.
- [setSubType(UInt32)](./ioaudiocontrol/api-1812293-setsubtype.md)
  Called at init time to set the control type.
- [setType(UInt32)](./ioaudiocontrol/api-1812300-settype.md)
  Called at init time to set the control type.
- [setUsage](./ioaudiocontrol/api-1812305-setusage.md)
  Called at init time to set the control usage.
- [setValue](./ioaudiocontrol/api-1812307-setvalue.md)
  Sets the value for this control.
- [setValueAction](./ioaudiocontrol/api-1812310-setvalueaction.md)
  IOCommandGate Action which calls setValue() while holding the IOCommandGate.
- [start](./ioaudiocontrol/api-1812313-start.md)
  Starts a newly created IOAudioControl.
- [stop](./ioaudiocontrol/api-1812316-stop.md)
  Stops the control when the provider is going away.
- [updateValue](./ioaudiocontrol/api-1812319-updatevalue.md)
  Called by setValue() in order to update the value and the registry.
- [validateValue](./ioaudiocontrol/api-1812322-validatevalue.md)
  Called by setValue() to verify that the value is valid.
- [withAttributes](./ioaudiocontrol/api-1812328-withattributes.md)
  Static function that allocates a new IOAudioControl with the given attributes.
### Callbacks
- [IntValueChangeHandler](./ioaudiocontrol/intvaluechangehandler.md)
  Handler function used to make a notification when a value is to be changed.
### Instance Variables
- [workLoop](./ioaudiocontrol/workloop.md)
- [userClients](./ioaudiocontrol/userclients.md)
- [isStarted](./ioaudiocontrol/isstarted.md)
- [controlID](./ioaudiocontrol/controlid.md)
- [commandGate](./ioaudiocontrol/commandgate.md)
- [channelID](./ioaudiocontrol/channelid.md)
### Instance Methods
- [- addUserClient](./ioaudiocontrol/api-1485871-adduserclient.md)
- [- attachAndStart](./ioaudiocontrol/api-1485811-attachandstart.md)
- [- clientClosed](./ioaudiocontrol/api-1485815-clientclosed.md)
- [- createUserClient](./ioaudiocontrol/api-1485832-createuserclient.md)
- [- createUserClient](./ioaudiocontrol/api-3516514-createuserclient.md)
- [- detachUserClients](./ioaudiocontrol/api-1485893-detachuserclients.md)
- [- flushValue](./ioaudiocontrol/api-1485879-flushvalue.md)
- [- free](./ioaudiocontrol/api-1485856-free.md)
- [- getChannelID](./ioaudiocontrol/api-1485850-getchannelid.md)
- [- getCommandGate](./ioaudiocontrol/api-1485859-getcommandgate.md)
- [- getControlID](./ioaudiocontrol/api-1485824-getcontrolid.md)
- [- getDataBytes](./ioaudiocontrol/api-1485848-getdatabytes.md)
- [- getDataLength](./ioaudiocontrol/api-1485904-getdatalength.md)
- [- getIntValue](./ioaudiocontrol/api-1485853-getintvalue.md)
- [- getIsStarted](./ioaudiocontrol/api-1485813-getisstarted.md)
- [- getMetaClass](./ioaudiocontrol/api-1485887-getmetaclass.md)
- [- getSubType](./ioaudiocontrol/api-1485910-getsubtype.md)
- [- getType](./ioaudiocontrol/api-1485908-gettype.md)
- [- getUsage](./ioaudiocontrol/api-1485873-getusage.md)
- [- getValue](./ioaudiocontrol/api-1485838-getvalue.md)
- [- getWorkLoop](./ioaudiocontrol/api-1485912-getworkloop.md)
- [- hardwareValueChanged](./ioaudiocontrol/api-1485883-hardwarevaluechanged.md)
- [- init](./ioaudiocontrol/api-1485826-init.md)
- [- newUserClient](./ioaudiocontrol/api-1485889-newuserclient.md)
- [- newUserClient](./ioaudiocontrol/api-3516515-newuserclient.md)
- [- performValueChange](./ioaudiocontrol/api-1485899-performvaluechange.md)
- [- removeUserClient](./ioaudiocontrol/api-1485809-removeuserclient.md)
- [- sendChangeNotification](./ioaudiocontrol/api-1485830-sendchangenotification.md)
- [- sendQueuedNotifications](./ioaudiocontrol/api-1485918-sendqueuednotifications.md)
- [- sendValueChangeNotification](./ioaudiocontrol/api-1485819-sendvaluechangenotification.md)
- [- setChannelID](./ioaudiocontrol/api-1485917-setchannelid.md)
- [- setChannelName](./ioaudiocontrol/api-1485865-setchannelname.md)
- [- setChannelNumber](./ioaudiocontrol/api-1485861-setchannelnumber.md)
- [- setControlID](./ioaudiocontrol/api-1485846-setcontrolid.md)
- [- setCoreAudioPropertyID](./ioaudiocontrol/api-1485844-setcoreaudiopropertyid.md)
- [- setProperties](./ioaudiocontrol/api-1485840-setproperties.md)
- [- setReadOnlyFlag](./ioaudiocontrol/api-1485875-setreadonlyflag.md)
- [- setSubType](./ioaudiocontrol/api-1485916-setsubtype.md)
- [- setType](./ioaudiocontrol/api-1485897-settype.md)
- [- setUsage](./ioaudiocontrol/api-1485816-setusage.md)
- [- setValue](./ioaudiocontrol/api-1485842-setvalue.md)
- [- setValue](./ioaudiocontrol/api-3516516-setvalue.md)
- [- setValueChangeHandler](./ioaudiocontrol/api-1485869-setvaluechangehandler.md)
- [- setValueChangeHandler](./ioaudiocontrol/api-3516517-setvaluechangehandler.md)
- [- setValueChangeHandler](./ioaudiocontrol/api-3516518-setvaluechangehandler.md)
- [- setValueChangeTarget](./ioaudiocontrol/api-1485876-setvaluechangetarget.md)
- [- setWorkLoop](./ioaudiocontrol/api-1485901-setworkloop.md)
- [- start](./ioaudiocontrol/api-1485891-start.md)
- [- stop](./ioaudiocontrol/api-1485836-stop.md)
- [- updateValue](./ioaudiocontrol/api-1485881-updatevalue.md)
- [- validateValue](./ioaudiocontrol/api-1485914-validatevalue.md)
### Type Methods
- [+ addUserClientAction](./ioaudiocontrol/api-1485863-adduserclientaction.md)
- [+ detachUserClientsAction](./ioaudiocontrol/api-1485822-detachuserclientsaction.md)
- [+ removeUserClientAction](./ioaudiocontrol/api-1485895-removeuserclientaction.md)
- [+ setCommandGateUsage](./ioaudiocontrol/api-1485867-setcommandgateusage.md)
- [+ setValueAction](./ioaudiocontrol/api-1485834-setvalueaction.md)
- [+ withAttributes](./ioaudiocontrol/api-1485828-withattributes.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Interfaces
- [IOAudioLevelControl](./ioaudiolevelcontrol.md)
- [IOAudioSelectorControl](./ioaudioselectorcontrol.md)
- [IOAudioToggleControl](./ioaudiotogglecontrol.md)
- [IOAudioEngine](./ioaudioengine.md)
  Abstract base class for a single audio audio / I/O engine.
- [IOAudioStream](./ioaudiostream.md)
  This class wraps a single sample buffer in an audio driver.
- [IOAudioPort](./ioaudioport.md)
  Represents a logical or physical port or functional unit in an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiocontrol)*
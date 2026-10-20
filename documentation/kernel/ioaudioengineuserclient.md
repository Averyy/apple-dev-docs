# IOAudioEngineUserClient

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.1+

## Declaration

```cpp
class IOAudioEngineUserClient : IOUserClient
```

## Topics

### Instance Methods
- [- clientClose](./ioaudioengineuserclient/api-1495608-clientclose.md)
- [- clientDied](./ioaudioengineuserclient/api-1495593-clientdied.md)
- [- clientMemoryForType](./ioaudioengineuserclient/api-1495596-clientmemoryfortype.md)
- [- clientStart](./ioaudioengineuserclient/api-1495585-clientstart.md)
- [- clientStop](./ioaudioengineuserclient/api-1495532-clientstop.md)
- [- closeClient](./ioaudioengineuserclient/api-1495590-closeclient.md)
- [- externalMethod](./ioaudioengineuserclient/api-1495551-externalmethod.md)
- [- findBufferSet](./ioaudioengineuserclient/api-1495519-findbufferset.md)
- [- findExtendedInfo](./ioaudioengineuserclient/api-1495543-findextendedinfo.md)
- [- findExtendedInfo64](./ioaudioengineuserclient/api-1495533-findextendedinfo64.md)
- [- free](./ioaudioengineuserclient/api-1495480-free.md)
- [- freeClientBuffer](./ioaudioengineuserclient/api-1495513-freeclientbuffer.md)
- [- freeClientBufferSetList](./ioaudioengineuserclient/api-1495502-freeclientbuffersetlist.md)
- [- getClientNearestStartTime](./ioaudioengineuserclient/api-1495499-getclientneareststarttime.md)
- [- getConnectionID](./ioaudioengineuserclient/api-1495609-getconnectionid.md)
- [- getExternalMethodForIndex](./ioaudioengineuserclient/api-1495558-getexternalmethodforindex.md)
- [- getExternalTrapForIndex](./ioaudioengineuserclient/api-1495570-getexternaltrapforindex.md)
- [- getMetaClass](./ioaudioengineuserclient/api-1495613-getmetaclass.md)
- [- getNearestStartTime](./ioaudioengineuserclient/api-1495478-getneareststarttime.md)
- [- initWithAudioEngine](./ioaudioengineuserclient/api-1495515-initwithaudioengine.md)
- [- initWithAudioEngine](./ioaudioengineuserclient/api-3516526-initwithaudioengine.md)
- [- isOnline](./ioaudioengineuserclient/api-1495497-isonline.md)
- [- lockBuffers](./ioaudioengineuserclient/api-1495577-lockbuffers.md)
- [- performClientIO](./ioaudioengineuserclient/api-1495550-performclientio.md)
- [- performClientInput](./ioaudioengineuserclient/api-1495619-performclientinput.md)
- [- performClientOutput](./ioaudioengineuserclient/api-1495603-performclientoutput.md)
- [- performWatchdogOutput](./ioaudioengineuserclient/api-1495600-performwatchdogoutput.md)
- [- registerBuffer](./ioaudioengineuserclient/api-1495561-registerbuffer.md)
- [- registerBuffer64](./ioaudioengineuserclient/api-1495504-registerbuffer64.md)
- [- registerClientBuffer](./ioaudioengineuserclient/api-1495517-registerclientbuffer.md)
- [- registerClientBuffer64](./ioaudioengineuserclient/api-1495522-registerclientbuffer64.md)
- [- registerClientParameterBuffer](./ioaudioengineuserclient/api-1495572-registerclientparameterbuffer.md)
- [- registerNotification](./ioaudioengineuserclient/api-1495492-registernotification.md)
- [- registerNotificationPort](./ioaudioengineuserclient/api-1495490-registernotificationport.md)
- [- removeBufferSet](./ioaudioengineuserclient/api-1495524-removebufferset.md)
- [- safeRegisterClientBuffer](./ioaudioengineuserclient/api-1495568-saferegisterclientbuffer.md)
- [- safeRegisterClientBuffer64](./ioaudioengineuserclient/api-1495553-saferegisterclientbuffer64.md)
- [- sendFormatChangeNotification](./ioaudioengineuserclient/api-1495487-sendformatchangenotification.md)
- [- sendNotification](./ioaudioengineuserclient/api-1495614-sendnotification.md)
- [- setOnline](./ioaudioengineuserclient/api-1495495-setonline.md)
- [- startClient](./ioaudioengineuserclient/api-1495582-startclient.md)
- [- stop](./ioaudioengineuserclient/api-1495488-stop.md)
- [- stopClient](./ioaudioengineuserclient/api-1495540-stopclient.md)
- [- unlockBuffers](./ioaudioengineuserclient/api-1495621-unlockbuffers.md)
- [- unregisterBuffer](./ioaudioengineuserclient/api-1495560-unregisterbuffer.md)
- [- unregisterBuffer64](./ioaudioengineuserclient/api-1495556-unregisterbuffer64.md)
- [- unregisterClientBuffer](./ioaudioengineuserclient/api-1495544-unregisterclientbuffer.md)
- [- unregisterClientBuffer64](./ioaudioengineuserclient/api-1495595-unregisterclientbuffer64.md)
### Type Methods
- [+ closeClientAction](./ioaudioengineuserclient/api-1495474-closeclientaction.md)
- [+ getNearestStartTimeAction](./ioaudioengineuserclient/api-1495507-getneareststarttimeaction.md)
- [+ registerBufferAction](./ioaudioengineuserclient/api-1495546-registerbufferaction.md)
- [+ registerNotificationAction](./ioaudioengineuserclient/api-1495575-registernotificationaction.md)
- [+ setCommandGateUsage](./ioaudioengineuserclient/api-1495586-setcommandgateusage.md)
- [+ startClientAction](./ioaudioengineuserclient/api-1495574-startclientaction.md)
- [+ stopClientAction](./ioaudioengineuserclient/api-1495483-stopclientaction.md)
- [+ unregisterBufferAction](./ioaudioengineuserclient/api-1495584-unregisterbufferaction.md)
- [+ withAudioEngine](./ioaudioengineuserclient/api-1495494-withaudioengine.md)
- [+ withAudioEngine](./ioaudioengineuserclient/api-3516527-withaudioengine.md)

## Relationships

### Inherits From
- [IOUserClient](./iouserclient.md)

## See Also

### User-Space Access
- [IOAudioControlUserClient](./ioaudiocontroluserclient.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioengineuserclient)*
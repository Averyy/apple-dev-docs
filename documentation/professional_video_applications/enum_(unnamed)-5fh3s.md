# enum (unnamed)

**Framework**: Professional Video Applications  
**Kind**: enum  
**Role**: Enumeration

Errors returned by plug-in hosts applications.

## Declaration

```c
enum: unsigned int;
```

## Topics

### Constants
- [var kFxError_AnalysisError: Int](./kfxerror_analysiserror.md)
  An error with analysis occurred.
- [var kFxError_AnalysisExtensionNotFound: Int](./kfxerror_analysisextensionnotfound.md)
  An error that indicates Analysis extension is not found.
- [var kFxError_APIUnavailable: Int](./kfxerror_apiunavailable.md)
  An error that indicates that the requested API cannot be used by the plug-in at this time.
- [var kFxError_CommandNotProcessed: Int](./kfxerror_commandnotprocessed.md)
  An error that indicates that the command sent to the `FxCommandAPI` is unable to complete.
- [var kFxError_HostUnreachable: Int](./kfxerror_hostunreachable.md)
  An error that indicates that the host application cannot be reached to complete an operation.
- [var kFxError_InvalidColorGamut: Int](./kfxerror_invalidcolorgamut.md)
  An Error that indicates that an attempt to get color gamut info from the host failed.
- [var kFxError_InvalidDataLength: Int](./kfxerror_invaliddatalength.md)
  An error that indicates an invalid data length was found by the plug-in while the host or framework was decoding data.
- [var kFxError_InvalidKeyframeIndex: Int](./kfxerror_invalidkeyframeindex.md)
  An error that indicates that the plug-in passed an invalid keyframe index to the host.
- [var kFxError_InvalidLightAccess: Int](./kfxerror_invalidlightaccess.md)
  An error that indicates that an attempt was made by the plug-in to access lights without first requesting light access.
- [var kFxError_InvalidParameter: Int](./kfxerror_invalidparameter.md)
  An error that indicates that a parameter sent by the caller to an API method was invalid.
- [var kFxError_InvalidParameterChannelIndex: Int](./kfxerror_invalidparameterchannelindex.md)
  An error that indicates that the plug-in passed an invalid channel number for a parameter to the host.
- [var kFxError_InvalidParameterID: Int](./kfxerror_invalidparameterid.md)
  An error that indicates that the plug-in passed an invalid parameter to the host.
- [var kFxError_InvalidPathID: Int](./kfxerror_invalidpathid.md)
  An error that indicates that no path with that ID exists.
- [var kFxError_InvalidPathIndex: Int](./kfxerror_invalidpathindex.md)
  An error that indicates that the index is greater than the number of paths.
- [var kFxError_InvalidPaths: Int](./kfxerror_invalidpaths.md)
  An error that indicates that an attempt to get path info from the host failed.
- [var kFxError_InvalidPathStyle: Int](./kfxerror_invalidpathstyle.md)
  An error that indicates that an invalid path style was used by the plug-in.
- [var kFxError_InvalidSegmentIndex: Int](./kfxerror_invalidsegmentindex.md)
  An error that indicates that the index of the segment of the path is greater than the number of segments in the path.
- [var kFxError_InvalidTime: Int](./kfxerror_invalidtime.md)
  An error that indicates that the plug-in passed an invalid time to the host.
- [var kFxError_InvalidTiming: Int](./kfxerror_invalidtiming.md)
  An error that indicates that an attempt to get timing info from the host failed.
- [var kFxError_LostConnectionToPlugin: Int](./kfxerror_lostconnectiontoplugin.md)
  An error that indicates that the connection between the host and the plug-in was lost.
- [var kFxError_MemoryNotAllocated: Int](./kfxerror_memorynotallocated.md)
  An error that indicates unable to free a memory resource because it is not allocated.
- [var kFxError_NoDocumentFound: Int](./kfxerror_nodocumentfound.md)
  An error that indicates that the FxPlug is not in a project.
- [var kFxError_NoMediaFolder: Int](./kfxerror_nomediafolder.md)
  An error that indicates that the project has no media folder.
- [var kFxError_NotYetImplemented: Int](./kfxerror_notyetimplemented.md)
  An error that indicates that the host application has not yet implemented the API.
- [var kFxError_NoViewFound: Int](./kfxerror_noviewfound.md)
  An error that indicates that a constant that indicates the remote window view wasn’t retrieved by the host.
- [var kFxError_OpenGLError: Int](./kfxerror_openglerror.md)
  An error that indicates that OpenGL returned an error.
- [var kFxError_OutOfMemory: Int](./kfxerror_outofmemory.md)
  An error that indicates unable to allocate memory.
- [var kFxError_PluginNotFound: Int](./kfxerror_pluginnotfound.md)
  An error that indicates that the host couldn’t find the plug-in.
- [var kFxError_Success: Int](./kfxerror_success.md)
  No error occurred.
- [var kFxError_ThirdPartyDeveloperStart: Int](./kfxerror_thirdpartydeveloperstart.md)
  All third-party error values must be greater than or equal to this value.
- [var kFxError_UnableToCreateDynamicRegistrationEndpoint: Int](./kfxerror_unabletocreatedynamicregistrationendpoint.md)
  An error that indicates that the XPC service was unable to create a new XPC Listener Endpoint for communication with the host application.
- [var kFxError_UnableToInstantiateDynamicRegistrar: Int](./kfxerror_unabletoinstantiatedynamicregistrar.md)
  An error that indicates that the XPC service was unable to instantiate a dynamic registrar object.
- [var kFxError_UnableToMovePlayhead: Int](./kfxerror_unabletomoveplayhead.md)
  An error that indicates that an attempt by the host to move the playhead failed.
- [var kFxError_UserCancelled: Int](./kfxerror_usercancelled.md)
  An error that indicates that an analysis operation was canceled by the user.
- [var kFxError_UnableToObtainProjectAspectRatio: Int](./kfxerror_unabletoobtainprojectaspectratio.md)
  An error that indicates that the host couldn’t obtain the project’s aspect ratio.

## See Also

### Anonymous enumerations
- [enum (unnamed)](./enum_%28unnamed%29-14vbr.md)
  The field order.
- [enum (unnamed)](./enum_%28unnamed%29-187sa.md)
- [enum (unnamed)](./enum_%28unnamed%29-1tjh8.md)
  The possible states of analysis, as reported by the host application when queried with [`analysisStateForEffect()`](./fxanalysisapi/analysisstateforeffect%28%29.md).
- [enum (unnamed)](./enum_%28unnamed%29-2epbe.md)
- [enum (unnamed)](./enum_%28unnamed%29-35krj.md)
  The path blend mode.
- [enum (unnamed)](./enum_%28unnamed%29-3fxly.md)
  The bit-depth
- [enum (unnamed)](./enum_%28unnamed%29-3hmov.md)
  The render quality.
- [enum (unnamed)](./enum_%28unnamed%29-424rv.md)
- [enum (unnamed)](./enum_%28unnamed%29-5key8.md)
- [enum (unnamed)](./enum_%28unnamed%29-5ml7h.md)
- [enum (unnamed)](./enum_%28unnamed%29-5r2wt.md)
  Constants used to describe a set of color primaries.
- [enum (unnamed)](./enum_%28unnamed%29-5zg4z.md)
- [enum (unnamed)](./enum_%28unnamed%29-74key.md)
- [enum (unnamed)](./enum_%28unnamed%29-7b48r.md)
- [enum (unnamed)](./enum_%28unnamed%29-7jahq.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/enum_(unnamed)-5fh3s)*
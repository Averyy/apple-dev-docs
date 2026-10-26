# Web Services

**Framework**: Core Services  
**Role**: API Collection

## Topics

### Constants
- [kWSDebugIncomingBody](../kwsdebugincomingbody.md)
  If this flag is set, the result includes the incoming message body.
- [kWSDebugIncomingHeaders](../kwsdebugincomingheaders.md)
  If this flag is set, the result includes the incoming message headers.
- [kWSDebugOutgoingBody](../kwsdebugoutgoingbody.md)
  If this flag is set, the result includes the outgoing message body.
- [kWSDebugOutgoingHeaders](../kwsdebugoutgoingheaders.md)
  If this flag is set, the result includes the outgoing message headers.
- [kWSFaultCode](../kwsfaultcode.md)
  If the result is a fault, this key returns a CFNumber with the fault code, unless the fault is a network error, in which case this field should be ignored.
- [kWSFaultExtra](../kwsfaultextra.md)
  If the result is a fault, and the fault is a network error, the key returns a CFDictionary with the network error. This key may also return a CFString, or `NULL`.
- [kWSFaultString](../kwsfaultstring.md)
  If the result is a fault, this key returns a CFString with the fault type. If the fault type is `kWSNetworkStreamFaultString`, then the fault is a network error. In the case of a network error, `kWSFaultCode` should be ignored, and `kWSFaultExtra` returns a dictionary indicating the network error.
- [kWSHTTPExtraHeaders](../kwshttpextraheaders.md)
  A CFDictionary of `{ key (CFString), val (CFString) }` pairs.
- [kWSHTTPFollowsRedirects](../kwshttpfollowsredirects.md)
  A CFBoolean that controls whether the invocation follows redirects (default is false).
- [kWSHTTPMessage](../kwshttpmessage.md)
  The message.
- [kWSHTTPProxy](../kwshttpproxy.md)
  The `CFURLRef` of the SOCKS proxy.
- [kWSHTTPResponseMessage](../kwshttpresponsemessage.md)
  The key used to retrieve the response from the reply dictionary..
- [kWSHTTPVersion](../kwshttpversion.md)
  The `CFHTTPMessageRef` version such as “http/1.1”.
- [kWSMethodInvocationResult](../kwsmethodinvocationresult.md)
  Dictionary entry if the invocation result is not a fault.  If you don't know what field to ask for, you can ask for this key.  You can also specify the name of a reply parameter in the invocation using `kWSMethodInvocationResultParameterName`. This will add an alias for the given name to the result dictionary so that this key will return the named parameter.
- [kWSMethodInvocationResultParameterName](../kwsmethodinvocationresultparametername.md)
  Set this property to create an alias to a parameter to be returned by `kWSMethodInvocationResult`. Pass in the parameter name as a `CFStringRef`.
- [kWSMethodInvocationTimeoutValue](../kwsmethodinvocationtimeoutvalue.md)
- [kWSNetworkStreamFaultString](../kwsnetworkstreamfaultstring.md)
  If `kWSFaultExtra` is a dictionary, this key returns a CFString from that dictionary for debug purposes.
- [kWSRecordNamespaceURI](../kwsrecordnamespaceuri.md)
  A  `CFStringRef` containing the namespace.
- [kWSRecordParameterOrder](../kwsrecordparameterorder.md)
  A `CFArrayRef` of `CFStringRefs` containing the parameter names, in order.
- [kWSRecordType](../kwsrecordtype.md)
  A `CFStringRef` containing the record type.
- [kWSSOAP1999Protocol](../kwssoap1999protocol.md)
  SOAP v1.1 protocol.
- [kWSSOAP2001Protocol](../kwssoap2001protocol.md)
  SOAP v1.2 protocol.
- [kWSSOAPBodyEncodingStyle](../kwssoapbodyencodingstyle.md)
- [kWSSOAPMessageHeaders](../kwssoapmessageheaders.md)
  A `CFArrayRef` of XML header elements, as `CFStringRefs`.
- [kWSSOAPMethodNamespaceURI](../kwssoapmethodnamespaceuri.md)
- [kWSSOAPStyleDoc](../kwssoapstyledoc.md)
- [kWSSOAPStyleRPC](../kwssoapstylerpc.md)
- [kWSStreamErrorDomain](../kwsstreamerrordomain.md)
  If `kWSFaultExtra` is a dictionary, this key returns a `CFNumberRef` from that dictionary containing domain number. See `CFStream.h` for domain numbers.
- [kWSStreamErrorError](../kwsstreamerrorerror.md)
  If `kWSFaultExtra` is a dictionary, this key returns a `CFNumberRef` from that dictionary containing error number. See `CFStream.h` for error numbers.
- [kWSStreamErrorMessage](../kwsstreamerrormessage.md)
  If `kWSFaultExtra` is a dictionary, this key returns a CFString from that dictionary containing the stream error message.
- [kWSXMLRPCProtocol](../kwsxmlrpcprotocol.md)
  XML-RPC protocol.
### Data Types
- [WSClientContextCopyDescriptionCallBackProcPtr](../wsclientcontextcopydescriptioncallbackprocptr.md)
  This is the callback that copies the information.
- [WSClientContextReleaseCallBackProcPtr](../wsclientcontextreleasecallbackprocptr.md)
  This is the callback that releases the information.
- [WSClientContextRetainCallBackProcPtr](../wsclientcontextretaincallbackprocptr.md)
  This is the callback that retains the information.
- [WSMethodInvocationCallBackProcPtr](../wsmethodinvocationcallbackprocptr.md)
  This is the callback that handles method invocation completion when the method is invoked asynchronously.
- [WSMethodInvocationDeserializationProcPtr](../wsmethodinvocationdeserializationprocptr.md)
  This is an optional callback that handles custom deserialization of a particular data type for a method response.
- [WSMethodInvocationRef](../wsmethodinvocationref.md)
  An opaque reference to a web services method invocation.
- [WSMethodInvocationSerializationProcPtr](../wsmethodinvocationserializationprocptr.md)
  This is an optional callback that handles custom serialization of a particular data type for method invocation.
- [WSProtocolHandlerDeserializationProcPtr](../wsprotocolhandlerdeserializationprocptr.md)
  This is an optional callback that handles custom deserialization of a particular data type for a protocol handler.
- [WSProtocolHandlerRef](../wsprotocolhandlerref.md)
  An opaque reference to a web services protocol handler.
- [WSProtocolHandlerSerializationProcPtr](../wsprotocolhandlerserializationprocptr.md)
  This is an optional callback that handles custom serialization of a particular data type for a protocol handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/os_services/web_services)*
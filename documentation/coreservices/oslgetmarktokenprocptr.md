# OSLGetMarkTokenProcPtr

**Framework**: Core Services  
**Kind**: tdef

Defines a pointer to a mark token callback function. Your mark token function returns a mark token.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias OSLGetMarkTokenProcPtr = (UnsafePointer<AEDesc>?, DescType, UnsafeMutablePointer<AEDesc>?) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). Your mark token function should return `noErr` if it successfully supplies a mark token and `errAEEventNotHandled` if it fails to supply a mark token. When the Apple Event Manager gets an error result of `errAEEventNotHandled` after calling a mark token function, it attempts to get a mark token by calling the equivalent system marking callback function.

#### Discussion

To get a mark token, the Apple Event Manager calls your mark token function. Like other tokens, the mark token returned can be a descriptor of any type; however, unlike other tokens, a mark token identifies the way your application will mark Apple event objects during the current session while resolving a single object specifier that specifies the key form `formTest`. 

A mark token is valid until the Apple Event Manager either disposes of it by calling [`AEDisposeToken(_:)`](1446783-aedisposetoken.md) or returns it as the result of the [`AEResolve(_:_:_:)`](1449720-aeresolve.md) function. If the final result of a call to `AEResolve` is a mark token, the Apple event objects currently marked for that mark token are those specified by the object specifier passed to `AEResolve`, and your application can proceed to do whatever the Apple event has requested. Note that your application is responsible for disposing of a final mark token with a call to `AEDisposeToken`, just as for any other final token.

If your application supports marking, it should also provide a token disposal function modeled after the token disposal function described in [`OSLDisposeTokenProcPtr`](osldisposetokenprocptr.md). When the Apple Event Manager calls `AEDisposeToken` to dispose of a mark token that is not the final result of a call to `AEResolve`, the subsequent call to your token disposal function lets you know that you can unmark the Apple event objects marked with that mark token. A call to `AEDisposeDesc` to dispose of a mark token (which would occur if you did not provide a token disposal function) would go unnoticed.

To provide a pointer to your mark token callback function, you create a universal procedure pointer (UPP) of type [`OSLGetMarkTokenUPP`](oslgetmarktokenupp.md), using the function [`NewOSLGetMarkTokenUPP(_:)`](1445166-newoslgetmarktokenupp.md). You can do so with code like the following:

```occ
OSLGetMarkTokenUPP MyGetMarkTokenUPP;
MyGetMarkTokenUPP = NewOSLGetMarkTokenUPP (&MyGetMarkTokenCallback)
```

You can then pass the UPP `MyGetMarkTokenUPP` as a parameter to the [`AESetObjectCallbacks(_:_:_:_:_:_:_:)`](1447756-aesetobjectcallbacks.md) function or the [`AEInstallSpecialHandler(_:_:_:)`](1445532-aeinstallspecialhandler.md) function.

If you wish to call your mark token callback function directly, you can use the [`InvokeOSLGetMarkTokenUPP(_:_:_:_:)`](1441894-invokeoslgetmarktokenupp.md) function.

After you are finished with your mark token callback function, you can dispose of the UPP with the [`DisposeOSLGetMarkTokenUPP(_:)`](1442377-disposeoslgetmarktokenupp.md) function. However, if you will use the same mark token function in subsequent calls to the function `AESetObjectCallbacks` or the function `AEInstallSpecialHandler`, you can reuse the same UPP, rather than dispose of it and later create a new UPP. 

## Parameters

- `dContainerToken`: A pointer to the Apple event object that contains the elements to be marked with the mark token. (Token is defined in  . See  .
- `containerClass`: The object class of the container that contains the objects to be marked. See  .
- `result`: A pointer to a descriptor where your mark token function should return a mark token. If your function can’t return a mark token, it should return a null descriptor. See  .

## See Also

- [typealias AERemoteProcessResolverCallback](aeremoteprocessresolvercallback.md)
  Defines a pointer to a function the Apple Event Manager calls when the asynchronous execution of a remote process resolver completes, either due to success or failure, after a call to the `AERemoteProcessResolverScheduleWithRunLoop` function. Your callback function can use the reference passed to it to get the remote process information.
- [typealias AEDisposeExternalProcPtr](aedisposeexternalprocptr.md)
  Defines a pointer to a function the Apple Event Manager calls to dispose of a descriptor created by the `AECreateDescFromExternalPtr` function. Your callback function disposes of the buffer you originally passed to that function.
- [typealias AECoerceDescProcPtr](aecoercedescprocptr.md)
  Defines a pointer to a function that coerces data stored in a descriptor. Your descriptor coercion callback function coerces the data from the passed descriptor to the specified type, returning the coerced data in a second descriptor.
- [typealias AECoercePtrProcPtr](aecoerceptrprocptr.md)
  Defines a pointer to a function that coerces data stored in a buffer. Your pointer coercion callback routine coerces the data from the passed buffer to the specified type, returning the coerced data in a descriptor.
- [typealias AEEventHandlerProcPtr](aeeventhandlerprocptr.md)
  Defines a pointer to a function that handles one or more Apple events. Your Apple event handler function performs any action requested by the Apple event, adds parameters to the reply Apple event if appropriate (possibly including error information), and returns a result code.
- [typealias OSLAccessorProcPtr](oslaccessorprocptr.md)
  Your object accessor function either finds elements or properties of an Apple event object.
- [typealias OSLAdjustMarksProcPtr](osladjustmarksprocptr.md)
  Defines a pointer to an adjust marks callback function. Your adjust marks function unmarks objects previously marked by a call to your marking function.
- [typealias OSLCompareProcPtr](oslcompareprocptr.md)
  Defines a pointer to an object comparison callback function. Your object comparison function compares one Apple event object to another or to the data for a descriptor.
- [typealias OSLCountProcPtr](oslcountprocptr.md)
  Defines a pointer to an object counting callback function. Your object counting function counts the number of Apple event objects of a specified class in a specified container object.
- [typealias OSLDisposeTokenProcPtr](osldisposetokenprocptr.md)
  Defines a pointer to a dispose token callback function. Your dispose token function, required only if you use a complex token format, disposes of the specified token.
- [typealias OSLGetErrDescProcPtr](oslgeterrdescprocptr.md)
  Defines a pointer to an error descriptor callback function. Your error descriptor callback function supplies a pointer to an address where the Apple Event Manager can store the current descriptor if an error occurs during a call to the `AEResolve` function.
- [typealias OSLMarkProcPtr](oslmarkprocptr.md)
  Defines a pointer to an object marking callback function. Your object-marking function marks a specific Apple event object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/oslgetmarktokenprocptr)*
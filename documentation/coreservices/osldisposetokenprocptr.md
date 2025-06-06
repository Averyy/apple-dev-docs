# OSLDisposeTokenProcPtr

**Framework**: Core Services  
**Kind**: tdef

Defines a pointer to a dispose token callback function. Your dispose token function, required only if you use a complex token format, disposes of the specified token.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias OSLDisposeTokenProcPtr = (UnsafeMutablePointer<AEDesc>?) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). Your token disposal function should return `noErr` if it successfully disposed of the token and `errAEEventNotHandled` if it can’t dispose of the token. When the Apple Event Manager receives the result code `errAEEventNotHandled` after calling a token disposal function, it attempts to use other methods of disposing of the specified token, such as calling an equivalent system token disposal function if one is available or, if that fails, by calling [`AEDisposeDesc(_:)`](1444208-aedisposedesc.md).

#### Discussion

The Apple Event Manager calls your token disposal function whenever it needs to dispose of a token. It also calls your disposal function when your application calls the [`AEDisposeToken(_:)`](1446783-aedisposetoken.md) function. If your application does not provide a token disposal function, the Apple Event Manager calls [`AEDisposeDesc(_:)`](1444208-aedisposedesc.md) instead.

Your token disposal function must be able to dispose of all of the token types used by your application. 

If your application supports marking, a call to `MyDisposeTokenCallback` to dispose of a mark token lets your application know that it can unmark the objects marked with that mark token, as described in the Discussion section for [`OSLGetMarkTokenProcPtr`](oslgetmarktokenprocptr.md).

To provide a pointer to your token disposal callback function, you create a universal procedure pointer (UPP) of type [`OSLDisposeTokenUPP`](osldisposetokenupp.md), using the function [`NewOSLDisposeTokenUPP(_:)`](1450027-newosldisposetokenupp.md). You can do so with code like the following:

```occ
OSLDisposeTokenUPP MyDisposeTokenUPP;
MyDisposeTokenUPP = NewOSLDisposeTokenUPP (&MyDisposeTokenCallback)
```

You can then pass the UPP `MyDisposeTokenUPP` as a parameter to the [`AESetObjectCallbacks(_:_:_:_:_:_:_:)`](1447756-aesetobjectcallbacks.md) function or the [`AEInstallSpecialHandler(_:_:_:)`](1445532-aeinstallspecialhandler.md) function.

If you wish to call your token disposal callback function directly, you can use the [`InvokeOSLDisposeTokenUPP(_:_:)`](1443963-invokeosldisposetokenupp.md) function.

After you are finished with your token disposal callback function, you can dispose of the UPP with the [`DisposeOSLDisposeTokenUPP(_:)`](1442670-disposeosldisposetokenupp.md) function. However, if you will use the same token disposal function in subsequent calls to the function `AESetObjectCallbacks` or the function `AEInstallSpecialHandler`, you can reuse the same UPP, rather than dispose of it and later create a new UPP. 

## Parameters

- `unneededToken`: A pointer to the token to dispose of. (Token is defined in  .) On successful return, your function must set this to the null descriptor. See  .

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
- [typealias OSLGetErrDescProcPtr](oslgeterrdescprocptr.md)
  Defines a pointer to an error descriptor callback function. Your error descriptor callback function supplies a pointer to an address where the Apple Event Manager can store the current descriptor if an error occurs during a call to the `AEResolve` function.
- [typealias OSLGetMarkTokenProcPtr](oslgetmarktokenprocptr.md)
  Defines a pointer to a mark token callback function. Your mark token function returns a mark token.
- [typealias OSLMarkProcPtr](oslmarkprocptr.md)
  Defines a pointer to an object marking callback function. Your object-marking function marks a specific Apple event object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/osldisposetokenprocptr)*
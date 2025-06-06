# OSLMarkProcPtr

**Framework**: Core Services  
**Kind**: tdef

Defines a pointer to an object marking callback function. Your object-marking function marks a specific Apple event object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias OSLMarkProcPtr = (UnsafePointer<AEDesc>?, UnsafePointer<AEDesc>?, Int) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). Your object marking function should return `noErr` if it successfully marks the Apple event object and `errAEEventNotHandled` if it fails to mark the object. When the Apple Event Manager gets an error result of `errAEEventNotHandled` after calling an object marking function, it attempts to get mark the object by calling the equivalent system object marking function.

#### Discussion

To mark an Apple event object using the current mark token, the Apple Event Manager calls the object-marking function provided by your application. In addition to marking the specified object, your `MyMarkCallback` function should record the mark count for each object that it marks. The mark count recorded for each marked object allows your application to determine which of a set of marked tokens pass a test, as described in the Discussion section for the [`OSLAdjustMarksProcPtr`](osladjustmarksprocptr.md) function.

To provide a pointer to your mark callback function, you create a universal procedure pointer (UPP) of type [`OSLMarkUPP`](oslmarkupp.md), using the function [`NewOSLMarkUPP(_:)`](1446942-newoslmarkupp.md). You can do so with code like the following:

```occ
OSLMarkUPP MyMarkUPP;
MyMarkUPP = NewOSLMarkUPP (&MyMarkCallback)
```

You can then pass the UPP `MyMarkUPP` as a parameter to the [`AESetObjectCallbacks(_:_:_:_:_:_:_:)`](1447756-aesetobjectcallbacks.md) function or the [`AEInstallSpecialHandler(_:_:_:)`](1445532-aeinstallspecialhandler.md) function.

If you wish to call your mark callback function directly, you can use the [`InvokeOSLMarkUPP(_:_:_:_:)`](1447444-invokeoslmarkupp.md) function.

After you are finished with your mark callback function, you can dispose of the UPP with the [`DisposeOSLMarkUPP(_:)`](1449253-disposeoslmarkupp.md) function. However, if you will use the same mark function in subsequent calls to the function `AESetObjectCallbacks` or the function `AEInstallSpecialHandler`, you can reuse the same UPP, rather than dispose of it and later create a new UPP. 

## Parameters

- `dToken`: A pointer to the token for the Apple event object to be marked. (Token is defined in  . See  .
- `markToken`: A pointer to the mark token used to mark the Apple event object. See  .
- `index`: The number of times your   function has been called for the current mark token (that is, the number of Apple event objects that have so far passed the test, including the element to be marked).

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
- [typealias OSLGetMarkTokenProcPtr](oslgetmarktokenprocptr.md)
  Defines a pointer to a mark token callback function. Your mark token function returns a mark token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/oslmarkprocptr)*
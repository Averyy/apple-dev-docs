# OSLCountProcPtr

**Framework**: Core Services  
**Kind**: tdef

Defines a pointer to an object counting callback function. Your object counting function counts the number of Apple event objects of a specified class in a specified container object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias OSLCountProcPtr = (DescType, DescType, UnsafePointer<AEDesc>?, UnsafeMutablePointer<Int>?) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). Your object counting function should return `noErr` if it successfully counted the objects and `errAEEventNotHandled` if it can’t count the objects. When the Apple Event Manager receives the result code `errAEEventNotHandled` after calling an object counting function, it attempts to use other methods of counting the specified objects, such as calling an equivalent system object counting function.

#### Discussion

If you want the Apple Event Manager to help your application resolve object specifiers of key form `formTest` (and if your application doesn’t specify `kAEIDoWhose` as described in [`Callback Constants for the AEResolve Function`](apple_events/1572741-callback_constants_for_the_aeres.md)), you should provide an object comparison function, as described in [`OSLCompareProcPtr`](oslcompareprocptr.md), and an object-counting function.

The Apple Event Manager calls your object-counting function when, in the course of resolving an object specifier, the manager requires a count of the number of Apple event objects of a given class in a given container.

To provide a pointer to your object counting callback function, you create a universal procedure pointer (UPP) of type [`OSLCountUPP`](oslcountupp.md), using the function [`NewOSLCountUPP(_:)`](1448156-newoslcountupp.md). You can do so with code like the following:

```occ
OSLCountObjectsUPP MyCountObjectsUPP;
MyCountObjectsUPP = NewOSLCountObjectsUPP (&MyCountObjectsCallback)
```

You can then pass the UPP `MyCountObjectsUPP` as a parameter to the [`AESetObjectCallbacks(_:_:_:_:_:_:_:)`](1447756-aesetobjectcallbacks.md) function or the [`AEInstallSpecialHandler(_:_:_:)`](1445532-aeinstallspecialhandler.md) function.

If you wish to call your object counting callback function directly, you can use the [`InvokeOSLCountUPP(_:_:_:_:_:)`](1448030-invokeoslcountupp.md) function.

After you are finished with your object counting callback function, you can dispose of the UPP with the [`DisposeOSLCountUPP(_:)`](1443984-disposeoslcountupp.md) function. However, if you will use the same object counting function in subsequent calls to the function `AESetObjectCallbacks` or the function `AEInstallSpecialHandler`, you can reuse the same UPP, rather than dispose of it and later create a new UPP. 

## Parameters

- `desiredType`: The object class of the Apple event objects to be counted. See  .
- `containerClass`: The object class of the container for the Apple event objects to be counted. See  .
- `container`: A pointer to a token that identifies the container for the Apple event objects to be counted. (Token is defined in  . See  .
- `result`: A pointer to a variable where your object-counting function stores the number of Apple objects of the specified class in the specified container.

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
- [typealias OSLDisposeTokenProcPtr](osldisposetokenprocptr.md)
  Defines a pointer to a dispose token callback function. Your dispose token function, required only if you use a complex token format, disposes of the specified token.
- [typealias OSLGetErrDescProcPtr](oslgeterrdescprocptr.md)
  Defines a pointer to an error descriptor callback function. Your error descriptor callback function supplies a pointer to an address where the Apple Event Manager can store the current descriptor if an error occurs during a call to the `AEResolve` function.
- [typealias OSLGetMarkTokenProcPtr](oslgetmarktokenprocptr.md)
  Defines a pointer to a mark token callback function. Your mark token function returns a mark token.
- [typealias OSLMarkProcPtr](oslmarkprocptr.md)
  Defines a pointer to an object marking callback function. Your object-marking function marks a specific Apple event object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/oslcountprocptr)*
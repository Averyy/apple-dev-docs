# OSLAccessorProcPtr

**Framework**: Core Services  
**Kind**: tdef

Your object accessor function either finds elements or properties of an Apple event object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias OSLAccessorProcPtr = (DescType, UnsafePointer<AEDesc>?, DescType, DescType, UnsafePointer<AEDesc>?, UnsafeMutablePointer<AEDesc>?, SRefCon?) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). Your object accessor function should return `noErr` if it successfully located the requested object and `errAEEventNotHandled` if it could not locate the object. When the Apple Event Manager receives the result code `errAEEventNotHandled` after calling an object accessor function, it attempts to use other methods of locating the requested objects, such as calling an equivalent system object accessor function.

#### Discussion

To resolve an object specifier, your application calls the [`AEResolve(_:_:_:)`](1449720-aeresolve.md) function. `AEResolve` in turn calls application-defined object accessor functions to locate specific Apple event objects and properties in the application’s data structures. Your application provides one or more object accessor functions that can locate all the element classes and properties it supports.

Each object accessor function provided by your application should either find elements or properties of an Apple event object. The `AEResolve` function uses the object class ID of the specified Apple event object and the descriptor type of the token that identifies the object’s container to determine which object accessor function to call. To install an object accessor function, use the [`AEInstallObjectAccessor(_:_:_:_:_:)`](1447905-aeinstallobjectaccessor.md) function.

To provide a pointer to your object accessor callback function, you create a universal procedure pointer (UPP) of type [`OSLAccessorUPP`](oslaccessorupp.md), using the function [`NewOSLAccessorUPP(_:)`](1449584-newoslaccessorupp.md). You can do so with code like the following:

```occ
AEObjectAccessorUPP MyObjectAccessorUPP;
MyObjectAccessorUPP = NewAEObjectAccessorUPP (&MyObjectAccessorCallback)
```

You can then pass the UPP `MyObjectAccessorUPP` as a parameter to any function that installs or removes an object accessor, such as [`AEInstallObjectAccessor(_:_:_:_:_:)`](1447905-aeinstallobjectaccessor.md). If your application installs the same object accessor to handle more than one kind of object class or property of an Apple event, you can use the same UPP to install the accessor multiple times.

If you wish to call your object accessor callback function directly, you can use the [`InvokeOSLAccessorUPP(_:_:_:_:_:_:_:_:)`](1448978-invokeoslaccessorupp.md) function.

After you are finished with an object accessor callback function, and have removed it with the [`AERemoveObjectAccessor(_:_:_:_:)`](1442552-aeremoveobjectaccessor.md) function, you can dispose of the UPP with the [`DisposeOSLAccessorUPP(_:)`](1444684-disposeoslaccessorupp.md) function. However, don’t dispose of the UPP if any remaining accessor function uses it or if you plan to install the accessor function again. 

## Parameters

- `desiredClass`: The object class of the desired Apple event object or objects. Constants for object class IDs are described in  . See  .
- `container`: A pointer to a descriptor that specifies the container of the desired Apple event object or objects. See  .
- `containerClass`: The object class of the container. Constants for object class IDs are described in  . See  .
- `form`: The key form specified by the object specifier being resolved. Constants for key form are described in  . See  .
- `selectionData`: A pointer to a descriptor containing the key data specified by the object specifier being resolved. See  .
- `value`: A pointer to a descriptor where your object accessor routine stores a descriptor that identifies the found object. See  .
- `accessorRefcon`: A reference constant. The Apple Event Manager passes this value to your object accessor function each time it calls it. The reference constant may have a value of 0.

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
- [typealias OSLMarkProcPtr](oslmarkprocptr.md)
  Defines a pointer to an object marking callback function. Your object-marking function marks a specific Apple event object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/oslaccessorprocptr)*
# OSLAdjustMarksProcPtr

**Framework**: Core Services  
**Kind**: tdef

Defines a pointer to an adjust marks callback function. Your adjust marks function unmarks objects previously marked by a call to your marking function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias OSLAdjustMarksProcPtr = (Int, Int, UnsafePointer<AEDesc>?) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). Your adjust marks function should return `noErr` if it successfully adjusted the marks and `errAEEventNotHandled` if it could not locate the object. When the Apple Event Manager gets an error result of `errAEEventNotHandled`, it attempts to adjust the marks by calling the equivalent system mark-adjusting function.

#### Discussion

When the Apple Event Manager needs to identify either a range of elements or the absolute position of an element in a group of Apple event objects that pass a test, it can use your application’s mark-adjusting function to unmark objects previously marked by a call to your marking function.

For example, suppose an object specifier specifies `any row in the table "MyCustomers" for which the City column is "San Francisco"`. The Apple Event Manager first uses the appropriate object accessor function to locate all the rows in the table for which the City column is `"San Francisco"` and calls the application’s marking function repeatedly to mark them. It then generates a random number between 1 and the number of rows it found that passed the test and calls the application’s mark-adjusting function to unmark all the rows whose mark count does not match the randomly generated number. If the randomly chosen row has a mark count value of 5, the Apple Event Manager passes the value 5 to the mark-adjusting function in both the `newStart` parameter and the `newStop `parameter, and passes the current mark token in the `markToken` parameter.

When the Apple Event Manager calls your `MyAdjustMarksCallback `function, your application must dispose of any data structures that it created to mark the previously marked objects.

To provide a pointer to your adjust marks callback function, you create a universal procedure pointer (UPP) of type [`OSLAdjustMarksUPP`](osladjustmarksupp.md), using the function [`NewOSLAdjustMarksUPP(_:)`](1443347-newosladjustmarksupp.md). You can do so with code like the following:

```occ
OSLAdjustMarksUPP MyAdjustMarksUPP;
MyAdjustMarksUPP = NewOSLAdjustMarksUPP (&MyAdjustMarksCallback)
```

You can then pass the UPP `MyAdjustMarksUPP` as a parameter to the [`AESetObjectCallbacks(_:_:_:_:_:_:_:)`](1447756-aesetobjectcallbacks.md) function or the [`AEInstallSpecialHandler(_:_:_:)`](1445532-aeinstallspecialhandler.md) function.

If you wish to call your adjust marks callback function directly, you can use the [`InvokeOSLAdjustMarksUPP(_:_:_:_:)`](1448506-invokeosladjustmarksupp.md) function.

After you are finished with your adjust marks callback function, you can dispose of the UPP with the [`DisposeOSLAdjustMarksUPP(_:)`](1443940-disposeosladjustmarksupp.md) function. However, if you will use the same adjust marks function in subsequent calls to the function `AESetObjectCallbacks` or the function `AEInstallSpecialHandler`, you can reuse the same UPP, rather than dispose of it and later create a new UPP. 

## Parameters

- `newStart`: The mark count value (provided when the   callback function was called to mark the object) for the first object in the new set of marked objects.
- `newStop`: The mark count value (provided when the   callback function was called to mark the object) for the last object in the new set of marked objects.
- `markToken`: A pointer to the mark token for the marked objects. (Token is defined in  . See  .

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/osladjustmarksprocptr)*
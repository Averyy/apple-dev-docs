# AEResolve(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Resolves an object specifier.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AEResolve(_ objectSpecifier: UnsafePointer<AEDesc>!, _ callbackFlags: Int16, _ theToken: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145). The `AEResolve` function returns any result code returned by one of your application’s object accessor functions or object callback functions. For example, an object accessor function can return `errAENoSuchObject` (–1728) when it can’t find an Apple event object, or it can return more specific result codes. If any object accessor function or object callback function returns a result code other than `noErr` or `errAEEventNotHandled`, `AEResolve` immediately disposes of any existing tokens and returns. The result code it returns in this case is the result code returned by the object accessor function or the object callback function.

#### Discussion

If an Apple event parameter consists of an object specifier, your handler for the event typically calls the `AEResolve` function to begin the process of resolving the object specifier.

The `AEResolve` function resolves the object specifier passed in the `objectSpecifier` parameter with the help of your object accessor functions, described in [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager), and the object callback functions, described in [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager).

For information on how to receive error information from the `AEResolve` function, see [`OSLGetErrDescProcPtr`](oslgeterrdescprocptr.md). 

## Parameters

- `objectSpecifier`: A pointer to the object specifier to resolve. See  .
- `callbackFlags`: A value that determines what additional assistance, if any, your application can give the Apple Event Manager when it parses the object specifier. The value is specified by adding the desired constants described in  . Most applications use  .
- `theToken`: Whenever the   function returns final token to your event handler as the result of the resolving an object specifier passed to  , your application must deallocate the memory used by the token. If your application uses complex tokens, it must dispose of the token by calling  . If your application uses simple tokens, you can use either   or  . See  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1449720-aeresolve)*
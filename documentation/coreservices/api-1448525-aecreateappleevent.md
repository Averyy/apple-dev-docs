# AECreateAppleEvent(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates an Apple event with several important attributes but no parameters.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AECreateAppleEvent(_ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ target: UnsafePointer<AEAddressDesc>!, _ returnID: AEReturnID, _ transactionID: AETransactionID, _ result: UnsafeMutablePointer<AppleEvent>!) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1656145).

#### Discussion

The `AECreateAppleEvent `function creates an empty Apple event. You can add parameters to the Apple event after you create it with the functions described in [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager). 

##### 1770171

Thread safe starting in OS X v10.2.

## Parameters

- `theAEEventClass`: The event class of the Apple event to create. This parameter becomes accessible through the   attribute of the Apple event. Some event classes are described in  . See  .
- `theAEEventID`: The event ID of the Apple event to create. This parameter becomes accessible through the  attribute of the Apple event. Some event IDs are described in  . See  .
- `target`: A pointer to an address descriptor. Before calling  , you set the descriptor to identify the target (or server) application for the Apple event. This parameter becomes accessible through the   attribute of the Apple event. See  .
- `returnID`: The return ID for the created Apple event. If you pass a value of  , the Apple Event Manager assigns the created Apple event a return ID that is unique to the current session. If you pass any other value, the Apple Event Manager assigns that value for the ID. This parameter becomes accessible through the   attribute of the Apple event. The return ID constant is described in  . See  .
- `transactionID`: The transaction ID for this Apple event. A transaction is a sequence of Apple events that are sent back and forth between the client and server applications, beginning with the client’s initial request for a service. All Apple events that are part of a transaction must have the same transaction ID. You can specify the   constant if the Apple event is not one of a series of interdependent Apple events. This parameter becomes accessible through the   attribute of the Apple event. This transaction ID constant is described in  . See  .
- `result`: A pointer to an Apple event. On successful return, the new Apple event. On error, a null descriptor (one with descriptor type  ). If the function returns successfully, your application should call the   function to dispose of the resulting Apple event after it has finished using it. See the   data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448525-aecreateappleevent)*
# AETransactionID

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Specifies a transaction ID.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AETransactionID = Int32
```

```c
typedef SInt32 AETransactionID;
```

#### Discussion

A transaction is a sequence of Apple events that are sent back and forth between the client and server applications, beginning with the client’s initial request for a service. When you call the [`AECreateAppleEvent(_:_:_:_:_:_:)`](./api-1448525-aecreateappleevent.md) function, you pass a value of type `AETransactionID` for the `transactionID` parameter. [ID Constants for the AECreateAppleEvent Function](./apple_events/api-1542799-id_constants_for_the_aecreateapp.md) lists the valid constant values for a variable or parameter of this type. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aetransactionid)*
# ID Constants for the AECreateAppleEvent Function

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify values for the ID parameters of the `AECreateAppleEvent` function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : int {
    ...
};
```

## Topics

### Constants
- [kAutoGenerateReturnID](./api-1542799-id_constants_for_the_aecreateapp/kautogeneratereturnid.md)
  If you pass this value for the `returnID` parameter of the [`AECreateAppleEvent`](./api-1448525-aecreateappleevent.md) function, the Apple Event Manager assigns to the created Apple event a return ID that is unique to the current session.
- [kAnyTransactionID](./api-1542799-id_constants_for_the_aecreateapp/kanytransactionid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542799-id_constants_for_the_aecreateapp)*
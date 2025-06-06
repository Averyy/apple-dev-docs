# AEReturnID

**Framework**: Core Services  
**Kind**: tdef

Specifies a return ID for a created Apple event.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AEReturnID = Int16
```

#### Discussion

When you call the [`AECreateAppleEvent(_:_:_:_:_:_:)`](1448525-aecreateappleevent.md) function, you pass a value of type `AEReturnID` for the `returnID` parameter. [`ID Constants for the AECreateAppleEvent Function`](apple_events/1542799-id_constants_for_the_aecreateapp.md) lists the valid constant values for a variable or parameter of this type. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aereturnid)*
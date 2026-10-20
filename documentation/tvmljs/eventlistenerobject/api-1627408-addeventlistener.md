# addEventListener

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Creates an event listener.

**Availability**:
- tvOS 9.0+

## Declaration

```
void addEventListener(
    in String type, 
    in Object listener, 
    in optional Object extraInfo
);
```

#### Discussion

Use the `extraInfo` parameter to handle information for different types of events; for example, specifying the type of metadata a metadata listener is listening for.

## Parameters

- `type`: The developer-defined name of the event type to add.
- `listener`: The listener object to be added. This object is typically a function.
- `extraInfo`: Optional parameter that is used to handle specific types of events. Different events have different formats.

## See Also

### Adding and Removing Event Listeners
- [removeEventListener](./api-1627423-removeeventlistener.md)
  Removes the designated event listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/eventlistenerobject/1627408-addeventlistener)*